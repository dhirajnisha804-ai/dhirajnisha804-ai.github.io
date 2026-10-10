"""tools/instruments/instruments.json (+ img/*.jpg) -> Resident Corner posts (section "Instruments") and tools/src/instruments/*.jpg"""
import json, os, shutil, time
HERE = os.path.dirname(os.path.abspath(__file__))
POSTS = os.path.join(HERE, "..", "dbb4", "posts")
IMG_OUT = os.path.join(HERE, "..", "src", "instruments")
os.makedirs(IMG_OUT, exist_ok=True)
data = json.load(open(os.path.join(HERE, "instruments.json"), encoding="utf-8"))
now = int(time.time() * 1000)

def sec(title, items):
    items = [x for x in (items or []) if str(x).strip()]
    return f"## {title}\n" + "\n".join(f"- {x}" for x in items) + "\n\n" if items else ""

n = 0
for i, d in enumerate(data):
    slug = d["slug"]; img = ""
    src = os.path.join(HERE, "img", slug + ".jpg")
    if d.get("image") and os.path.exists(src):
        shutil.copy(src, os.path.join(IMG_OUT, slug + ".jpg")); img = f"instruments/{slug}.jpg"
    body = ""
    if img: body += f"![{d['name']}]({img})\n\n"
    if d.get("aka"): body += f"_Also called: {', '.join(d['aka'])}_\n\n"
    if d.get("description"): body += d["description"] + "\n\n"
    body += sec("Parts", d.get("parts")) + sec("Types / variants", d.get("types")) + sec("Uses / indications", d.get("uses"))
    body += sec("Contraindications", d.get("contraindications"))
    if d.get("how_to_hold"): body += f"## How to hold\n{d['how_to_hold']}\n\n"
    if d.get("method"): body += "## Method of use\n" + "\n".join(f"{k+1}. {x}" for k, x in enumerate(d["method"])) + "\n\n"
    if d.get("sterilization"): body += f"## Sterilisation & care\n{d['sterilization']}\n\n"
    body += sec("Viva points & tips", d.get("tips"))
    doc = {"section": "Instruments", "title": d["name"], "summary": f"{d.get('category','')} · " + (d.get("description") or "")[:110],
           "icon": "🔧", "image": img, "category": d.get("category", ""), "body": body.strip(), "draft": True, "banner": False,
           "createdAt": now - i, "updatedAt": now}
    json.dump({"data": doc}, open(os.path.join(POSTS, f"ins-{slug}.json"), "w"), ensure_ascii=False, indent=1)
    n += 1
print("instrument posts:", n)
