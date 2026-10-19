# Viva notes for all 140 cases — plan (start Wednesday 14 Oct 2026)

Sources: DYP Survival Guide for PG Dermatology Examination (main, Q&A style; text in scratchpad ins/dyp.txt and uploaded PDF) + IADVL Textbook (on her laptop: DERMATOLOGY BOOKS / new iadvl — needs computer linked or upload). Rook's only if both are silent. Own words; drafts until she approves.

Where: new Resident Corner section "Viva" (one post per case, grouped like the Cases list). Each case page in Cases gets a "📝 Viva questions" button that opens its viva post (admins see drafts; others only approved posts).

Each post: likely viva questions with short model answers —
definition & synonyms · epidemiology · aetiopathogenesis · classification/variants · key clinical signs & named signs · differential diagnosis (with distinguishing points) · investigations incl. histopathology & dermoscopy · treatment (link to Derma Desk ladder) · complications/prognosis · recent advances · spotter/photo questions · "examiner's favourites".

Slots
- [done 10 Oct] Slot V1 (app wiring + 24): add "Viva" section, case↔post link, button on case page; Infections — bacterial (7), leprosy & cutaneous TB (2), viral (5), fungal (8), infestations (2)
- [done 10 Oct] Slot V2 (23): STI (5), eczemas (11), reactive & drug eruptions (7)
- Slot V3 (24): papulosquamous & erythroderma (7), vesicobullous (1), connective tissue (8), vascular & ulcers (6), granulomatous (1), psychocutaneous (1)
- Slot V4 (22): pigmentary (14), acne & appendageal (8)
- Slot V5 (24): hair & nail (7), oral (1), nutritional & metabolic (4), disorders of keratinisation (7), premalignant & malignant (3), + 2 from nevi (acquired melanocytic nevus, congenital melanocytic nevus)
- Slot V6 (23): remaining nevi & hamartomas (7), genodermatoses (8), benign tumours & cysts (8); final QA, build, publish note

Rules: Wolverton-style rule here = DYP first, IADVL second; if they disagree, ask her (decide at slot end). Ask doubts at end of each slot.
- Next session: start at Slot V3. IADVL text is extracted on her laptop at ~/iadvl/iadvl.txt (device shell); DYP Q&A text in container scratchpad viva/dyp_raw.txt (re-create with pdftotext from the uploaded DYP PDF if lost).

## REVISED (10 Oct, user): content too thin — deeper format from Wednesday 14 Oct
- Depth: long cases 30–40 Qs; short cases 15–25; tiny cases ≥10. Fuller answers (classifications, distinguishing tables, histopathology, scores, regimens, recent advances).
- Cover every question DYP asks for that case (full chapter text via tools: scratchpad viva/ch.py, qs.py) + extra IADVL viva points (IADVL text on her laptop ~/iadvl/iadvl.txt via device shell).
- Slots of 10–12 cases (~12 slots total).
- Order: first REDO V1+V2 (47 cases) in deep format (slots R1–R4), then remaining 93 cases (slots D1–D8) in this order: papulosquamous & erythroderma, vesicobullous, CTD, vascular & ulcers, granulomatous, psychocutaneous, pigmentary, acne & appendageal, hair & nail, oral, nutritional & metabolic, keratinisation, premalignant & malignant, nevi & hamartomas, genodermatoses, benign tumours & cysts.

## RULE (10 Oct, user): do NOT copy DYP
- DYP is only one reference for which topics get asked. Frame questions ourselves; answers fully in our own words — nobody should be able to say the content is copied from DYP.
- Also use the previous-year question book on her laptop: "Dermatology Questions Book.pdf" = Sahana P Raju, Solved Papers Dermatology for PG Students (Jaypee) — text extracted to ~/iadvl/pyq.txt (device shell). Use it to find which questions are actually asked in exams.
- Combine: PYQ book (what is asked) + IADVL (facts) + DYP (examiner style) + own knowledge. Take time; quality over speed.
- No source's sentences or question lists reproduced verbatim; sources line on each post names all references.

## Progress of deep redo
- [done 19 Oct] Slot R1 (12 cases, files r1a.py + r1b.py): impetigo, folliculitis, furuncle/carbuncle, ecthyma, erysipelas/cellulitis, pitted keratolysis, erythrasma, leprosy (37 Qs), cutaneous TB (28 Qs), herpes simplex, molluscum, chickenpox. Topics chosen from the PYQ book question lists (leprosy chapter Q1–Q69, pyoderma, viral chapters); facts checked with IADVL ch.16 etc. make.py: r*.py replaces the same case from v*.py.
- [done 19 Oct] Slot R2 (12 cases, r2a.py + r2b.py): warts, herpes zoster, mycetoma, sporotrichosis, chromoblastomycosis, tinea corporis/cruris/faciei, tinea capitis, tinea pedis & onychomycosis, pityriasis versicolor, candidiasis, pediculosis, scabies.
- [done 19 Oct] Slots R3 (r3a STI 5, r3b eczemas 6) and R4 (r4a eczemas 5, r4b drug/reactive 7) — all 47 V1+V2 cases now deep.
- [done 19 Oct] D1 (8 cases: erythroderma, psoriasis, LP, lichen striatus, parapsoriasis, PR, PRP, vesicobullous) — d1a.py, d1b.py; make.py globs d*.py.
- [done 19 Oct] D2 (11 cases: DM, SLE, SSc, DLE, LSA, morphoea, Parry–Romberg, striae, GA, dermatitis artefacta, RAS) — d2a.py, d2b.py.
- [done 19 Oct] D3 (10 cases: vascular & ulcers 6, nutritional & metabolic 4) — d3a.py, d3b.py.
- Next: D4 pigmentary (14), D5 acne & appendageal (8) + hair & nail (7), D6 keratinisation (7) + premalignant/malignant (3), D7 nevi (9) + genodermatoses (8), D8 benign tumours (8).
- [done 19 Oct] D4 pigmentary (14, d4a/d4b), D5 acne & appendageal + hair & nail (15, d5a/d5b), D6 keratinisation + AK/BCC/SCC (10, d6a/d6b), D7 nevi + genodermatoses (17, d7a/d7b), D8 benign tumours (8, d8.py).
- ALL 140 CASES NOW HAVE DEEP VIVA POSTS (drafts). Laptop link dropped during D6; D6–D8 topics came from PYQ question lists already pulled earlier that session (genodermatoses, ichthyoses/PPK, tumours, naevi chapters).
- [19 Oct] e1.py: extra questions for 14 small cases (5 → 9 each); make.py appends e*.py questions to existing cases.
- [19 Oct] e2.py: extra questions for 39 more cases that had 6–7 Qs (now ≥9 each).
- [19 Oct] e3.py: extra questions for the 18 cases still at 8 (rosacea, HS, NF1 got 4–5 more). Every viva post now has ≥9 questions (54 posts have exactly 9).
- Next (only if she asks): review pass, her corrections, approve/publish.
- [19 Oct, her request 'information too less'] Long-case expansion (e4–e8): 25 long cases brought to ~25–37 Qs each — L1 psoriasis, pemphigus/pemphigoid, vitiligo, SLE, cutaneous TB; L2 SSc, DM, erythroderma, LP, AD, contact; L3 SJS/TEN, urticaria, ichthyosis, NF1, TSC; L4 alopecia areata, acne, AGA, BCC, SCC; L5 leg ulcers, HS, XP. Answers are viva-length bullets (her choice).
- Next: short cases to 15–25 Qs (her chosen order: long first, then short), slot by slot with e9+.
- [19 Oct] Short-case expansion (e9–e17, slots S1–S9): every one of the 140 viva posts now has ≥15 questions (total 2520). Shared generic questions (keratinisation, Wood's lamp, sunscreens, topical steroid potency, nail anatomy, alopecia classification, antifungals, ADR classification, cryotherapy, electrosurgery, melanoma staging, genodermatosis classification) are reused across related cases.
