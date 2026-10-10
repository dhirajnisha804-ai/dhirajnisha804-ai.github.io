# Derma Desk — handover & build plan (saved 4 Oct 2026)

Owner: Dr. Nisha Pattewar (dhirajnisha804@gmail.com). Co-admin: her husband (email still to be given).
The owner approved everything below ("done" given). Build it in stages, test, deploy, then report briefly.

## How the project works (read first)
- **Source of truth:** `tools/app.html` (single-file app, also published as the Claude artifact
  https://claude.ai/artifact/GLv7GJV7MV3MphjJehfFHQ). Shared data snapshot: `tools/dbb4/` (brands, templates).
- **Build:** `python3 tools/build.py` → writes `www/` (keeps `www/prices.json` and `www/vendor/`). Push to `main`;
  GitHub Actions deploys Pages and rebuilds the APK only when `android/` changes (release tag `apk-latest`).
- **Runtime:** `tools/src/drx-shim.js` emulates `window.claude.use(db|assets|downloads)`; brands/templates live in
  Firestore (project dermrx-4fa87, owner-only writes), everything else in IndexedDB on the phone.
  Publish button (More → Sync & sharing) adds new templates and refreshes corrected ones (uses `prevUpdatedAt`).
- **Android shell:** `android/` (WebView, applicationId `in.dermrx.desk`, package `com.dermadesk.app`,
  JS bridge `DermaAndroid.saveFile`, back → `window.DRX_back()`). Keystore decrypted in CI with secret DRX_KEYPASS.
- **Artifact:** after changing `tools/app.html`, read the live artifact first and merge (other sessions edit it),
  then publish to the same URL. Its own template DB is separate (ArtifactData collection `templates`).
- **Tests:** `tools/tests/` (Playwright; run from a folder containing the built `www/` and `mockfb2.js`).
- **Rules:** patient data never leaves the phone; Wolverton/IADVL text never copied (facts in own words only);
  no ads inside the app; monthly price task (trigger trig_01HagW6JbLSyApZTDdqQuywT) writes `www/prices.json`.

## Decisions (final)
- Tagline: **"Dermatology Made Easy"** (replaces "Dermatology consultations and prescriptions").
- **Free for every signed-up user:** case formats, patient records, and 5 templates — tinea corporis/cruris,
  scabies, acute urticaria, acne vulgaris (mild to moderate), pityriasis versicolor.
- **Paid (verified dermatologists/residents only):** all other templates, dose by weight, drug safety,
  drug-interaction checker. Price & payment method: **decide later** (show "Verified — subscription coming soon").
- Sign-up: name, date of birth, sex, phone, email, role (resident / practising dermatologist / other),
  state council + registration no., proof upload (residents: college ID or joining letter; practising: MD/DNB/DVD
  degree certificate). **Email verification only** (no phone OTP). Consent tick box (terms + privacy).
- Approvals: owner + husband, from an in-app **Approvals** screen (view proof, approve / reject with reason,
  user gets an email). Delete proof after decision; keep "verified on <date> by <admin>".
- Screenshot block (Android FLAG_SECURE) **only** on Templates, Drug safety, Dose by weight, Interactions.
- Help emails: decide later. Play Store listing: English only. No ads inside the app.
- Testing stays private (owner, husband, a friend, sister) until full-fledged.

## UI decisions (mockups approved)
- Header: Derma Desk + tagline; top-right **+** (new patient) and **⋯** (More — moved from bottom bar).
- Bottom bar: **Cases · Patients · Drugs · Templates · Resident Corner**.
- **Drugs tab** (renamed from Medicines) with top switch, Interactions open by default:
  `Interactions | Brands & prices | Dose by weight | Drug safety`. "Check interactions" button in the patient
  Prescription section; automatic red/amber alerts on the patient page from "current medicines" + Rx.
- **Interaction checker:** dermatology-focused, curated from Wolverton 4e ch 66 (top interactions) + drug chapters
  + labels, own wording; severity contraindicated / serious / monitor / none (red / amber / green), what happens,
  what to do; brand → generic via catalogue; footer "Not a complete check for all medicines".
- **Resident Corner tab:** Articles · Procedures (e.g. peels step by step) · Updates. Owner/husband post (title,
  section, text, optional photo, "Show as banner"); everyone signed-in reads; search + "new" badges. Free.
- **Animations:** (1) screens slide in/out; (2) rotating tips while loading; (3) banner carousel on main tabs
  (auto-slides, dots, from Resident Corner posts marked "Show as banner").
- **Branded loading screen** (navy + icon + tagline, held until the page is ready — Android 12 SplashScreen keep-on)
  and **first-run walkthrough** (4 swipe screens, Skip, "Show tour again" in Help).

## Build stages
1. **Stage 1 (needs one APK reinstall):** splash, walkthrough, tagline, header ⋯, bottom bar, Drugs tab with switch,
   slide animations, loading tips, banner carousel, FLAG_SECURE bridge (`DermaAndroid.secure(true|false)` toggled
   per screen).
2. **Stage 2:** Firebase Auth email/password sign-up + email verification; `users/{uid}` profile; proof upload
   (compressed image in Firestore `verifications/{uid}` to avoid needing the paid Storage plan); admin Approvals;
   roles `free | verified | pro`; Firestore rules so paid templates are readable only by verified/pro (move them to
   a protected collection), free 5 readable by any signed-in user; remove public templates from `seed.json`;
   Resident Corner (`posts` collection, admins write).
3. **Stage 3:** interaction checker data + UI; admin dashboard (sign-ups, pending, verified, usage per campaign);
   usage analytics without patient data; device limit (2); doctor name on printouts.
4. **Stage 4 (after owner decides price/payment):** Google Play Billing subscription with server check
   (needs Firebase Blaze + spending cap), move hosting to Firebase Hosting (GitHub Pages bars commercial use),
   privacy policy + terms + account deletion, Play listing (draft in chat 4 Oct), store screenshots with sample
   data only, AAB build, 12-tester closed test for 14 days, landing page, campaign links, promo & referral codes.

## Needs the owner (ask, don't guess)
- Husband's email for admin access. Price, payment method, help-email wording, Play account holder name.
- Firebase console: confirm Email/Password sign-in is enabled (it is for the owner) — no other console step for stages 1–2.

## Resident Corner — launch content (owner request, 4 Oct)
Write standard SOPs (own words; Wolverton 4e ch 53 peels, ch 23 phototherapy, ch 58 local anaesthetics,
plus IADVL/standard procedural texts — never copy text) as Procedures posts, marked "Draft — owner to review"
until she approves each:
1. Salicylic acid (SA) peel  2. Glycolic acid (GA) peel  3. TCA peel  4. NB-UVB phototherapy  5. Excimer (308 nm)
6. Paring of warts and corns  7. Punch biopsy  8. Milia extraction  9. Molluscum extraction
10. Comedone extraction  11. DPN (dermatosis papulosa nigra) removal — RF/electrocautery  12. Intralesional steroid injection
13. Wood's lamp examination (room prep, findings by condition, documentation)
14. Whole-body phototherapy (cabin NB-UVB ± PUVA: skin typing/MED, starting dose & increments, eye/genital
    protection, missed-dose rules, cumulative dose log, stopping criteria) — #4 covers NB-UVB basics/targeted units
Owner wants the chat summaries of Excimer (#5) and RF vs EC (#15) given on 5 Oct used as the base of those SOPs:
  Excimer — 308 nm targeted; indications (vitiligo face/neck best, acral poor; localised/scalp/palmoplantar psoriasis;
  patchy AA; localised AD/prurigo); CI (photosensitivity disorders, photosensitising drugs, melanoma/NMSC at site);
  goggles; start ~100 (face/neck) / 150–200 (trunk, limbs) / 250–300 (hands, feet) mJ/cm² for vitiligo, MED-based for
  psoriasis; twice weekly non-consecutive; +10–20% until 24–48 h faint erythema; blister → skip, restart 20–25% lower;
  missed → reduce 10–25%; combine tacrolimus/steroid; response 8–12 sessions, assess at 24, up to ~6 months.
15. Radiofrequency (RF) vs electrocautery (EC): principle, modes, indications, pacemaker precautions, electrode
    choice, operating steps, plume safety, aftercare, complications (settings per machine manual)
Each SOP: indications · contraindications · pre-procedure (consent, counselling, priming, test patch) · equipment
· step-by-step · endpoints · post-care · complications & management · follow-up/sessions. Paid content? — default free.

## Extra features approved (4 Oct)
- **Voice typing**: mic button on History, Chief complaints, Diagnosis and instruction fields (Android speech-to-text
  via the WebView / Web Speech API; works with English, Hindi, Marathi). Needs RECORD_AUDIO permission in the APK.
- **Before/after photo comparison**: on a patient, pick two visit photos → side-by-side and slider view with dates;
  when taking a new follow-up photo show a faint "ghost" overlay of the previous photo to match the angle.
  Photos stay on the phone.

## Play Store consents & documents (stage 4)
- Play Console: privacy policy URL, Data safety form, Health apps declaration (clinical tool for HCPs, not a medical
  device), account deletion (in-app + web link), target audience 18+, content rating, "No ads", reviewer test login,
  permissions = camera + microphone only (use Android photo picker, no broad media permission).
- In-app: DPDP notice + unticked "I agree to Terms & Privacy" at sign-up; separate consent for proof documents
  (deleted after verification); one-time medical disclaimer; one-line reason before each permission prompt;
  "Patient consent taken" tick when adding clinical photos + printable photo-consent form (EN/HI/MR).
- Draft for owner review (and a lawyer): privacy policy, terms of use (subscription terms once priced),
  medical disclaimer, photo-consent form.

## Review before launch (owner taking 1–2 weeks to recheck and add ideas)
- Add "Needs review" badge + Review queue for every new/changed template, drug-safety entry and weight-dose entry;
  owner taps ✓ Reviewed; unreviewed items are not published to colleagues.
- Run an independent second check (fresh reviewer agent) of the 42 new templates, 101 drug-safety corrections and
  65 weight-dose entries against Wolverton 4e; give the owner a list of doubtful items first.

## Drug safety additions (owner request, 5 Oct)
- **Upadacitinib — separate entry** (currently only inside the combined "JAK inhibitors" entry). Check against current
  label (AD: 15 mg OD, 30 mg if inadequate response <65 y; ≥65 y 15 mg; adolescents ≥12 y & ≥40 kg 15 mg; strong CYP3A4
  inhibitors → max 15 mg), boxed warnings (serious infection, mortality, malignancy, MACE, thrombosis — esp. ≥65,
  smokers, CV risk), baseline TB/HBV/HCV/CBC/LFT/lipids, lipids at ~12 wk, interrupt if ALC <500, ANC <1000, Hb <8,
  no live vaccines, pregnancy contraindicated (contraception during and 4 wk after), no breastfeeding (during + 6 days).
  Mark "Needs review".

## Small fixes requested 5 Oct (do first after usage reset)
1. **Back button**: Cases → open a topic → back must return to the previous screen (the case list / group),
   not jump all the way out. Check `window.DRX_back()` and in-app back arrows keep a proper history stack
   (same for nested sheets everywhere).
2. Remove the case-format source line `<p class="csrc">Written in original wording for Derma Desk. Based on standard
   references: …</p>` completely.
3. Drug safety page: remove the whole line "Checked against Wolverton 4e (2020), ch N. ⚠ Verify against current
   guidelines before use." (the `dsverify` text) — keep only the Edit button / "Edited by you" pill.


## Status 7 Oct 2026
- DONE Batch A (web): back-nav fix, csrc + Wolverton lines removed, tagline, header ⋯, bottom bar (Cases·Patients·Drugs·Templates·Resident Corner), Drugs tab (Interactions default · Brands · Dose · Safety), interaction checker (292 pairs, /tmp data in app as IX), auto alerts on patient page, Resident Corner (posts collection, 15 SOP drafts, admin editor/approve), banner carousel, slide-in, loading tips, tour, Review queue + "Needs review" badges (templates field `reviewed`; DS/WT in local meta/reviewed), upadacitinib DS entry, photo compare, ghost camera, voice typing (web + bridge).
- DONE Batch B (APK, built 7 Oct): native splash until page ready, DermaAndroid.secure(bool) FLAG_SECURE (templates + Drugs non-brand tabs), DermaAndroid.listen(id, lang) speech → window.DRX_voiceResult, CAMERA permission + WebView getUserMedia grant.
- DONE Batch C (accounts): shim role model (none/unverified/new/pending/rejected/verified/admin), sign-up + email verification + profile + proof (Firestore users/{uid}, verifications/{uid} ≤700 KB JPEG), admin Approvals (approve/reject + mailto), templates query free-only for non-verified (FREE_TPL ids + `free:true`), locks on Drugs tools / dose / safety / interactions, My account (sign out, delete). Rules in tools/firestore.rules — OWNER MUST PUBLISH THEM. Husband's email → add to adminEmails in tools/src/config.js AND to rules isAdmin list.
- KNOWN GAP: repo is public (GitHub Pages) → tools/dbb4 + www/seed.json expose all templates. Fix in stage 4: private repo + Firebase Hosting, strip non-free templates from public seed, publish templates from a private source.
- Tests: tools/tests (mockfb3.js, test_acct.py, test_v2.py, v3_test_b1.py) — run from a folder containing www/ and the mock.

## Treatment ladders (1st / 2nd / 3rd line) — replaces old templates, done in slots
Data: `tools/ladders/slotN.py` (one `L(case, group, general, l1, l2, l3, special)` per disease; rx line = "Drug | dose | freq | dur | route | note").
Build: `python3 tools/ladders/make.py` → `tools/dbb4/templates/l-*.json` (kind:"ladder", review:true, free for acne/scabies/tinea/PV/urticaria), then `python3 tools/build.py`.
UI: Templates tab lists ladders, old templates under "Older templates (being replaced)"; case page "💊 Treatment" button; patient Rx "Use template" opens the ladder to pick a line.
- Slot 1 (8 Oct) DONE: framework + 35 ladders — Acne & appendageal, Bacterial, Fungal, Infestations, Viral, STI. Source: Wolverton 4e + standard practice.
- Slot 2 (8 Oct) DONE: 39 ladders — Eczemas, Papulosquamous, Reactive & drug, Hair & nail, Pigmentary (skipped café-au-lait, DDD, LWNH, nevus depigmentosus, piebaldism, RAPK: no drug ladder). Book text extracted on device to $HOME/w/iadvl_r.txt, flat.txt, rook.txt (VM, may be gone); helper g.py = regex snippets. Was: (treatable ones). Books on her computer (linked folder C:\Users\Rajeshwar\OneDrive\Attachments\DERMATOLOGY BOOKS): "IADVL new edition .pdf" (176 MB), "Rook's Textbook of Dermatology 10E.pdf" (204 MB), "NACO - National Technical Guidelines on STI and RTI_2024.pdf" (recheck STI ladders). Extract text on the device with pdftotext, bring only the treatment sections across.
- Slot 3 (8 Oct) DONE: 43 ladders (117 total). Her decisions applied: Parthenium azathioprine weekly 300 mg only; SJS cyclosporine first line; JAK/ruxolitinib kept as later options; oral minoxidil 2nd line OK. 23 cases skipped (nevi, genodermatoses, simple benign lesions, tattoo). Was: Connective tissue, Vesicobullous, Leprosy & TB, Vascular, Nutritional, Keratinisation, tumours, oral, granulomatous, psychocutaneous, + extra conditions from the 42 newer templates. Skip: genodermatoses/nevi without real drug ladders (note "No standard drug treatment" instead).
- Slot 4 (8 Oct) DONE: 18 extra ladders (135 total), old t-* templates removed from seed; app hides t-* once ladders exist; admin Publish deletes t-* from Firestore; artifact DB has all l-* docs (old t-* left in artifact DB, hidden). Recheck 8 Oct: STI vs NACO 2024 (added cefixime 800 mg alt), tinea capitis vs IADVL (griseofulvin 6–12 wk, itraconazole 5 mg/kg 4–8 wk), propranolol/rituximab/AZA weekly confirmed. Remaining doubts listed to Dr Nisha. Was: cross-check slot 1–3 against IADVL/Rook's, list doubts for Dr Nisha, retire old templates (delete from seed + Firestore), sync artifact DB (ArtifactData templates), publish artifact, admin Publish in app.
- 8 Oct: Pemphigus ladder reordered per Dr Nisha — 1st steroid (+azathioprine), 2nd rituximab/MMF, 3rd DCP/IVIG. Hyperhidrosis ladder ON HOLD (she is studying it): `if False:` in slot4.py, json removed, artifact doc deleted; if it was already published to Firestore, delete l-palmar-plantar-hyperhidrosis there. Leprosy MDT regimen confirmation still pending from her.
- 8 Oct (batch D): header + → universal search (cases, guides, drug safety, guides by drug, brands, patients, SOPs); Download + Send PDF (Web Share / Android share sheet / wa.me fallback); non-admins can no longer edit drug safety, templates, or add/edit products (only MR/notes/★ on own phone; v3_test_b1 step 4 now expectedly fails); More → Account has Log out + Delete account; header line shows "Dr. Name, Qualification" from Doctor profile or sign-up profile (new fields: qualification, clinic address → copied into clinic settings if empty), else tagline; DDx entries link to matching case formats. NOTE tests v3/test_acct serve ./www — copy fresh build into scratch apk/www before running.
- 8 Oct (slot A): privacy.html + terms.html (public, from tools/src/legal, built by build.py; linked in sign-up consent, About); change password (shim changePassword/checkPassword); app lock (PIN SHA-256 in localStorage drx.lock, timeout options, phone fingerprint/screen lock via new Android bridge DermaAndroid.unlock/canUnlock → DRX_unlocked; forgot PIN = account password); About sheet (content build, APK version, update check, outdated-APK prompt via feature detection); SW controllerchange → "updated, reload" banner; offline banner; unsaved-changes guard on consultation (S.guard) + window.DRX_back for Android back button.
- 8 Oct (slot B): patient filters (diagnosis dropdown from visits + visit date: today/7/30/90/365 days/custom range); favourite medicines (meta/favmeds, ★ checkbox in medicine details, top of Add medicine, ✕ remove); "⚑ Report a problem" pre-filled email on treatment guides, case formats, drug safety; FAQ expanded in Help. Dose by weight removed from More (still in Drugs tab). Dropped by Dr Nisha: repeat last Rx, dashboard/follow-ups due/recent patients/quick new patient.
- 8 Oct: Slot C (doctor photo/logo/header colour, procedure record, erase-all, backup reminder) CANCELLED by Dr Nisha — do not build.
- 8 Oct: Brochure PDF (49 pages, 22 companies, 560 unique products) → 426 already in list, 134 added (tools/dbb4/brands, source "Company brochure (Oct 2026)", no MRP except 5). Extracted list: scratchpad ocr/products.json. Generic formulary (249) in tools/src/generics.txt embedded in app.html between /*GENERICS*/ markers — shown in Add medicine ("Generic medicines") and universal search. Artifact DB NOT synced with the 134 new brands (website/APK have them after admin Publish). App lock REMOVED from UI per Dr Nisha (code left, any saved PIN cleared at start); legal pages updated.
- 8 Oct: Scan-a-prescription feature removed from the consultation page (OCR code + vendor/tesseract left unused).
- 8 Oct: Drug interactions moved to Cases page button (data-act ixopen, verified only); Drug safety removed from Cases page (only in Drugs tab + consultation); Drugs tab = Brands & prices | Dose by weight | Drug safety. test_acct updated; test_v2 ix steps now outdated.
- 8 Oct: diagnosis field = type-first suggestions under the box (fuzzy, + 'Use typed'); Treatment button moved to bottom of case format; adding a score on a new patient auto-saves then opens score; History guide button removed from patient page; generics also shown in Drugs → Brands & prices search.
- 8 Oct QA sweep fixes: New visit button for existing patient (vid 'new'); treatment-line drugs are tick-boxes (first ticked); dose by weight filters child/adult by patient age; mobile field + ☆ interesting case on patient page; back button handles photo, tour, coach, score panel; tour Skip doesn't start coach; generic search result opens generic info (brands, guides, drug safety, dose); drug safety search puts name match first & opens it; procedure items excluded from 'guides using this drug'; Use template prefilled from diagnosis; PDF images resolved before service worker; dx filter ignores deleted patients; generic strengths as chips; wording fixes. Not done (by design/declined): follow-up due list; SOP drafts hidden from non-admins until reviewed.
- 8 Oct: Dose guide: 38 adult (fixed-dose) entries added for drugs that only had child entries (itraconazole, terbinafine, fluconazole, griseofulvin, acyclovir, valacyclovir, antibiotics, antihistamines, methotrexate, MMF, dapsone, dupilumab, adalimumab); list filtered/sorted by patient age; IV entries last; no 'practical' rounding for fixed doses. WT_DOSE now 103 entries.
- 8 Oct: Dose guide +34 drugs that had no entry at all (tofacitinib, baricitinib, upadacitinib, abrocitinib, ritlecitinib, apremilast, secukinumab, ustekinumab, pentoxifylline, spironolactone, finasteride, oral minoxidil, tranexamic acid, nicotinamide, deflazacort, methylprednisolone oral, rifampicin, clofazimine, pregabalin, gabapentin, famciclovir, montelukast, doxepin, amitriptyline, glycopyrrolate, metronidazole, secnidazole, benzathine penicillin, ceftriaxone, metformin, vitamin D3, folic acid, fixed adult cyclosporine & HCQ). Total 137.
- 10 Oct: Resident Corner → Instruments: 63 instruments/apparatus (Khopkar 'Drugs & Instruments' App II/III primary; seminar PDF + 2 PPTs secondary), 49 with photos (tools/instruments/img → www/instruments). Source: tools/instruments/instruments.json; generator tools/instruments/make.py → posts ins-*.json (draft). Open doubts in tools/instruments/report.md.
- 10 Oct slot 2: +6 Khopkar App I office aids (69 total, 44 local photos + 5 Wikimedia Commons photos hotlinked with credits for Wood's lamp, dermoscope, cryotherapy unit, patch test kit, prick test kit; B&W scans removed); typo corrections applied (dermatome thickness, iontophoresis principle, iris forceps no lock, monofilament 10 sites).


## Resident Corner → Exam drugs (Oct 2026)
- New section "Exam drugs" (grouped by exam-list heading, sorted by list order). Generator: tools/examdrugs/make.py + slot*.py → posts exd-*.json (drafts).
- Slot 1 done: oral I–V (22). Slot 2 done: oral VI–XI (26). Slot 3 done: injectables (23). Slot 4 done: topicals. Products in neither book removed (user rule). "More from Khopkar" slots 6–9 done (systemic+topical merged). Total 257 drafts awaiting review. Notes: tools/examdrugs/report.md

## Planned: Viva notes for all 140 cases (from Wed 14 Oct)
- See tools/viva/PLAN.md — 6 slots, new Resident Corner "Viva" section + "Viva questions" button on each case page.

## TODO (user, 10 Oct — do later, not now)
- [done 11 Oct] History file: docs/HISTORY.md — keep it updated after each session.

## Play Store launch checklist (10 Oct)
Tech (me): remove DLQI/CDLQI and link to Cardiff's free official DLQI app instead (decided 10 Oct, do Wed); raise targetSdk/compileSdk from 34 to Play's current minimum (35+, check 36); build signed AAB (bundleRelease) not only APK; app-access test account for reviewers; account-deletion web page/URL; final QA.
Her: Play developer account; closed test with 12 testers for 14 days (new personal accounts); store listing (icon 512, feature graphic 1024x500, screenshots, descriptions); Data safety form; content rating; target audience 18+ professionals; health-app declaration; privacy policy URL; lawyer review of privacy/terms; make GitHub repo private; approve drafts.
