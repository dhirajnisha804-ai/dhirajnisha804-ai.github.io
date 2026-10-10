"""tools/examdrugs/slot*.py -> Resident Corner posts (section "Exam drugs") in tools/dbb4/posts/exd-*.json (drafts)"""
import glob, json, os, re, runpy, time
HERE = os.path.dirname(os.path.abspath(__file__))
POSTS = os.path.join(HERE, "..", "dbb4", "posts")
now = int(time.time() * 1000)

def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]
def sec(title, items):
    if isinstance(items, str): items = [items]
    items = [x for x in (items or []) if str(x).strip()]
    return f"## {title}\n" + "\n".join(f"- {x}" for x in items) + "\n\n" if items else ""

n = 0
for f in sorted(glob.glob(os.path.join(HERE, "slot*.py"))):
    s = int(re.search(r"slot(\d+)", f).group(1))
    for i, d in enumerate(runpy.run_path(f)["D"]):
        body = f"_{d['group']}_\n\n**Class:** {d['cls']}\n\n"
        body += sec("Mechanism of action", d.get("moa")) + sec("Pharmacokinetics", d.get("pk"))
        body += sec("Indications in dermatology & STI", d.get("uses")) + sec("Dose & formulations", d.get("dose"))
        body += sec("Adverse effects", d.get("ae")) + sec("Contraindications", d.get("ci"))
        body += sec("Drug interactions", d.get("ix")) + sec("Monitoring", d.get("mon"))
        if d.get("preg"): body += f"## Pregnancy & lactation\n{d['preg']}\n\n"
        body += sec("Viva points", d.get("viva"))
        if d.get("note"): body += f"## Note on sources\n{d['note']}\n\n"
        body += f"_Sources: {d['src']}. Facts summarised in our own words; Wolverton followed where books differ._"
        doc = {"section": "Exam drugs", "title": d["name"], "summary": f"{d['group'].split(' · ',1)[-1]} · {d['cls']}"[:160],
               "icon": "💊", "category": d["group"], "order": s * 1000 + i, "body": body.strip(),
               "draft": True, "banner": False, "createdAt": now - (s * 1000 + i), "updatedAt": now}
        json.dump({"data": doc}, open(os.path.join(POSTS, f"exd-{slug(d['name'])}.json"), "w"), ensure_ascii=False, indent=1)
        n += 1
print("exam drug posts:", n)
