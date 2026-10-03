/* DermRx Desk — standalone runtime.
   Provides the same window.claude.use("db" | "assets" | "downloads") API the app was written against.
   - brands + templates  → shared Firestore (everyone reads; only the admin email can write)
   - everything else     → this phone only (IndexedDB): patients, visits, photos, scores, drug-safety edits, clinic settings
*/
(function () {
  "use strict";
  const CFG = window.DRX_CONFIG || {};
  const SHARED = new Set(["brands", "templates"]);
  const clone = o => JSON.parse(JSON.stringify(o ?? null));
  const rid = () => Array.from(crypto.getRandomValues(new Uint8Array(10)), b => b.toString(16).padStart(2, "0")).join("");
  const err = (code, message) => Object.assign(new Error(message || code), { code });

  /* ---------------- IndexedDB ---------------- */
  const idbP = new Promise((res, rej) => {
    const r = indexedDB.open("dermrx", 1);
    r.onupgradeneeded = () => { const d = r.result; d.createObjectStore("docs"); d.createObjectStore("blobs"); };
    r.onsuccess = () => res(r.result); r.onerror = () => rej(r.error);
  });
  const tx = (store, mode, fn) => idbP.then(d => new Promise((res, rej) => {
    const t = d.transaction(store, mode); const s = t.objectStore(store); const out = fn(s);
    t.oncomplete = () => res(out && "result" in out ? out.result : out); t.onerror = () => rej(t.error); t.onabort = () => rej(t.error || err("quota_exceeded"));
  }));

  /* ---------------- local collections ---------------- */
  const L = { data: {}, subs: {}, docSubs: {} };
  const ready = tx("docs", "readonly", s => {
    const req = s.openCursor();
    req.onsuccess = () => { const c = req.result; if (!c) return; const [col, id] = String(c.key).split("\u0000"); (L.data[col] ||= new Map()).set(id, c.value); c.continue(); };
  }).catch(() => {});
  const map = col => (L.data[col] ||= new Map());
  const snapOf = col => ({ docs: [...map(col)].map(([id, d]) => ({ id, exists: true, data: () => clone(d) })), size: map(col).size, empty: !map(col).size });
  const docSnap = (col, id) => { const d = map(col).get(id); return { id, exists: !!d, data: () => (d ? clone(d) : undefined) }; };
  function emit(col, id) {
    (L.subs[col] || []).forEach(f => { try { f(snapOf(col)); } catch {} });
    (L.docSubs[col + "/" + id] || []).forEach(f => { try { f(docSnap(col, id)); } catch {} });
  }
  async function persist(col, id, val) {
    await tx("docs", "readwrite", s => (val === undefined ? s.delete(col + "\u0000" + id) : s.put(val, col + "\u0000" + id)));
  }
  function localDoc(col, id) {
    id = id || rid();
    return {
      id,
      async get() { await ready; return docSnap(col, id); },
      async set(d) { await ready; const v = clone(d); await persist(col, id, v); map(col).set(id, v); emit(col, id); },
      async update(d) { await ready; const cur = map(col).get(id); if (!cur) throw err("not_found"); const v = { ...cur, ...clone(d) }; await persist(col, id, v); map(col).set(id, v); emit(col, id); },
      async delete() { await ready; await persist(col, id, undefined); map(col).delete(id); emit(col, id); },
      onSnapshot(cb) { const k = col + "/" + id; (L.docSubs[k] ||= []).push(cb); ready.then(() => cb(docSnap(col, id))); return () => { L.docSubs[k] = L.docSubs[k].filter(f => f !== cb); }; }
    };
  }
  function localCol(col) {
    return {
      doc: id => localDoc(col, id),
      async get() { await ready; return snapOf(col); },
      onSnapshot(cb) { (L.subs[col] ||= []).push(cb); ready.then(() => cb(snapOf(col))); return () => { L.subs[col] = L.subs[col].filter(f => f !== cb); }; }
    };
  }

  /* ---------------- shared collections (Firestore) ---------------- */
  const DRX = window.DRX = { configured: false, user: null, isAdmin: false, authSubs: [], seed: null, status: {} };
  let fs = null, auth = null;
  const adminEmail = String(CFG.adminEmail || "").toLowerCase();
  if (CFG.firebase && CFG.firebase.apiKey && window.firebase) {
    try {
      firebase.initializeApp(CFG.firebase);
      fs = firebase.firestore();
      fs.enablePersistence({ synchronizeTabs: true }).catch(() => {});
      auth = firebase.auth();
      DRX.configured = true;
      auth.onAuthStateChanged(u => {
        DRX.user = u ? { email: u.email } : null;
        DRX.isAdmin = !!(u && u.email && u.email.toLowerCase() === adminEmail);
        DRX.authSubs.forEach(f => { try { f(); } catch {} });
      });
    } catch (e) { console.warn("Firebase init failed", e); fs = null; }
  }
  const seedP = fetch("seed.json", { cache: "no-cache" }).then(r => r.ok ? r.json() : {}).catch(() => ({})).then(s => (DRX.seed = s || {}));
  const seedSnap = col => { const arr = (DRX.seed && DRX.seed[col]) || []; return { docs: arr.map(({ id, ...d }) => ({ id, exists: true, data: () => clone(d) })), size: arr.length, empty: !arr.length }; };

  function guardWrite() {
    if (!fs) throw err("admin_only", "Shared list isn’t connected yet");
    if (!DRX.isAdmin) throw err("admin_only", "Only the admin can change the shared medicines and templates");
  }
  function sharedCol(col) {
    if (!fs) {
      // Not connected to the cloud yet: show the bundled list, read-only.
      return {
        doc: id => ({ id: id || rid(), set: async () => guardWrite(), update: async () => guardWrite(), delete: async () => guardWrite(), get: async () => ({ exists: false, data: () => undefined }) }),
        onSnapshot(cb) { seedP.then(() => { DRX.status[col] = { source: "bundled", n: seedSnap(col).size }; cb(seedSnap(col)); }); return () => {}; }
      };
    }
    const ref = fs.collection(col);
    return {
      doc(id) {
        const d = id ? ref.doc(id) : ref.doc();
        return {
          id: d.id,
          get: () => d.get(),
          async set(v) { guardWrite(); await d.set(clone(v)); },
          async update(v) { guardWrite(); await d.update(clone(v)); },
          async delete() { guardWrite(); await d.delete(); },
          onSnapshot: (cb, e) => d.onSnapshot(cb, e)
        };
      },
      onSnapshot(cb, e) {
        return ref.onSnapshot({ includeMetadataChanges: false }, snap => {
          const fromServer = !snap.metadata.fromCache;
          if (snap.empty) {
            // Nothing published yet (or first launch offline): fall back to the bundled list.
            seedP.then(() => { DRX.status[col] = { source: "bundled", n: seedSnap(col).size }; DRX.statusHook?.(); cb(seedSnap(col)); });
            return;
          }
          DRX.status[col] = { source: fromServer ? "cloud" : "cache", n: snap.size, at: Date.now() }; DRX.statusHook?.();
          cb(snap);
        }, er => { seedP.then(() => cb(seedSnap(col))); e && e(er); });
      }
    };
  }

  const db = {
    collection: col => (SHARED.has(col) ? sharedCol(col) : localCol(col)),
    doc(path) { const [col, id] = path.split("/"); return SHARED.has(col) ? sharedCol(col).doc(id) : localDoc(col, id); }
  };

  /* ---------------- admin helpers (used by the Sync & sharing panel) ---------------- */
  DRX.onAuth = f => { DRX.authSubs.push(f); return () => { DRX.authSubs = DRX.authSubs.filter(g => g !== f); }; };
  DRX.signIn = (email, pw) => { if (!auth) return Promise.reject(err("not_configured")); return auth.signInWithEmailAndPassword(email.trim(), pw); };
  DRX.signOut = () => auth ? auth.signOut() : Promise.resolve();
  DRX.adminEmail = adminEmail;
  DRX.cloudCount = async col => { if (!fs) return null; try { const s = await fs.collection(col).get({ source: "server" }); return s.size; } catch { return null; } };
  /* Upload the bundled list to the cloud. mode "missing" = add only items not already there; "all" = overwrite all. */
  DRX.publishSeed = async (mode, onProgress) => {
    guardWrite(); await seedP;
    let done = 0; const total = ["brands", "templates"].reduce((n, c) => n + ((DRX.seed[c] || []).length), 0);
    for (const col of ["brands", "templates"]) {
      const items = DRX.seed[col] || [];
      const existing = new Set(); if (mode === "missing") { const s = await fs.collection(col).get(); s.forEach(d => existing.add(d.id)); }
      for (let i = 0; i < items.length; i += 400) {
        const b = fs.batch();
        items.slice(i, i + 400).forEach(({ id, ...d }) => { if (!existing.has(id)) b.set(fs.collection(col).doc(id), clone(d)); });
        await b.commit(); done += Math.min(400, items.length - i); onProgress && onProgress(done, total);
      }
    }
    return total;
  };
  /* Restore a backup file (from the Claude version or this app) into this phone. */
  DRX.restoreLocal = async data => {
    await ready; let n = 0;
    const put = async (col, arr) => { for (const x of arr || []) { const { id, ...d } = x; if (!id) continue; await persist(col, id, clone(d)); map(col).set(id, clone(d)); n++; } emit(col); };
    await put("people", data.people); await put("visits", data.visits); await put("scores", data.scores);
    if (data.settings && Object.keys(data.settings).length) { const st = clone(data.settings); delete st.signatureId; await persist("settings", "clinic", st); map("settings").set("clinic", st); emit("settings", "clinic"); }
    if (data.drugSafetyEdits) for (const [k, v] of Object.entries(data.drugSafetyEdits)) { const { k: _k, ...d } = v || {}; await persist("drugsafety", k, clone(d)); map("drugsafety").set(k, clone(d)); n++; }
    emit("drugsafety");
    return n;
  };

  /* ---------------- assets (photos, reports) — stored on this phone ---------------- */
  const assets = {
    async upload(blob, opts) {
      const type = (opts && opts.type) || blob.type || "application/octet-stream";
      if (blob.size > 20 * 1024 * 1024) throw err("too_large");
      if (!/^(image\/|application\/pdf)/.test(type)) throw err("unsupported_type");
      const id = rid() + rid().slice(0, 12);
      try { await tx("blobs", "readwrite", s => s.put({ blob, type, size: blob.size, at: Date.now() }, id)); }
      catch { throw err("quota_or_state"); }
      return { id, contentType: type, url: "/_blob/" + id };
    },
    async delete(id) { await tx("blobs", "readwrite", s => s.delete(id)); },
    async list() {
      let files = 0, bytes = 0;
      await tx("blobs", "readonly", s => { const r = s.openCursor(); r.onsuccess = () => { const c = r.result; if (!c) return; files++; bytes += c.value.size || 0; c.continue(); }; });
      let maxBytes = 1024 * 1024 * 1024; try { const e = await navigator.storage.estimate(); if (e.quota) maxBytes = e.quota; } catch {}
      return { usage: { files, bytes, maxBytes } };
    }
  };
  try { navigator.storage && navigator.storage.persist && navigator.storage.persist(); } catch {}

  /* ---------------- downloads ---------------- */
  const downloads = {
    async save({ filename, data }) {
      const blob = data instanceof Blob ? data : new Blob([data], { type: /\.json$/.test(filename) ? "application/json" : /\.csv$/.test(filename) ? "text/csv" : /\.html$/.test(filename) ? "text/html" : "application/octet-stream" });
      const url = URL.createObjectURL(blob); const a = document.createElement("a");
      a.href = url; a.download = filename; document.body.appendChild(a); a.click(); a.remove();
      setTimeout(() => URL.revokeObjectURL(url), 60000);
      return { status: "saved" };
    }
  };

  /* ---------------- service worker (offline + /_blob/ photos) ---------------- */
  if ("serviceWorker" in navigator && location.protocol !== "file:") {
    navigator.serviceWorker.register("sw.js").catch(() => {});
  }
  // Until the service worker controls the page, resolve /_blob/ images directly.
  const blobURL = async id => { const v = await tx("blobs", "readonly", s => s.get(id)); return v ? URL.createObjectURL(v.blob) : ""; };
  DRX.blobURL = blobURL;
  new MutationObserver(ms => {
    if (navigator.serviceWorker && navigator.serviceWorker.controller) return;
    const fix = img => { const s = img.getAttribute("src") || ""; const i = s.indexOf("/_blob/"); if (i >= 0) blobURL(s.slice(i + 7)).then(u => { if (u) img.src = u; }); };
    for (const m of ms) {
      if (m.type === "attributes") { if (m.target.tagName === "IMG") fix(m.target); continue; }
      for (const n of m.addedNodes) {
        if (n.nodeType !== 1) continue;
        (n.tagName === "IMG" ? [n] : n.querySelectorAll ? n.querySelectorAll("img[src*='/_blob/']") : []).forEach(fix);
      }
    }
  }).observe(document.documentElement, { childList: true, subtree: true, attributes: true, attributeFilter: ["src"] });

  window.claude = {
    use: async name => (name === "db" ? db : name === "assets" ? assets : name === "downloads" ? downloads : null)
  };
})();
