"""Turn tools/ladders/slot*.py into treatment-ladder templates in tools/dbb4/templates/l-*.json"""
import json, re, glob, os, runpy, time
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "dbb4", "templates")
FREE = {"Acne vulgaris","Scabies","Tinea corporis / cruris / faciei","Pityriasis versicolor","Urticaria & angioedema"}
NAMES = ["First line", "Second line", "Third line"]

def rx(s):
    p = [x.strip() for x in s.split("|")] + [""] * 6
    drug, dose, freq, dur, route, note = p[:6]
    return dict(drug=drug, dose=dose, freq=freq, dur=dur, route=route or ("Topical" if re.search(r"cream|gel|lotion|ointment|shampoo|paint|solution|powder|lacquer", drug, re.I) else ""),
                instr=note, timing="", brand="", brandId="", generic="", cost="")

def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]

n = 0
for f in sorted(glob.glob(os.path.join(HERE, "slot*.py"))):
    for d in runpy.run_path(f)["D"]:
        lines = [dict(line=i + 1, label=NAMES[i], when=l[0], rx=[rx(x) for x in l[1]]) for i, l in enumerate(d["lines"])]
        doc = dict(kind="ladder", name=d["case"], dx=d["case"], caseName=d["case"], group=d["group"],
                   general=d["general"], special=d.get("special", ""), lines=lines,
                   rx=lines[0]["rx"], advice=d["general"], adviceText=d["general"], fuDays="",
                   review=True, free=d["case"] in FREE, source=os.path.basename(f), updatedAt=int(time.time() * 1000))
        json.dump(doc, open(os.path.join(OUT, "l-" + slug(d["case"]) + ".json"), "w"), ensure_ascii=False, indent=1)
        n += 1
print("ladders written:", n)
