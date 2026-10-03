function openSync(){
  const D=window.DRX||{}; const st=D.status||{};
  const line=(label,col)=>{ const s=st[col]; const n=col==="brands"?S.brands.length:S.templates.length; const src=!s?"loading…":s.source==="cloud"?"up to date with the shared list":s.source==="cache"?"saved copy (offline) — updates when online":"built-in list (not yet synced)"; return `<div class="row" style="cursor:default"><span class="main"><span class="t">${label}: ${n}</span><span class="s">${esc(src)}</span></span></div>`; };
  const admin = D.isAdmin;
  const authHTML = !D.configured
    ? `<p class="hint" style="margin:0">Cloud sync isn’t connected in this build, so the built-in list is shown.</p>`
    : admin
      ? `<p class="hint" style="margin:0">Signed in as <b>${esc(D.user?.email||"")}</b> (list owner). Medicines and templates you add or edit here reach everyone the next time they open the app online.</p>
         <div class="actions"><button class="btn" id="syPub">Publish built-in list to everyone</button><button class="btn" id="syOut">Sign out</button></div>
         <p class="hint" id="syMsg" style="margin:0"></p>`
      : `<p class="hint" style="margin:0">Only the list owner signs in here, to edit the shared medicines and templates. Everyone else can use the app without signing in.</p>
         <div class="grid"><div class="field" style="grid-column:1/-1"><label for="syEm">Email</label><input id="syEm" type="email" autocomplete="username" value="${esc(D.user?.email||"")}"></div>
         <div class="field" style="grid-column:1/-1"><label for="syPw">Password</label><input id="syPw" type="password" autocomplete="current-password"></div></div>
         <div class="actions"><button class="btn primary" id="syIn">Sign in as owner</button>${D.user?`<button class="btn" id="syOut">Sign out</button>`:""}</div>
         <p class="hint" id="syMsg" style="margin:0">${D.user&&!admin?`Signed in as ${esc(D.user.email)}, which isn’t the owner account.`:""}</p>`;
  openSheet("Sync & sharing", `<div class="stack">
    <div class="group"><h3>Shared with everyone</h3><div class="list">${line("Medicines","brands")}${line("Rx templates","templates")}</div></div>
    <p class="hint" style="margin:0">The app design and these two lists update by themselves whenever the phone is online.</p>
    <div class="group"><h3>Owner</h3><div class="section stack">${authHTML}</div></div>
    <div class="group"><h3>Kept only on this phone</h3><div class="section stack">
      <p class="hint" style="margin:0">Patients, clinical photos, scores, drug-safety edits and your doctor profile never leave this phone. Use <b>Backup</b> regularly.</p>
      <div class="actions"><label class="btn filebtn"><input type="file" id="syRestore" accept=".json,application/json">Restore a backup file</label><button class="btn" id="syReload">Check for app update</button></div>
      <p class="hint" id="syRMsg" style="margin:0"></p></div></div>
  </div>`);
  const msg=t=>{ const el=$("#syMsg"); if(el) el.textContent=t; };
  $("#syIn")?.addEventListener("click", async()=>{ const em=$("#syEm").value, pw=$("#syPw").value; if(!em||!pw){ msg("Enter email and password."); return; } msg("Signing in…"); try{ await D.signIn(em,pw); setTimeout(openSync,300); }catch(e){ msg(e?.code==="auth/invalid-credential"||e?.code==="auth/wrong-password"||e?.code==="auth/user-not-found"?"Email or password is wrong.":e?.code==="auth/network-request-failed"?"No internet. Try again when online.":"Couldn’t sign in. Try again."); } });
  $("#syOut")?.addEventListener("click", async()=>{ await D.signOut(); setTimeout(openSync,200); });
  $("#syPub")?.addEventListener("click", async e=>{ const b=e.currentTarget; b.disabled=true; msg("Publishing…"); try{ const n=await D.publishSeed("missing",(d,t)=>msg(`Publishing… ${d} of ${t}`)); msg(`Done. ${n} items checked; anything missing was added to the shared list.`); }catch(er){ msg(er?.code==="admin_only"?er.message:"Couldn’t publish. Check your connection."); } b.disabled=false; });
  $("#syReload").addEventListener("click", ()=>location.reload());
  $("#syRestore").addEventListener("change", async e=>{ const f=e.target.files[0]; e.target.value=""; if(!f) return; const el=$("#syRMsg"); try{ const data=JSON.parse(await f.text()); const n=await D.restoreLocal(data); el.textContent=`Restored ${n} records to this phone. Photos aren’t part of backup files.`; }catch{ el.textContent="That file couldn’t be read. Choose a DermRx backup (.json)."; } });
  D.statusHook=()=>{};
}
