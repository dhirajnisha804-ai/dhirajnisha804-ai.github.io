# Derma Desk — project history & decisions

Owner: **Dr. Nisha Pattewar** (dermatology resident). This file records what we built, every decision she made, and what is pending — so the work can be picked up again even if chat history is lost.
Keep it updated at the end of every working session (newest session at the bottom of "Session log").

---

## 1. What the app is

- **Derma Desk** (earlier name: DermRx Desk) — a dermatology practice + learning app for doctors and residents.
- Website: https://dhirajnisha804-ai.github.io (GitHub Pages). The Android APK is a shell that loads this website.
- Repo: `dhirajnisha804-ai.github.io`, branch `main`. Pushing to main deploys the site automatically (GitHub Actions). The APK rebuilds only when `android/` changes.
- Secondary preview copy as a Claude artifact (not kept in sync): https://claude.ai/artifact/GLv7GJV7MV3MphjJehfFHQ

### How it is built
- Whole UI is one file: `tools/app.html`. Build: `python3 tools/build.py` → writes `www/` (including `seed.json` from `tools/dbb4/{brands,templates,posts}`).
- Firebase project `dermrx-4fa87`: shared collections **brands / templates / posts** (only admins write); rules in `tools/firestore.rules` (she published them in the Firebase console; copy also saved on her laptop as Downloads/firestore-rules.txt).
- Admins: dhirajnisha804@gmail.com, dalal.dhiraj6@gmail.com. Admin publishes new seed content from the app (Publish → `DRX.publishSeed("missing")`).
- Patient data stays on the phone. No ads. Keystore password is a GitHub secret (never share).
- Content generators (edit these, then run them and build):
  - Treatment ladders: `tools/ladders/slot1–4.py` + `make.py`
  - Instruments: `tools/instruments/instruments.json` + `make.py` (photos in `img/`, web photo credits in `web_images.json`)
  - Exam drugs: `tools/examdrugs/slot1–9.py` + `make.py` (supports `merge_into` to put topical + systemic forms of one drug under one heading)
  - Viva: `tools/viva/v*.py` + `make.py`; plan in `tools/viva/PLAN.md`
- Tests: Playwright scripts (tools/tests/…; ad-hoc ones were kept in the session scratchpad). Build reports & plans: `ROADMAP.md`, `tools/instruments/report.md`, `tools/examdrugs/report.md`.

---

## 2. Standing rules she has given (always follow)

1. Do not copy book text; write facts in our own words. **Viva notes: do NOT copy DYP** — frame questions ourselves (DYP only as a style guide).
2. Unreviewed content stays **draft / "Needs review"** until she approves it.
3. Only openly licensed images, with credits; no B&W photos; items without photos stay without photos.
4. Work **slot-wise** (in parts), and ask doubts at the end of each slot.
5. **Exam drugs:** use Khopkar + Wolverton; if they disagree, **Wolverton wins**. Do **not** add products found in neither book (exceptions she approved: STI kits, Histoglob, minocycline foam).
6. If a drug has systemic and topical forms, put them **under one heading**.
7. For national programmes (leprosy, TB, HIV) give **only current/updated** content.
8. Preserve `www/prices.json`. Patient data must never leave the phone.

---

## 3. Features built (main ones)

- Prescriptions with templates; brand & price catalogue (592 brands incl. 134 brochure products, Cetaphil, Venusia, Melbild, Pregalin NT, Placentrex) + 249 generics with strength chips; favourite medicines; Download / Send prescription PDF.
- Patients with visits, filters (diagnosis/date), unsaved-changes guard, back handling.
- **Cases**: 140 case formats (history to ask, examination, investigations, clickable differentials, how to present, viva pearls), treatment button at the bottom, and a **📝 Viva questions** button that opens the case's viva post.
- **Treatment ladders** (1st/2nd/3rd line) for 134 diseases — view-only in Cases and Templates; ticking medicines only inside a patient via "Use template".
- Scores incl. DLQI/CDLQI item-by-item (**to be removed** — see pending); scores auto-save on a new patient.
- Drug interactions (on Cases page), Drug safety (A–Z, 26 entries, name-match first), Dose by weight (137 entries, age-filtered, adult doses added), all under the Drugs tab.
- Universal search (header 🔍), personalised header ("Dr. Name, Qual"), app tour, About & update banner, offline banner, FAQ, report-a-problem, privacy & terms pages, logout / delete account / change password in More.
- **Resident Corner** sections: Articles, Procedures, **Instruments** (69 items, Khopkar guide), **Exam drugs**, **Viva**, Updates — grouped lists, drafts visible only to admins, ✓ Approve button.
- Removed on her request: app lock/PIN, scan-prescription, dose by weight in More, history guide button, "Slot C" ideas.

---

## 4. Her clinical decisions (treatment ladders etc.)

- Parthenium dermatitis: azathioprine **weekly 300 mg** only.
- SJS/TEN: **cyclosporine first line**.
- JAK inhibitors / ruxolitinib: later options.
- Oral minoxidil: 2nd line.
- Pemphigus: 1st line steroid + azathioprine; 2nd rituximab / MMF; 3rd DCP / IVIG.
- **Hyperhidrosis ladder: ON HOLD** (`if False:` in `tools/ladders/slot4.py`) until she studies it.
- The 23 cases without drug treatment were **not** added as ladders.
- Instruments: Khopkar ("DYP") is the main guide; she approved adding office aids, keeping 8 seminar-only items, the merges, "Khopkar wins", typo corrections.
- Histoglob schedule: 6 injections at 4-day intervals, then boosters at 1, 3 and 6 months.
- STI kits: one post with all 7 NACO colour kits.
- Leprosy MDT: follow **NLEP revised regimen from 1 April 2025** (3 drugs for PB 6 months and MB 12 months; any nerve involvement = MB).
- TB: current **NTEP daily regimen** only (2HRZE + 4HRE).
- **DLQI/CDLQI: remove from the app** (Cardiff copyright — app use needs written consent) and link to Cardiff's free official DLQI app instead (decided 10 Oct).

---

## 5. Content status (as of 11 Oct 2026)

| Content | Count | Status |
|---|---|---|
| Treatment ladders | 134 | live, marked "needs review" |
| Instruments | 69 | drafts |
| Exam drugs | 257 (125 exam list + 132 "More from Khopkar") | drafts |
| Viva posts | 47 cases (V1 infections, V2 STI/eczemas/drug eruptions) | drafts — too thin, to be redone deeper |

---

## 6. Pending work

### Me (reminders set)
- **Sun 11 Oct 10:00 IST** — hyperhidrosis ladder (she is studying it).
- **Wed 14 Oct 10:00 IST** (scheduled reminder in this chat):
  1. Viva notes in DEEPER format: long cases 30–40 Qs, short 15–25, small ≥10; slots of 10–12 cases; redo the 47 first (R1–R4), then the remaining 93. Sources: previous-year question book (Sahana P Raju, *Solved Papers – Dermatology for PG Students*, on her laptop: DERMATOLOGY BOOKS/Dermatology Questions Book.pdf; text at ~/iadvl/pyq.txt via device shell), IADVL 5e (DERMATOLOGY BOOKS/IADVL new edition .pdf; text at ~/iadvl/iadvl.txt), DYP only as style guide. Own words. She must open the chat on her laptop.
  2. Remove DLQI/CDLQI; add link to official DLQI app.
  3. Play Store technical prep: raise targetSdk/compileSdk from 34 to Play's current minimum; build signed **AAB**; reviewer test login; account-deletion web page; final QA.
  4. Check exam-drugs slot 7 HIV PEP/PPTCT regimens against latest NACO.

### Open questions for her
- Vitamin K: menadione (K3) or phytomenadione (K1) for exams?
- Ceftriaxone dose for gonorrhoea (250 mg / 500 mg / 1 g) — department preference?
- Confirm newer facts not in the books: cantharidin approval for molluscum (2023), lindane withdrawal in India, becaplermin boxed warning removal, denileukin re-approval (2024), ranitidine withdrawal.

### Her actions in the app
- Close/reopen app → **Publish** (instruments, exam drugs, viva reach Firestore).
- Review and ✓ Approve drafts; review the 134 ladders.
- If she published before the merges: delete leftover separate topical posts (ivermectin cream, minocycline foam, methoxsalen topical, tofacitinib ointment, triamcinolone topical, hydrocortisone topical, etc.).

### Play Store launch (her side)
- Google Play developer account (US$25, ID verification).
- Closed test: **12 testers for 14 days** (new personal accounts).
- Store listing: icon 512×512, feature graphic 1024×500, ≥2 screenshots, short & full description.
- Play Console forms: Data safety, content rating, target audience (adult professionals), health-app declaration, privacy policy URL.
- Lawyer review of privacy & terms; make GitHub repo private.
- Realistic timeline given 11 Oct: closed test after Wed 14 Oct; public launch ~early November.

---

## 7. Session log

- **3 Oct 2026** — App created (DermRx Desk), Android shell + build workflow, templates, case formats, splash screen.
- **3–9 Oct** — Many features (see section 3): ladders, DLQI/CDLQI, drug safety, tour, universal search, PDF, admin-only edits, account options, personalised header, legal pages, about/update/offline banners, filters, favourites, FAQ; brochure products & generics; dose guide expansion; QA fixes; Firestore rules.
- **10 Oct** — Instruments (69). Exam drugs from Sassoon exam lists (slots 1–4) then "More from Khopkar" (slots 6–9); products in neither book removed; systemic+topical merged; NLEP 2025 MDT; NTEP TB. Viva section + case-page button; viva slots V1–V2 (47 cases). Decisions: deeper viva format, no copying DYP, use previous-year question book; remove DLQI; Play Store checklist.
- **11 Oct** — This history file created on her request.
