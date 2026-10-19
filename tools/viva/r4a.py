# Viva deep redo — slot R4 (part A): eczemas II (6 cases)
# Own words. Topics guided by the previous-year question book (Sahana P Raju) — palmoplantar eczema classification,
# pompholyx, nummular/infective eczema, prurigo nodularis, seborrhoeic dermatitis; facts checked with IADVL 5e.
PYQ = "Previous-year PG question papers (Sahana P Raju, Solved Papers Dermatology)"
IA = "IADVL Textbook of Dermatology 5e"

D = [
dict(case="Hand eczema & pompholyx", src=f"{PYQ}; {IA} (Hand eczema); ESCD hand eczema guideline",
 qa=[
 ("Why is hand eczema important?", ["Commonest occupational skin disease (prevalence ~10% in general population, much higher in wet workers — health workers, cleaners, hairdressers, cooks, construction); chronic, causes job loss and poor quality of life"]),
 ("Classify hand eczema.", ["By cause: irritant contact (commonest), allergic contact, atopic hand eczema, protein contact dermatitis/contact urticaria, combinations", "By morphology: pompholyx (recurrent vesicular), hyperkeratotic (palmar), fingertip (pulpitis), nummular, apron (proximal palm and adjacent fingers), chronic fissured, ring dermatitis, wear-and-tear (dorsa)", "Acute (<3 months) vs chronic (>3 months or ≥2 relapses/year)"]),
 ("What is pompholyx (dyshidrotic eczema)? (PYQ)", ["Recurrent crops of deep-seated, itchy, tense vesicles ('sago-grain'/tapioca) on sides of fingers and palms ± soles; may form bullae; dry to brown spots and peeling in 2–3 weeks", "Triggers: hot weather, sweating, stress, atopy, nickel/cobalt systemic exposure, dermatophyte id reaction, IVIG, smoking", "Not a disorder of sweat glands despite the name"]),
 ("Differential diagnosis of vesicular hand eczema.", ["Tinea manuum/id reaction (look at feet, KOH), palmoplantar pustulosis (pustules, smokers), scabies (burrows), bullous pemphigoid (dyshidrosiform), herpes, hand-foot-mouth disease, dermatitis herpetiformis, EBS", "Hyperkeratotic hand eczema vs palmar psoriasis — psoriasis has sharper edges, other sites, nail pits; histology helps"]),
 ("Investigations.", ["Detailed occupational and exposure history, look at feet (tinea), KOH, patch test (standard + occupational series) in every chronic hand eczema, prick test for contact urticaria, biopsy if psoriasis suspected"]),
 ("Management of hand eczema.", ["Skin protection programme: avoid wet work >2 h/day, cotton-lined gloves, emollients after each wash, alcohol-based hand rubs preferable to soap", "Topical: potent steroids (clobetasol, mometasone) for short courses then intermittent; tacrolimus; delgocitinib cream (topical pan-JAK inhibitor approved for chronic hand eczema)", "Phototherapy: hand PUVA (topical psoralen) or NB-UVB", "Systemic: alitretinoin 30 mg/day for chronic hyperkeratotic hand eczema (teratogenic), acitretin (hyperkeratotic), short oral steroid for acute flares, cyclosporine, methotrexate, azathioprine, dupilumab (atopic hand eczema)", "Pompholyx: potassium permanganate soaks (1:10,000), potent steroid, drain large bullae, treat id source, botulinum toxin if hyperhidrosis, low-nickel diet if nickel-sensitive"]),
 ("What is apron eczema?", ["Eczema on the proximal palm and adjacent volar surfaces of fingers — often allergic (food handlers) or atopic"]),
 ("What is fingertip eczema?", ["Dry, fissured, scaly fingertips (pulpitis) — irritant (paper handlers), allergic (garlic — tulipalin/diallyl disulphide in chefs; Alstroemeria tulipalin in florists), atopic"]),
 ("Prognosis?", ["Poor in atopics and when wet work continues; ~50% still have it after 15 years; early diagnosis, education and allergen avoidance improve outcome"]),
 ],
 spot=["Tapioca-like deep vesicles on finger sides — pompholyx", "Chronic hand eczema — always patch test"]),

dict(case="Nipple eczema", src=f"{PYQ}; {IA} (Eczemas, breast dermatoses)",
 qa=[
 ("What are the causes of nipple/areolar eczema?", ["Atopic dermatitis (minor criterion of Hanifin–Rajka) — commonest, usually bilateral, adolescent girls", "Irritant (friction — 'jogger's nipple', breastfeeding — saliva, pumps), allergic contact (nursing creams, lanolin, fragrances, bra materials), Candida during breastfeeding, scabies (areolae in women), seborrhoeic"]),
 ("Why is unilateral persistent nipple eczema a red flag?", ["Paget's disease of the nipple — intra-epidermal spread of underlying ductal breast carcinoma; unilateral, slowly progressive, well-defined, crusted/eroded, may have nipple retraction, discharge, lump", "Any unilateral nipple eczema not responding to 3–4 weeks of topical steroid needs biopsy and breast imaging"]),
 ("Differentiate eczema from Paget's disease of nipple.", ["Eczema: bilateral, itchy, ill-defined, starts on areola, fluctuates, responds to steroids, nipple intact", "Paget's: unilateral, little itch, sharply demarcated, starts on nipple then areola, persistent, steroid-unresponsive, nipple may be destroyed/retracted; histology — large pale Paget cells (CK7+, CEA+, HER2+)"]),
 ("Other differentials.", ["Psoriasis, erosive adenomatosis of nipple, Bowen's disease, hyperkeratosis of nipple and areola (naevoid), tinea, herpes, scabies"]),
 ("Management of nipple eczema in breastfeeding women.", ["Emollient (pure petrolatum), mild topical steroid applied after feeds and wiped before the next feed; treat Candida in mother and baby (oral thrush) with topical azole/nystatin; correct latch; avoid allergenic nursing creams"]),
 ("Work-up in a non-healing case.", ["Patch test (if contact allergy), KOH, skin biopsy, mammography/ultrasound for Paget's"]),
 ("What is hyperkeratosis of nipple and areola?", ["Rare benign verrucous thickening and pigmentation — naevoid, associated with ichthyosis/AD/ CTCL or oestrogen therapy; keratolytics, retinoids, cryotherapy"]),
 ],
 spot=["Unilateral, steroid-resistant nipple 'eczema' — biopsy for Paget's disease"]),

dict(case="Nummular (discoid) eczema", src=f"{PYQ}; {IA} (Eczemas)",
 qa=[
 ("What is nummular eczema?", ["Chronic eczema with coin-shaped (nummular) well-demarcated plaques, very itchy", "Two age peaks: young women (15–25) and elderly men (50–65); also in atopic children"]),
 ("Morphology.", ["Starts as tiny papulovesicles that coalesce into round plaques 1–10 cm, oozing and crusting in acute stage, scaly and lichenified later; may show central clearing (mimicking tinea)", "Sites: legs and dorsa of hands and feet, extensor forearms, trunk"]),
 ("Aetiological associations.", ["Xerosis and barrier damage, atopy, S. aureus colonisation (infective eczema), contact allergy (nickel, chromate, fragrances, neomycin), venous stasis, alcohol, drugs (isotretinoin, interferon, TNF inhibitors), dental/focal infection (older theory)"]),
 ("Differential diagnosis.", ["Tinea corporis (active edge, KOH), psoriasis (silvery scale, nails, other sites), impetigo, Bowen's disease (single, slowly growing), mycosis fungoides, granuloma annulare, contact dermatitis, lichen simplex"]),
 ("What is infective (infectious eczematoid) dermatitis? (PYQ)", ["Eczema around a discharging infected focus (otitis externa, ulcer, fistula) from exudate; spreads peripherally; treat infection + steroid", "Significance of bacteria in eczema — S. aureus colonises >90% of AD lesions; superantigens drive inflammation and steroid resistance"]),
 ("Investigations.", ["KOH, swab culture, patch test (especially if refractory), biopsy if atypical, blood sugar"]),
 ("Treatment.", ["Emollients, potent topical steroid (ointment) ± occlusion; combined steroid–antibiotic for short term when infected; oral antibiotics (cephalexin, cloxacillin) for widespread infected lesions", "Tacrolimus, coal tar, NB-UVB, systemic agents (methotrexate, cyclosporine) for widespread resistant disease; sedating antihistamines", "Treat xerosis, stop alcohol"]),
 ("Prognosis?", ["Chronic and relapsing; often recurs at previous sites"]),
 ],
 spot=["Coin-shaped oozing itchy plaques on legs — nummular eczema; do KOH to exclude tinea"]),

dict(case="Prurigo nodularis", src=f"{PYQ}; {IA} (Prurigo); EADV prurigo task-force concept of chronic prurigo",
 qa=[
 ("What is prurigo nodularis (PN)? (PYQ)", ["Chronic, intensely itchy, firm hyperkeratotic nodules (few mm–2 cm) due to chronic scratching; the nodular type of 'chronic prurigo' (itch >6 weeks + scratch lesions)", "Middle-aged and elderly; symmetrical on extensor limbs, upper back (spares mid-back — 'butterfly sign'), buttocks"]),
 ("Aetiological associations — work-up for a cause.", ["Dermatological: atopic dermatitis (most common association, 'atopic PN'), xerosis, insect bites, contact dermatitis", "Systemic: chronic kidney disease, liver disease (cholestasis, hepatitis C), diabetes, thyroid disease, iron deficiency, HIV, lymphoma/malignancy, gluten enteropathy", "Neurological: small fibre neuropathy, notalgia paraesthetica", "Psychiatric: depression, anxiety, OCD, substance use"]),
 ("Pathogenesis.", ["Neuroimmune circuit: itch–scratch cycle, increased dermal nerve fibres with reduced intraepidermal nerve density, neuropeptides (substance P, CGRP), IL-31, IL-4/13 (Th2), mast cells, eosinophils, periostin and fibrosis"]),
 ("Histopathology.", ["Marked hyperkeratosis, irregular/pseudoepitheliomatous acanthosis, fibrosis with vertical collagen, thickened dermal nerves (neural hyperplasia), increased mast cells and eosinophils"]),
 ("Differential diagnosis.", ["Hypertrophic lichen planus, nodular scabies, insect-bite reactions, pemphigoid nodularis, multiple keratoacanthomas, perforating disorders (acquired reactive perforating collagenosis in diabetics/CKD), dermatitis artefacta, lichen amyloidosis, nodular prurigo of pregnancy, epidermolysis bullosa pruriginosa"]),
 ("Investigations (screen for systemic disease).", ["CBC with eosinophils, renal and liver function, thyroid, blood sugar/HbA1c, iron studies, HIV, hepatitis B/C, chest X-ray, total IgE; biopsy (± DIF to exclude pemphigoid nodularis), skin scraping for scabies; age-appropriate cancer screening if indicated"]),
 ("Management (step-wise).", ["Break the cycle: emollients, cooling lotions (menthol, polidocanol), keep nails short, occlude lesions", "Topical: super-potent steroid under occlusion, intralesional triamcinolone, calcipotriol, tacrolimus, capsaicin", "Phototherapy: NB-UVB, UVA1, PUVA; cryotherapy for individual nodules", "Systemic: gabapentin/pregabalin, antidepressants (paroxetine, mirtazapine, amitriptyline), naltrexone/opioid modulators, methotrexate, cyclosporine, thalidomide (neuropathy risk)", "Biologics: dupilumab (approved for PN), nemolizumab (anti-IL-31RA; approved for PN 2024); JAK inhibitors under study"]),
 ("What is the butterfly sign?", ["Sparing of the mid-upper back (area patient cannot reach) — indicates lesions are from scratching"]),
 ("Prognosis?", ["Very chronic; nodules persist months–years even after itch control; severe impact on sleep and mood"]),
 ],
 spot=["Symmetric itchy hyperkeratotic nodules sparing mid-back — prurigo nodularis", "Screen kidney, liver, thyroid, HIV, malignancy"],
 note="Nemolizumab approval for PN is newer than the textbooks — confirm current Indian availability."),

dict(case="Seborrhoeic dermatitis", src=f"{PYQ}; {IA} (Seborrhoeic dermatitis)",
 qa=[
 ("Define seborrhoeic dermatitis.", ["Chronic relapsing inflammatory dermatosis in sebum-rich areas (scalp, face, chest, flexures), characterised by red patches with greasy yellowish scales; dandruff (pityriasis capitis) is its mildest form"]),
 ("Who gets it? (bimodal)", ["Infants (first 3 months — cradle cap, napkin/flexures; self-limiting) and adults (30–60 years, men more)", "Higher prevalence and severity in HIV (30–80%), Parkinson's disease and other neurological disorders (facial immobility, sebum pooling), Down syndrome, depression, alcoholism, after neuroleptics"]),
 ("Pathogenesis.", ["Malassezia yeasts (M. globosa, M. restricta) metabolise sebum triglycerides into irritant free fatty acids (oleic acid) → inflammation in susceptible individuals (barrier defects)", "Sebum quantity is not necessarily increased; host immune response, stress, cold dry weather contribute"]),
 ("Clinical features in adults.", ["Scalp: diffuse fine scaling to thick adherent greasy scales with erythema, may extend to forehead hairline (corona seborrhoica)", "Face: eyebrows, glabella, nasolabial folds, beard, eyelids (blepharitis), ears (retroauricular fissuring, external canal)", "Trunk: petaloid (annular) lesions on presternal/interscapular areas, pityriasiform type", "Flexures: axillae, groin, submammary, umbilicus — intertrigo-like", "Seborrhoeic erythroderma (rare)"]),
 ("Infantile seborrhoeic dermatitis vs infantile atopic dermatitis.", ["Seborrhoeic: onset first weeks, greasy yellow scales, scalp/flexures/napkin area involved, little itch, baby comfortable, resolves by 6–12 months", "Atopic: onset after 2–3 months, cheeks/extensors, napkin area spared, very itchy, irritable baby, family history, chronic course"]),
 ("What is Leiner's disease?", ["Historical term — generalised seborrhoeic-like erythroderma in infants with diarrhoea, failure to thrive and recurrent infections; now linked to immunodeficiency (C3/C5 dysfunction, SCID, Omenn)"]),
 ("Differential diagnosis.", ["Scalp: psoriasis (sharply defined, silvery scale, beyond hairline, nails), tinea capitis, atopic dermatitis, pityriasis amiantacea, LCH (infants), head lice", "Face: rosacea, lupus (malar), contact dermatitis, tinea faciei, perioral dermatitis", "Trunk: pityriasis versicolor, pityriasis rosea, secondary syphilis, Darier's disease", "'Sebopsoriasis' — overlap"]),
 ("Why test for HIV in severe seborrhoeic dermatitis?", ["Sudden onset, extensive, severe or treatment-resistant seborrhoeic dermatitis in a young adult may be an early marker of HIV infection"]),
 ("Treatment.", ["Scalp: antifungal shampoos (ketoconazole 2%, ciclopirox 1%, selenium sulphide 2.5%, zinc pyrithione) 2–3 times weekly with 5 min contact; keratolytics (salicylic acid, coal tar) for thick scales; short course of steroid lotion/ foam (betamethasone, clobetasol shampoo)", "Face/body: ketoconazole 2% cream, mild steroid (hydrocortisone/desonide) for short periods, calcineurin inhibitors (tacrolimus/pimecrolimus) as steroid-sparing, roflumilast 0.3% foam (newer topical PDE4 inhibitor)", "Blepharitis: lid hygiene with dilute baby shampoo", "Infants: emollient/olive oil to soften crusts, gentle brushing, mild shampoo; ketoconazole cream if needed", "Severe/extensive: oral itraconazole 200 mg/day for 7 days then 2 days/month maintenance, fluconazole; isotretinoin low dose; phototherapy NB-UVB", "Maintenance shampoo once weekly to prevent relapse"]),
 ("Histopathology.", ["Psoriasiform and spongiotic dermatitis with parakeratosis around follicular ostia ('shoulder parakeratosis'), neutrophils in scale crusts; yeasts in scale"]),
 ],
 spot=["Greasy yellow scales on scalp, eyebrows, nasolabial folds — seborrhoeic dermatitis", "Severe sudden seb derm in young adult — test HIV; also Parkinson's"]),
]
