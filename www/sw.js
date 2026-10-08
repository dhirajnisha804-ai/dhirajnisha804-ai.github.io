/* DermRx Desk service worker: works offline, always prefers the latest version when online,
   and serves locally stored photos at /_blob/<id>. */
const VERSION = "202610081017";
const SHELL = "drx-shell-" + VERSION;
const FILES = ["./", "index.html", "drx-shim.js", "config.js", "seed.json", "prices.json", "manifest.webmanifest",
  "vendor/firebase-app-compat.js", "vendor/firebase-auth-compat.js", "vendor/firebase-firestore-compat.js",
  "vendor/html2pdf.bundle.min.js", "icons/icon-192.png", "icons/icon-512.png"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(SHELL).then(c => c.addAll(FILES)).then(() => self.skipWaiting()));
});
self.addEventListener("activate", e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k.startsWith("drx-") && k !== SHELL && k !== "drx-runtime" && !k.startsWith("drx-ocr")).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});

function idbGet(id) {
  return new Promise((res, rej) => {
    const r = indexedDB.open("dermrx", 1);
    r.onupgradeneeded = () => { const d = r.result; if (!d.objectStoreNames.contains("docs")) d.createObjectStore("docs"); if (!d.objectStoreNames.contains("blobs")) d.createObjectStore("blobs"); };
    r.onsuccess = () => { const t = r.result.transaction("blobs", "readonly").objectStore("blobs").get(id); t.onsuccess = () => res(t.result); t.onerror = () => rej(t.error); };
    r.onerror = () => rej(r.error);
  });
}

self.addEventListener("fetch", e => {
  const url = new URL(e.request.url);
  if (e.request.method !== "GET") return;
  // Never touch file downloads (the app installer, backups, review pages): let the browser fetch them directly.
  if (/\.(apk|aab|zip|pdf)$/i.test(url.pathname) || url.pathname.includes("/review/")) return;
  const bi = url.pathname.indexOf("/_blob/");
  if (url.origin === location.origin && bi >= 0) {
    const id = decodeURIComponent(url.pathname.slice(bi + 7));
    e.respondWith(idbGet(id).then(v => v ? new Response(v.blob, { headers: { "Content-Type": v.type || "application/octet-stream", "Cache-Control": "no-store" } }) : new Response("", { status: 404 })).catch(() => new Response("", { status: 404 })));
    return;
  }
  if (url.origin !== location.origin) {
    // Fonts and other CDN files: cache as we go so the app keeps its look offline.
    if (/fonts\.(googleapis|gstatic)\.com|cdnjs\.cloudflare\.com|cdn\.jsdelivr\.net|upload\.wikimedia\.org/.test(url.host)) {
      e.respondWith(caches.open("drx-runtime").then(async c => { const hit = await c.match(e.request); const net = fetch(e.request).then(r => { if (r.ok || r.type === "opaque") c.put(e.request, r.clone()); return r; }).catch(() => hit); return hit || net; }));
    }
    return; // Firestore / auth traffic goes straight to the network.
  }
  if (url.pathname.includes("/vendor/tesseract/")) {
    // Prescription reader: downloaded once, kept across app updates, then works offline.
    e.respondWith(caches.open("drx-ocr-7").then(async c => { const hit = await c.match(e.request, { ignoreSearch: true }); return hit || fetch(e.request).then(r => { if (r.ok) c.put(e.request, r.clone()); return r; }); }));
    return;
  }
  const fresh = e.request.mode === "navigate" || /(\/|index\.html|seed\.json|prices\.json|config\.js|drx-shim\.js|manifest\.webmanifest)$/.test(url.pathname);
  if (fresh) {
    // Network first: whenever the phone is online it gets the newest app.
    e.respondWith(fetch(e.request, { cache: "no-cache" }).then(r => { if (r.ok) { const cp = r.clone(); caches.open(SHELL).then(c => c.put(e.request, cp)); } return r; })
      .catch(() => caches.match(e.request, { ignoreSearch: true }).then(r => r || caches.match("index.html"))));
  } else {
    e.respondWith(caches.match(e.request).then(r => r || fetch(e.request).then(res => { if (res.ok) { const cp = res.clone(); caches.open(SHELL).then(c => c.put(e.request, cp)); } return res; })));
  }
});
