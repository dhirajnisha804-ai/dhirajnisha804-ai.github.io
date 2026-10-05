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
