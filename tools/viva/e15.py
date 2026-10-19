# Short-case expansion S7 (target ≥15 Qs): eczemas (9 small cases).
# Own words; viva-length bullets. Facts from IADVL 5e and standard references.
ECZ = ("Describe the histopathology of eczema by stage (PYQ).", ["Acute: marked spongiosis with intraepidermal vesicles, papillary oedema, perivascular lymphocytes ± eosinophils", "Subacute: spongiosis + parakeratosis + acanthosis, crusts", "Chronic: compact hyperkeratosis, irregular/ psoriasiform acanthosis, hypergranulosis, minimal spongiosis, vertical collagen in papillae (lichenification)"])
TSA = ("Classify topical corticosteroids by potency (WHO/ British).", ["Super-potent (class I): clobetasol propionate 0.05%, halobetasol, betamethasone dipropionate in optimised vehicle", "Potent: betamethasone dipropionate/ valerate 0.1%, mometasone furoate 0.1%, fluticasone 0.05%, fluocinolone 0.025%, halcinonide", "Moderate: clobetasone butyrate 0.05%, triamcinolone 0.1%, desonide, hydrocortisone butyrate", "Mild: hydrocortisone 1–2.5%", "Ointments more potent than creams of same molecule; avoid potent on face, flexures, genitals, infants"])
D = [
dict(case="Asteatotic eczema", qa=[
 ECZ, TSA,
 ("What emollients are best and why?", ["Ointments (petrolatum — occlusive) most effective; humectants (glycerol, urea 5–10%, lactic acid) attract water; physiological lipid mixtures (ceramides, cholesterol, FFA 3:1:1) repair barrier; apply within 3 minutes after bathing; 'soak and smear'"]),
 ("Drug causes of xerosis/ asteatosis.", ["Diuretics, statins/ lipid-lowering agents, retinoids, cimetidine, EGFR inhibitors, BRAF inhibitors, clofazimine, nicotinic acid, protease inhibitors"]),
 ("What is 'winter itch' and pruritus of the elderly?", ["Generalised itch without primary lesions in elderly during winter — xerosis-related; exclude systemic causes (renal, hepatic, thyroid, iron deficiency, haematological malignancy, drugs, neuropathic); treat with emollients, cooling agents, avoid hot baths, sedating antihistamines cautiously (falls)"]),
 ]),
dict(case="Diaper (napkin) dermatitis", qa=[
 ECZ,
 ("Describe napkin psoriasis.", ["Well-demarcated bright red glazed plaques in napkin area including folds, often with psoriasiform lesions elsewhere (scalp, umbilicus, trunk); family history; may herald childhood psoriasis; treat with mild steroids, calcipotriol, tacrolimus"]),
 ("Langerhans cell histiocytosis in the napkin area — clues.", ["Persistent erosive/ petechial papules in folds (unlike irritant), scalp seborrhoeic-like scaling, purpura, hepatosplenomegaly, lymphadenopathy, bone lesions, diabetes insipidus; biopsy — CD1a+, CD207 (langerin)+ histiocytes; refer oncology"]),
 ("Allergic contact dermatitis in diaper area.", ["Less common; allergens — disperse dyes in diapers (blue/ pink), rubber additives (elastic bands — 'lucky Luke' pattern on outer buttocks/ thighs), fragrances in wipes (methylisothiazolinone), sorbitan sesquioleate; patch test in persistent cases; switch to dye-free diapers"]),
 ("Perianal streptococcal dermatitis.", ["Bright red, well-demarcated perianal erythema with pain on defecation, fissures, blood-streaked stools in children 6 months–10 years (group A strep); rapid strep test/ swab; treat with oral penicillin/ amoxicillin 10 days + topical mupirocin"]),
 ("Barrier products — composition and mechanism.", ["Zinc oxide (protective, mildly antiseptic), petrolatum (occlusive), dimethicone (silicone barrier), lanolin, titanium dioxide; apply thick layer at each change; avoid talc (inhalation risk) and boric acid"]),
 TSA,
 ]),
dict(case="Keratolysis exfoliativa", qa=[
 ECZ, TSA,
 ("What is juvenile plantar dermatosis?", ["Glazed, shiny, fissured erythema of weight-bearing forefoot and toe pads (sparing toe webs) in atopic children 3–14 y; worse in summer with synthetic socks/ occlusive shoes; treat with cotton socks, emollients/ barrier creams, change footwear; resolves at puberty"]),
 ("Recurrent focal palmar peeling — management advice.", ["Avoid wet work, detergents and solvents; cotton-lined gloves; regular emollients and urea 10% cream; avoid picking/ peeling the collarettes; reassure about benign recurrence"]),
 ("Hyperhidrosis link and treatment.", ["Palmar hyperhidrosis can aggravate keratolysis exfoliativa and pompholyx; treat with aluminium chloride hexahydrate 15–20%, tap water iontophoresis, botulinum toxin, oral glycopyrrolate/ oxybutynin, sympathectomy (last resort — compensatory sweating)"]),
 ]),
dict(case="Lichen simplex chronicus", qa=[
 ECZ, TSA,
 ("Dermoscopy findings.", ["White structureless areas with white scales, dotted/ glomerular vessels in clustered/ irregular distribution, erosions/ haemorrhagic crusts (excoriations), accentuated skin markings"]),
 ("Anogenital lichen simplex — special points.", ["Scrotum, vulva, perianal skin: intense nocturnal itch, thickened leathery skin; exclude LS, tinea, candidiasis, contact allergy (medicaments, fragrances, condoms), psoriasis, extramammary Paget's (biopsy if persistent); treat with potent steroid ointment, avoid irritants, tacrolimus, address anxiety"]),
 ("Intralesional triamcinolone technique for LSC.", ["Triamcinolone acetonide 5–10 mg/ml, 0.1 ml per cm² into the dermis of thickened plaques every 3–4 weeks (max ~20–40 mg/session); side effects — atrophy, hypopigmentation, telangiectasia"]),
 ]),
dict(case="Hand eczema & pompholyx", qa=[
 ECZ, TSA,
 ("What is the 'id reaction' in hand eczema?", ["Autoeczematisation: vesicular eruption on hands (pompholyx-like) triggered by distant inflammatory focus — tinea pedis (dermatophytide), stasis dermatitis, contact dermatitis; resolves after treating the primary site; KOH of feet"]),
 ("What is hyperkeratotic hand eczema?", ["Thick, fissured, scaly plaques on palms (central/ proximal) of middle-aged men, not very itchy; differentiate from palmar psoriasis (biopsy, nail/ scalp signs) and tinea manuum; treat with keratolytics, potent steroids under occlusion, acitretin/ alitretinoin, PUVA"]),
 ("Patient education — hand care programme.", ["Use lukewarm water, mild soap substitutes, dry hands well (including web spaces), apply emollient after every wash and at night (cotton gloves), gloves for wet work (≤15–20 min stretches with cotton liners), remove rings during wet work, avoid direct contact with irritants (detergents, solvents, raw foods)"]),
 ("Prognosis factors for hand eczema.", ["Poor prognosis: atopy (childhood eczema), extensive disease at diagnosis, early onset, contact allergy, continued wet work exposure, delay in diagnosis; better with early patch testing and allergen avoidance"]),
 ]),
dict(case="Nipple eczema", qa=[
 ECZ, TSA,
 ("Breastfeeding nipple pain — differentials.", ["Poor latch/ trauma (fissures), candidiasis (burning, shooting pain, shiny pink nipple — treat mother and baby), bacterial infection (S. aureus — fissures with crusts), vasospasm/ Raynaud's of nipple (blanching, pain after feeds — nifedipine), contact dermatitis (creams, pump parts), eczema, herpes"]),
 ("Nipple involvement in atopic dermatitis — features.", ["Bilateral scaly, fissured, itchy erythema of areola and nipple in adolescent girls/ young women; part of Hanifin–Rajka minor criteria; responds to mild steroids/ tacrolimus and emollients"]),
 ("Imaging and biopsy in suspected Paget's disease.", ["Mammography + ultrasound ± MRI breast to find underlying carcinoma (present in >90%); punch/ wedge biopsy of nipple skin; refer to breast surgeon — mastectomy or breast-conserving surgery with radiotherapy"]),
 ]),
dict(case="Nummular (discoid) eczema", qa=[
 ECZ, TSA,
 ("Histopathology of nummular eczema.", ["Acute/ subacute spongiotic dermatitis with spongiotic vesicles, parakeratosis with serum crusts and neutrophils, acanthosis; chronic lesions psoriasiform with lichenification"]),
 ("Nummular eczema with isotretinoin and other drugs.", ["Reported with isotretinoin (xerosis), interferon, ribavirin, TNF inhibitors, gold, methyldopa; withdraw/ treat xerosis aggressively"]),
 ("Nummular eczema vs psoriasis — clinical tips.", ["Nummular: oozing/ crusting in acute stage, poorly marginated periphery with satellite vesicles, intense itch, legs/ dorsa of hands, no nail pitting", "Psoriasis: silvery dry scale, sharp margins, extensors/ scalp, nail pitting, Auspitz sign, less itch"]),
 ("Systemic therapy options.", ["Short courses of prednisolone, methotrexate 7.5–15 mg/week, cyclosporine, azathioprine, NB-UVB; dupilumab (atopic background), oral antibiotics for impetiginised disease"]),
 ]),
dict(case="Prurigo nodularis", qa=[
 ECZ, TSA,
 ("Explain the neural changes and itch mediators.", ["Hypertrophy of dermal nerves with decreased intraepidermal small-fibre density (small fibre neuropathy), increased NGF, substance P and CGRP; IL-31, IL-4/IL-13 (Th2), IL-17/22, oncostatin M; mast cells and eosinophils — targets for dupilumab, nemolizumab"]),
 ("Dupilumab in PN — dose and evidence.", ["Approved for PN in adults: 600 mg loading then 300 mg every 2 weeks SC; PRIME trials — significant itch reduction (≥4-point WI-NRS) and nodule clearance; conjunctivitis main side effect"]),
 ("Chronic prurigo classification (EADV).", ["Chronic prurigo = chronic pruritus (≥6 weeks) + history/ signs of repeated scratching + multiple localised/ generalised pruriginous lesions; subtypes — papular, nodular, plaque, umbilicated, linear"]),
 ("What is uraemic pruritus and its treatment?", ["Common in CKD stage 5/ dialysis; xerosis, PN-like lesions; treat with emollients, UVB phototherapy, gabapentin/ pregabalin (renal dosing), difelikefalin (kappa-opioid agonist IV after dialysis), nalfurafine, optimise dialysis, kidney transplant"]),
 ("Cholestatic pruritus — treatment ladder.", ["Cholestyramine, rifampicin, naltrexone (opioid antagonist), sertraline; newer — IBAT inhibitors (odevixibat, maralixibat in paediatric cholestasis), fibrates; UV-B; treat cause (stent biliary obstruction)"]),
 ]),
dict(case="Seborrhoeic dermatitis", qa=[
 ECZ,
 ("Dermoscopy of scalp seborrhoeic dermatitis vs psoriasis.", ["Seborrhoeic: yellowish greasy scales, arborising thin red lines and atypical vessels, structureless red areas, honeycomb pigment", "Psoriasis: silvery-white scales, regularly distributed red dots/ globules and twisted red loops"]),
 ("Seborrhoeic dermatitis in neurological disease — why?", ["Parkinson's disease (increased sebum, facial immobility, autonomic dysfunction), post-stroke, spinal cord injury, facial nerve palsy (on affected side), syringomyelia — sebum pooling and Malassezia proliferation"]),
 ("Drugs that induce seborrhoeic dermatitis-like eruptions.", ["Neuroleptics (haloperidol, chlorpromazine), lithium, buspirone, methyldopa, cimetidine, interferon, gold, psoralens, EGFR/ BRAF inhibitors, dupilumab (head-neck dermatitis)"]),
 TSA,
 ("Seborrhoeic blepharitis — management.", ["Scaling of eyelid margins with crusts and redness; warm compresses, lid scrubs with diluted baby shampoo/ commercial lid cleansers twice daily, topical ketoconazole cream cautiously on eyelid skin, artificial tears; ophthalmology referral if keratitis"]),
 ]),
]
