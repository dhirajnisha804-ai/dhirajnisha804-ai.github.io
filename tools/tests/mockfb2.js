window.firebase=(function(){
 const DEL={__del:1};
 const raw=localStorage.getItem('__mockstore'); const init=raw?JSON.parse(raw):{brands:{"p-dabur-femcinol-adp":{product:"Femcinol-ADP gel",brand:"Dabur",category:"Anti-acne (topical)",composition:"Adapalene + Clindamycin",price:175,pack:"15 g",mrName:"Shubham Dubey",mrPhone:"9118079126",updatedAt:1},"p-x":{product:"Xcream",brand:"Y",category:"Other",composition:"z",price:100,pack:"10 g",updatedAt:1}},templates:{"t1":{name:"T1",rx:[]}}};
 const store={}; for(const c in init){store[c]=new Map(Object.entries(init[c]));}
 const persistStore=()=>{const o={};for(const c in store)o[c]=Object.fromEntries(store[c]);localStorage.setItem('__mockstore',JSON.stringify(o));};
 const subs={}; let user=JSON.parse(localStorage.getItem('__mockuser')||'null'); const authSubs=[];
 const col=c=>(store[c]||=new Map());
 const snap=c=>({empty:!col(c).size,size:col(c).size,metadata:{fromCache:false},docs:[...col(c)].map(([id,d])=>({id,exists:true,data:()=>JSON.parse(JSON.stringify(d))})),forEach(f){this.docs.forEach(f)}});
 const emit=c=>{persistStore();(subs[c]||[]).forEach(f=>f(snap(c)));};
 const canWrite=()=>{ if(!user||user.email!=='dhirajnisha804@gmail.com'){const e=new Error('denied');e.code='permission-denied';throw e;} };
 const applyUpd=(o,d)=>{const r={...o};for(const k in d){if(d[k]&&d[k].__del)delete r[k];else r[k]=d[k];}return r;};
 const docRef=(c,id)=>({id:id||Math.random().toString(36).slice(2),async set(d){canWrite();col(c).set(this.id,d);emit(c)},async update(d){canWrite();col(c).set(this.id,applyUpd(col(c).get(this.id)||{},d));emit(c)},async delete(){canWrite();col(c).delete(this.id);emit(c)},async get(){const d=col(c).get(this.id);return{exists:!!d,data:()=>d}},onSnapshot(cb){cb({id:this.id,exists:col(c).has(this.id),data:()=>col(c).get(this.id)});return()=>{}}});
 const fsObj={enablePersistence:()=>Promise.resolve(),collection:c=>({doc:id=>docRef(c,id),onSnapshot(o,cb){(subs[c]||=[]).push(cb);setTimeout(()=>cb(snap(c)),30);return()=>{}},async get(){return snap(c)}}),
   batch(){const ops=[];return{set(r,d){ops.push(['s',r,d])},update(r,d){ops.push(['u',r,d])},async commit(){canWrite();for(const[t,r,d] of ops) await (t==='s'?r.set(d):r.update(d))}}}};
 const fire=()=>fsObj; fire.FieldValue={delete:()=>DEL};
 window.__store=store;
 return {initializeApp(){},firestore:fire,auth:()=>({onAuthStateChanged(f){authSubs.push(f);setTimeout(()=>f(user),10)},async signInWithEmailAndPassword(e,p){if(p!=='pw'){const er=new Error();er.code='auth/invalid-credential';throw er}user={email:e};localStorage.setItem('__mockuser',JSON.stringify(user));authSubs.forEach(f=>f(user))},async signOut(){user=null;localStorage.removeItem('__mockuser');authSubs.forEach(f=>f(null))}})};
})();
