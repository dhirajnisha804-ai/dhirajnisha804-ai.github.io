window.firebase=(function(){
 const ADMIN='dhirajnisha804@gmail.com';
 const ls=k=>{try{return JSON.parse(localStorage.getItem(k)||'null')}catch(e){return null}};
 const init=ls('__mockstore')||{brands:{},templates:{},posts:{},users:{},verifications:{}};
 const store={}; for(const c in init) store[c]=new Map(Object.entries(init[c]));
 const accounts=ls('__mockaccounts')||{[ADMIN]:{uid:'u-admin',pw:'pw',verified:true}};
 const save=()=>{const o={};for(const c in store)o[c]=Object.fromEntries(store[c]);localStorage.setItem('__mockstore',JSON.stringify(o));localStorage.setItem('__mockaccounts',JSON.stringify(accounts));};
 const col=c=>(store[c]||=new Map());
 let cur=null; const authSubs=[]; const subs=[];
 const mkUser=email=>{const a=accounts[email];return{email,uid:a.uid,get emailVerified(){return !!accounts[email].verified},async reload(){},async getIdToken(){return 't'},async sendEmailVerification(){},async delete(){delete accounts[email];save();cur=null;authSubs.forEach(f=>f(null))}}};
 const sess=ls('__mockuser'); if(sess&&accounts[sess]) cur=mkUser(sess);
 const deny=()=>{const e=new Error('denied');e.code='permission-denied';throw e};
 const isAdmin=()=>cur&&cur.email===ADMIN;
 const canWrite=(c,id)=>{ if(['brands','templates','posts'].includes(c)) return isAdmin(); if(['users','verifications'].includes(c)) return isAdmin()||(cur&&cur.uid===id); return true; };
 const snapOf=(c,q)=>{ let docs=[...col(c)].filter(([id,d])=>!q||d[q[0]]===q[2]).map(([id,d])=>({id,exists:true,data:()=>JSON.parse(JSON.stringify(d))})); return {docs,size:docs.length,empty:!docs.length,metadata:{fromCache:false},forEach(f){docs.forEach(f)}}; };
 const fireAll=()=>{save();subs.forEach(s=>{try{s()}catch(e){}})};
 const applyUpd=(o,d)=>{const r={...o};for(const k in d){if(d[k]&&d[k].__del)delete r[k];else r[k]=d[k];}return r;};
 const docRef=(c,id)=>{ id=id||Math.random().toString(36).slice(2); return {id,
   async set(d){if(!canWrite(c,id))deny();col(c).set(id,JSON.parse(JSON.stringify(d)));fireAll()},
   async update(d){if(!canWrite(c,id))deny();col(c).set(id,applyUpd(col(c).get(id)||{},d));fireAll()},
   async delete(){if(!canWrite(c,id))deny();col(c).delete(id);fireAll()},
   async get(){const d=col(c).get(id);return{id,exists:!!d,data:()=>d&&JSON.parse(JSON.stringify(d))}},
   onSnapshot(cb,er){const f=()=>{const d=col(c).get(id);cb({id,exists:!!d,data:()=>d&&JSON.parse(JSON.stringify(d))})};subs.push(f);setTimeout(f,10);return()=>{const i=subs.indexOf(f);if(i>=0)subs.splice(i,1)}}};};
 const colRef=(c,q)=>({doc:id=>docRef(c,id),where:(a,op,b)=>colRef(c,[a,op,b]),
   onSnapshot(o,cb,er){ if(typeof o==='function'){er=cb;cb=o;} const f=()=>cb(snapOf(c,q)); subs.push(f); setTimeout(f,20); return()=>{const i=subs.indexOf(f);if(i>=0)subs.splice(i,1)}},
   async get(){return snapOf(c,q)}});
 const fsObj={enablePersistence:()=>Promise.resolve(),collection:c=>colRef(c),
   batch(){const ops=[];return{set(r,d){ops.push(['s',r,d])},update(r,d){ops.push(['u',r,d])},async commit(){for(const[t,r,d] of ops) await (t==='s'?r.set(d):r.update(d))}}}};
 const fire=()=>fsObj; fire.FieldValue={delete:()=>({__del:1})};
 window.__store=store; window.__accounts=accounts; window.__verify=e=>{accounts[e].verified=true;save()};
 const setCur=u=>{cur=u;localStorage.setItem('__mockuser',JSON.stringify(u?u.email:null));authSubs.forEach(f=>f(u))};
 return {initializeApp(){},firestore:fire,auth:()=>({
   get currentUser(){return cur},
   onAuthStateChanged(f){authSubs.push(f);setTimeout(()=>f(cur),10)},
   async signInWithEmailAndPassword(e,p){const a=accounts[e];if(!a||a.pw!==p){const er=new Error();er.code='auth/invalid-credential';throw er}setCur(mkUser(e))},
   async createUserWithEmailAndPassword(e,p){if(accounts[e]){const er=new Error();er.code='auth/email-already-in-use';throw er}accounts[e]={uid:'u-'+Math.random().toString(36).slice(2,8),pw:p,verified:false};save();const u=mkUser(e);setCur(u);return{user:u}},
   async sendPasswordResetEmail(){},
   async signOut(){setCur(null)}})};
})();
