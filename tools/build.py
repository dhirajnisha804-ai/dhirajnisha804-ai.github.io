#!/usr/bin/env python3
"""Assemble the standalone DermRx Desk site (www/) from the artifact source app.html."""
import json, os, glob, shutil, time, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.dirname(HERE)
OUT = os.path.join(HERE, "www")
SRC_APP = sys.argv[1] if len(sys.argv) > 1 else os.path.join(SP, "app.html")
DB = os.path.join(SP, "dbb4")

shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT + "/vendor"); os.makedirs(OUT + "/icons")

s = open(SRC_APP, encoding="utf-8").read()
def rep(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, (old[:80], n)
    s = s.replace(old, new)

BUILD = time.strftime("%Y%m%d%H%M")
head = f"""<link rel="manifest" href="manifest.webmanifest"><meta name="theme-color" content="#2f6b5a">
<link rel="icon" href="icons/icon-192.png"><link rel="apple-touch-icon" href="icons/icon-192.png">
<meta name="drx-build" content="{BUILD}">
<script src="config.js"></script>
<script src="vendor/firebase-app-compat.js"></script><script src="vendor/firebase-auth-compat.js"></script><script src="vendor/firebase-firestore-compat.js"></script>
<script src="drx-shim.js"></script>
</head>"""
rep("</style></head><body>", "</style>" + head + "<body>")

# PDF library: bundled copy first (works offline), CDN as backup
rep('pdfLib = tryLoad("https://cdnjs.cloudflare.com', 'pdfLib = tryLoad("vendor/html2pdf.bundle.min.js").catch(()=>tryLoad("https://cdnjs.cloudflare.com')
rep('.catch(()=>tryLoad("https://cdn.jsdelivr.net/npm/html2pdf.js@0.10.1/dist/html2pdf.bundle.min.js"));',
    '.catch(()=>tryLoad("https://cdn.jsdelivr.net/npm/html2pdf.js@0.10.1/dist/html2pdf.bundle.min.js")));')

# Friendly message when a non-owner tries to change the shared lists
ADM = 'if(e&&e.code==="admin_only"){ toast(e.message); return false; } '
rep('  catch(e){ toast(e && e.code==="quota_exceeded"', '  catch(e){ ' + ADM + 'toast(e && e.code==="quota_exceeded"')
rep('async function patch(col, id, data){ try{ await S.db.collection(col).doc(id).update(data); return true; } catch{ toast(',
    'async function patch(col, id, data){ try{ await S.db.collection(col).doc(id).update(data); return true; } catch(e){ ' + ADM + 'toast(')
rep('async function remove(col, id){ try{ await S.db.collection(col).doc(id).delete(); return true; } catch{ toast(',
    'async function remove(col, id){ try{ await S.db.collection(col).doc(id).delete(); return true; } catch(e){ ' + ADM + 'toast(')

# "Sync & sharing" entry in More, its handler and panel
rep('  <div class="group"><h3>Data</h3><div class="list">\n',
    '  <div class="group"><h3>Data</h3><div class="list">\n    <button class="row" data-act="sync"><span class="main"><span class="t">Sync &amp; sharing</span><span class="s">${window.DRX?.isAdmin?"Signed in as list owner":"Shared medicines and templates update automatically"}</span></span></button>\n')
rep('  else if(a==="backup") exportBackup();', '  else if(a==="backup") exportBackup();\n  else if(a==="sync") openSync();')
rep('function openSignature(){', open(os.path.join(HERE, "src/sync-panel.js"), encoding="utf-8").read() + "function openSignature(){")

open(OUT + "/index.html", "w", encoding="utf-8").write(s)

# runtime files
shutil.copy(HERE + "/src/drx-shim.js", OUT)
open(OUT + "/sw.js", "w").write(open(HERE + "/src/sw.js").read().replace("__BUILD__", BUILD))
cfg = HERE + "/src/config.js"
shutil.copy(cfg if os.path.exists(cfg) else HERE + "/src/config.example.js", OUT + "/config.js")
V = HERE + "/vend"
for f in ["firebase-app-compat.js", "firebase-auth-compat.js", "firebase-firestore-compat.js"]:
    shutil.copy(f"{V}/x_firebase-10.12.2/package/{f}", OUT + "/vendor/")
shutil.copy(f"{V}/x_html2pdf.js-0.10.1/package/dist/html2pdf.bundle.min.js", OUT + "/vendor/")
for f in glob.glob(HERE + "/src/icons/*.png"): shutil.copy(f, OUT + "/icons/")
shutil.copy(HERE + "/src/manifest.webmanifest", OUT)
open(OUT + "/.nojekyll", "w").write("")

# seed: current shared lists
seed = {}
for col in ["brands", "templates"]:
    arr = []
    for f in sorted(glob.glob(f"{DB}/{col}/*.json")):
        d = json.load(open(f, encoding="utf-8")); d = d.get("data", d)
        arr.append({"id": os.path.basename(f)[:-5], **d})
    seed[col] = arr
json.dump(seed, open(OUT + "/seed.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print("built", BUILD, {k: len(v) for k, v in seed.items()})

# Digital asset links: lets the Android app open full-screen (no browser bar)
os.makedirs(OUT + "/.well-known", exist_ok=True)
FP = "37:23:48:67:AD:A0:60:DF:9F:CE:15:FF:84:51:46:68:26:E3:A1:82:54:A3:FA:7F:C2:32:27:10:BC:9E:97:B6"
json.dump([{"relation": ["delegate_permission/common.handle_all_urls"], "target": {"namespace": "android_app", "package_name": "in.dermrx.desk", "sha256_cert_fingerprints": [FP]}}], open(OUT + "/.well-known/assetlinks.json", "w"), indent=1)
