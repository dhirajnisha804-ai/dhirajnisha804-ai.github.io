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

for old in glob.glob(os.path.join(POSTS, "exd-*.json")): os.remove(old)  # rebuild from slot files
n = 0
ALL = []
for f in sorted(glob.glob(os.path.join(HERE, "slot*.py"))):
    s = int(re.search(r"slot(\d+)", f).group(1))
    for i, d in enumerate(runpy.run_path(f)["D"]):
        ALL.append((s, i, d))
names = {d["name"]: d for _, _, d in ALL}
# systemic + topical forms of one drug -> one post: entries with merge_into are appended to the target post
for _, _, d in ALL:
    if d.get("merge_into"):
        assert d["merge_into"] in names, "merge target missing: " + d["merge_into"]
        names[d["merge_into"]].setdefault("_merged", []).append(d)

def sub(title, items):
    if isinstance(items, str): items = [items]
    items = [x for x in (items or []) if str(x).strip()]
    return f"**{title}**\n" + "\n".join(f"- {x}" for x in items) + "\n\n" if items else ""

def merged_block(m):
    b = f"## {m.get('form_label') or 'Other form'}: {m['name']}\n_{m['cls']}_\n\n"
    b += sub("Mechanism", m.get("moa")) + sub("Pharmacokinetics", m.get("pk")) + sub("Indications", m.get("uses"))
    b += sub("Dose & how to apply", m.get("dose")) + sub("Adverse effects", m.get("ae")) + sub("Contraindications", m.get("ci"))
    b += sub("Interactions", m.get("ix")) + sub("Monitoring", m.get("mon"))
    if m.get("preg"): b += f"**Pregnancy:** {m['preg']}\n\n"
    b += sub("Viva points", m.get("viva"))
    if m.get("note"): b += f"_Note: {m['note']}_\n\n"
    return b

for s, i, d in ALL:
    if d.get("merge_into"): continue
    title = d.get("title") or d["name"]
    body = f"_{d['group']}_\n\n**Class:** {d['cls']}\n\n"
    body += sec("Mechanism of action", d.get("moa")) + sec("Pharmacokinetics", d.get("pk"))
    body += sec("Indications in dermatology & STI", d.get("uses")) + sec("Dose & formulations", d.get("dose"))
    body += sec("Adverse effects", d.get("ae")) + sec("Contraindications", d.get("ci"))
    body += sec("Drug interactions", d.get("ix")) + sec("Monitoring", d.get("mon"))
    if d.get("preg"): body += f"## Pregnancy & lactation\n{d['preg']}\n\n"
    body += sec("Viva points", d.get("viva"))
    for m in d.get("_merged", []): body += merged_block(m)
    if d.get("note"): body += f"## Note on sources\n{d['note']}\n\n"
    srcs = "; ".join([d["src"]] + [m["src"] for m in d.get("_merged", [])])
    body += f"_Sources: {srcs}. Facts summarised in our own words; Wolverton followed where books differ._"
    doc = {"section": "Exam drugs", "title": title, "summary": f"{d['group'].split(' · ',1)[-1]} · {d['cls']}"[:160],
           "icon": "💊", "category": d["group"], "order": s * 1000 + i, "body": body.strip(),
           "draft": True, "banner": False, "createdAt": now - (s * 1000 + i), "updatedAt": now}
    json.dump({"data": doc}, open(os.path.join(POSTS, f"exd-{slug(d['name'])}.json"), "w"), ensure_ascii=False, indent=1)
    n += 1
print("exam drug posts:", n)
