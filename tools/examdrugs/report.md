# Exam drugs (Resident Corner) — build notes

Source lists: Sassoon General Hospital exam lists (oral + injectable, topical) uploaded 10 Oct 2026.
Books: Wolverton, Comprehensive Dermatologic Drug Therapy 4e (main) and Khopkar, Handbook of Dermatological Drug Therapy. Wolverton wins on discrepancies.
Khopkar PDF: pages 8–16, 72–150 and 187–246 have no text layer — OCR'd with tesseract into scratchpad.

## Slot 1 — Oral I–V (22 posts, drafts)
Discrepancies / doubts:
- Acitretin contraception after stopping: some texts 2 y; Wolverton 3 y → 3 y used.
- Doxycycline: Khopkar says no anti-inflammatory effect; Wolverton describes it (sub-antimicrobial dosing) → Wolverton.
- Lymecycline: in neither book — product information used.
- ART (abacavir+3TC, 3TC+AZT, 3TC+NVP+AZT, ritonavir, dolutegravir, nevirapine): Wolverton has little; Khopkar edition predates dolutegravir → NACO/WHO used. Needs checking against latest NACO.
- Ivermectin scabies repeat: Wolverton "1 week to 10 days"; 7–14 days used.

## Slot 2 — Oral VI–XI (26 posts, drafts)
- Cyclosporine creatinine threshold: Wolverton notes 25% (newer) vs 30% (traditional) — both stated.
- Azathioprine dosing by TPMT taken from Wolverton Box 15.4.
- Deflazacort, bilastine: not in Wolverton → Khopkar / product data / urticaria guidelines.
- Montelukast: only brief in books → guidelines + FDA label.
- STI kits: single post with all 7 NACO colour kits (user confirmed single post); not in either book → NACO.

## Decisions for slot 3
- Histoglobulin = Histoglob PFS (human normal immunoglobulin + histamine dihydrochloride, Bharat Serums). User confirmed: induction 6 injections at 4-day intervals, then boosters at 1, 3 and 6 months.

## Slot 3 — Injectables I–IX (23 posts, drafts)
- Lignocaine max dose from Wolverton ch.58 (4.5 mg/kg plain, 7 mg/kg with adrenaline).
- Bleomycin: 1 U/mL for warts; Wolverton 0.2–0.4 mg/mL for vascular anomalies.
- Ceftriaxone gonorrhoea dose differs across guidelines (250 mg / 500 mg / 1 g) — flagged.
- Benzathine penicillin skin testing: Indian practice vs WHO/CDC — flagged.
- Histoglob: user's PFS card dosing; not in books.
- Vitamin D3 60,000 IU is mainly oral in India — oral and IM both covered.
- Menadione (K3) vs phytomenadione (K1) — asked user which examiners mean.
- PPSV23: adult pneumococcal schedule recently changed (PCV20/21) — flagged.

## Slot 4 — Topicals I–XI (60 posts, drafts; files slot4.py = I–V, slot5.py = VI–XI)
- Forms of one drug merged into one post (e.g. clotrimazole cream/solution/powder/paint/soap; clobetasol ointment/lotion/solution).
- Added a "Topical corticosteroids — overview & potency" post (classes, FTU, side effects).
- Triple combination cream (listed under both V and VIII) = one post in VIII.
- Clindamycin gel (listed under II and VII) = one post in II; glycolic acid (VI and VII) = one post in VI.
- Not in either book: eberconazole, ozenoxacin, minocycline topical, decapeptide, TXA+peptides+niacinamide combo, tofacitinib ointment → product data/trials.
- "Melanotx Ultra" brand not confirmed — ingredients covered.
- Minocycline: list says 4% gel; approved form is 4% foam.

## Rule from user (10 Oct): no products that are in neither book
Removed: lymecycline, bilastine, montelukast, eberconazole, TXA+peptides+niacinamide ("Melanotx Ultra"), methotrexate gel.
Kept despite being in neither book because the user asked for them specifically: STI kits (NACO), Histoglob (her dosing card), minocycline 4% foam (renamed from gel/foam).
Sources corrected (found in the books after re-check): ozenoxacin (Wolverton ch.41), tofacitinib 2% ointment (Wolverton ch.18), decapeptide/bFGF (Khopkar topical immunomodulators).
Total exam drug posts: 125.

## "More from Khopkar" (drugs in Khopkar but not on the exam lists) — user: add all, slot-wise; systemic + topical of same drug under one heading
make.py: entries with merge_into are rendered as a "Topical form" section inside the target post (optional title override).
### Slot 6 (done)
- Merged existing pairs: ivermectin, minocycline, methoxsalen, tofacitinib, triamcinolone, hydrocortisone.
- Added: dapsone (+gel), clofazimine, rifampicin, MDT regimens, newer antileprosy drugs, INH, PZA, ethambutol, streptomycin, cutaneous TB regimens (NTEP daily), second-line ATT, NTM regimens.
- Flags: MDT/NLEP regimen updates (3-drug PB); Khopkar DOTS thrice-weekly vs current NTEP daily — current given.
- MDT updated to NLEP revised classification & 3-drug PB/MB regimen effective 1 Apr 2025 (MoHFW DGHS NLEP page; DO letter 6 Mar 2025). TB post: only current NTEP daily regimen (old DOTS note removed).
