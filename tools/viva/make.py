"""tools/viva/v*.py -> Resident Corner posts (section "Viva") in tools/dbb4/posts/viva-*.json (drafts).
Each post is linked to a case in the Cases list by caseName (must match the case title exactly)."""
import glob, json, os, re, runpy, time
HERE = os.path.dirname(os.path.abspath(__file__))
POSTS = os.path.join(HERE, "..", "dbb4", "posts")
APP = os.path.join(HERE, "..", "app.html")
now = int(time.time() * 1000)

cases = json.loads(re.search(r'<script type="application/json" id="casesData">(.*?)</script>', open(APP, encoding="utf-8").read(), re.S).group(1))
idx = {c["n"]: (i, c["g"]) for i, c in enumerate(cases)}
grank = {}
for c in cases: grank.setdefault(c["g"], len(grank))
def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]

for old in glob.glob(os.path.join(POSTS, "viva-*.json")): os.remove(old)
n = 0
for f in sorted(glob.glob(os.path.join(HERE, "v[0-9]*.py"))):
    for d in runpy.run_path(f)["D"]:
        name = d["case"]; assert name in idx, "unknown case: " + name
        i, g = idx[name]
        body = f"_Viva questions for the case: **{name}** ({g})_\n\n"
        for k, (q, ans) in enumerate(d["qa"], 1):
            body += f"**Q{k}. {q}**\n" + "\n".join(f"- {a}" for a in ans) + "\n\n"
        if d.get("spot"): body += "## Quick spotter facts\n" + "\n".join(f"- {x}" for x in d["spot"]) + "\n\n"
        if d.get("note"): body += f"## Note\n{d['note']}\n\n"
        body += f"_Sources: {d['src']}. Answers written in our own words; check with your teachers' preferences._"
        doc = {"section": "Viva", "title": f"{name} — viva", "caseName": name, "summary": f"{g} · {len(d['qa'])} viva questions with answers",
               "icon": "🎓", "category": g, "order": grank[g] * 1000 + i, "body": body.strip(),
               "draft": True, "banner": False, "createdAt": now - i, "updatedAt": now}
        json.dump({"data": doc}, open(os.path.join(POSTS, f"viva-{slug(name)}.json"), "w"), ensure_ascii=False, indent=1)
        n += 1
print("viva posts:", n)
