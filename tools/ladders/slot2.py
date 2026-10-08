# Treatment ladders, slot 2: eczemas, papulosquamous, reactive & drug, hair & nail, pigmentary.
# Drafted from IADVL Textbook (new edition), Rook's 10e and Wolverton 4e, plus current guidelines; facts only, own wording.
# rx line: "Drug | dose | freq | duration | route | note"
D = []
def L(case, group, general, l1, l2, l3=None, special=""):
    D.append(dict(case=case, group=group, general=general, lines=[x for x in (l1, l2, l3) if x], special=special))

E="Eczemas"
L("Atopic dermatitis",E,
  "Daily emollient (at least twice, and after bathing), short lukewarm baths, soap-free cleanser, cotton clothes, short nails. Treat infection. Proactive twice-weekly anti-inflammatory on usual sites once controlled.",
  ("Mild–moderate: topical",[
   "Cream Mometasone 0.1% (body) / Hydrocortisone 1% (face, folds) | Thin layer (fingertip units) | OD | 1–2 weeks, then twice weekly | Topical | Step down once clear",
   "Ointment Tacrolimus 0.03% (child) / 0.1% (adult) | Thin layer | BD | Till clear, then twice weekly | Topical | Face, eyelids, folds; burning in first week",
   "Tab. Levocetirizine 5 mg / Syp. Hydroxyzine | | HS | 2–4 weeks | Oral | Sedating antihistamine helps sleep only"]),
  ("Moderate–severe or not controlled",[
   "Narrowband UVB phototherapy | | 2–3×/week | 3–6 months | Phototherapy | Adults and older children",
   "Cap. Cyclosporine 100 mg | 3–5 mg/kg/day in 2 doses | BD | 3–6 months, then taper | Oral | BP and creatinine every 2 weeks at first; fastest acting",
   "Tab. Methotrexate 7.5 mg | 7.5–15 mg (child 0.3–0.5 mg/kg) | Once weekly | Months | Oral | With folic acid 5 mg on other days; CBC, LFT"]),
  ("Severe, refractory",[
   "Inj. Dupilumab | 600 mg loading, then 300 mg | Every 2 weeks | Long-term | Subcutaneous | Conjunctivitis common; children by weight",
   "Tab. Upadacitinib 15 mg / Abrocitinib 100 mg | 1 tab | OD | Long-term | Oral | ≥12 yr; TB, hepatitis, lipids, CBC screening — see Drug safety",
   "Tab. Azathioprine 50 mg | 1–2.5 mg/kg (by TPMT) | OD | Months | Oral | Adults only; slow onset"]),
  "Avoid oral steroids except as a short bridge (rebound flare). Pregnancy: emollients, topical steroids, NB-UVB; cyclosporine if essential. Eczema herpeticum: IV/oral acyclovir urgently.")

L("Contact dermatitis",E,
  "Identify and avoid the cause — patch test (Indian Standard Series) for suspected allergic contact dermatitis. Gloves with cotton liners, barrier creams, substitution of the product.",
  ("Localised",[
   "Cream Mometasone 0.1% / Clobetasol 0.05% (hands, feet) | Thin layer | OD–BD | 2–3 weeks | Topical | Then taper",
   "Wet compresses (saline / potassium permanganate 1:10,000) | | BD | Acute oozing stage | Topical | ",
   "Emollient / barrier cream | | Frequently | Ongoing | Topical | "]),
  ("Widespread / acute severe",[
   "Tab. Prednisolone 20 mg | 0.5–1 mg/kg | OD | Taper over 2–3 weeks | Oral | Short taper to avoid rebound (e.g. Parthenium)",
   "Tab. Levocetirizine 5 mg | 1 tab | HS | 2–4 weeks | Oral | "]),
  ("Chronic (e.g. airborne Parthenium dermatitis)",[
   "Tab. Azathioprine 50 mg | 300 mg (6 tabs) | Once weekly | 6 months | Oral | Weekly pulse regimen; CBC and LFT before and monthly",
   "Tab. Methotrexate / Cap. Cyclosporine / PUVA | | | Months | Oral | Steroid-sparing alternatives"]))

L("Asteatotic eczema",E,
  "Fewer, shorter, lukewarm baths, soap substitute, avoid scrubbing; humidify room. Liberal greasy emollient within 3 minutes of bathing. Look for hypothyroidism, malnutrition, drugs (diuretics, statins).",
  ("First line",[
   "Emollient (white soft paraffin / urea 10% / lactic acid 12%) | Liberal | BD–TDS | Long-term | Topical | ",
   "Ointment Mometasone 0.1% | Thin layer | OD | 1–2 weeks | Topical | Inflamed areas only"]),
  ("Itchy, widespread",[
   "Tab. Levocetirizine 5 mg | 1 tab | HS | 2 weeks | Oral | Avoid strongly sedating antihistamines in elderly",
   "Narrowband UVB | | 2–3×/week | 6–8 weeks | Phototherapy | For generalised pruritus"]))

L("Diaper (napkin) dermatitis",E,
  "Change diapers often (every 2–3 h), diaper-free time daily, superabsorbent diapers, wipe with water or alcohol-free wipes, thick barrier paste at every change. No powders, no potent steroids, no combination steroid–antifungal creams.",
  ("Irritant",[
   "Zinc oxide paste / petrolatum | Thick layer | Every change | Till clear | Topical | ",
   "Cream Hydrocortisone 1% | Thin layer | BD | 5–7 days | Topical | Only if inflamed"]),
  ("Candida (satellite lesions, fold involvement)",[
   "Cream Clotrimazole 1% / Nystatin | Thin layer | BD–TDS | 2 weeks | Topical | Under the barrier paste",
   "Oral thrush: Nystatin oral suspension 1 mL | 1 mL | QID | 7–14 days | Oral | "]),
  ("Bacterial / not responding",[
   "Cream Mupirocin 2% | Thin layer | TDS | 5–7 days | Topical | If impetiginised; rethink diagnosis (psoriasis, LCH, zinc deficiency)"]))

L("Keratolysis exfoliativa",E,
  "Self-limiting peeling of palms; avoid soap, detergents and friction. Reassure.",
  ("First line",[
   "Cream Urea 10–20% / Lactic acid 12% | Thin layer | BD | 4 weeks | Topical | ",
   "Emollient / barrier cream | | Frequently | Ongoing | Topical | "]),
  ("Persistent",[
   "Cream Tacrolimus 0.1% / mild steroid | Thin layer | BD | 2 weeks | Topical | If inflamed"]))

L("Lichen simplex chronicus",E,
  "Break the itch–scratch cycle: explain habit, keep nails short, cover at night, look for and treat anxiety, underlying eczema or nerve-related itch.",
  ("First line",[
   "Ointment Clobetasol 0.05% | Thin layer | OD–BD | 2–4 weeks | Topical | Under occlusion (cling film) at night speeds response",
   "Tab. Hydroxyzine 25 mg | 1 tab | HS | 4 weeks | Oral | Sedation helps night scratching"]),
  ("Thick plaques",[
   "Inj. Triamcinolone 10 mg/mL | 0.1 mL per cm² | Every 3–4 weeks | 2–3 sessions | Intralesional | ",
   "Ointment Tacrolimus 0.1% / Capsaicin 0.025% | Thin layer | BD | 4–8 weeks | Topical | Steroid-sparing"]),
  ("Refractory",[
   "Tab. Doxepin 10 mg / Amitriptyline 10 mg | 1 tab | HS | 1–3 months | Oral | Or SSRI if anxious / obsessive",
   "Tab. Gabapentin 300 mg / Pregabalin 75 mg | | HS | 1–3 months | Oral | Neuropathic itch (e.g. brachioradial)"]))

L("Hand eczema & pompholyx",E,
  "Gloves for wet work (cotton liners), soap substitute, emollient after every wash, remove rings. Patch test if chronic. Treat tinea of feet if dermatophytide suspected.",
  ("Mild–moderate",[
   "Ointment Clobetasol 0.05% / Mometasone 0.1% | Thin layer | OD | 2–4 weeks, then twice weekly | Topical | ",
   "Potassium permanganate 1:10,000 soaks | 15 min | BD | Acute vesicular stage | Topical | Then aspirate large blisters",
   "Emollient (paraffin-based) | | After each wash | Long-term | Topical | "]),
  ("Severe or chronic",[
   "Tab. Prednisolone 20 mg | 0.5 mg/kg | OD | 1–2 weeks taper | Oral | Short course for acute pompholyx flare",
   "Hand PUVA / NB-UVB (local) | | 3×/week | 2–3 months | Phototherapy | "]),
  ("Refractory chronic",[
   "Tab. Methotrexate 7.5 mg | 7.5–15 mg | Weekly | Months | Oral | With folic acid",
   "Cap. Acitretin 25 mg / Alitretinoin 30 mg | 1 cap | OD | 3–6 months | Oral | Hyperkeratotic type; strict contraception (acitretin 3 years)",
   "Cap. Cyclosporine | 3 mg/kg/day | BD | 3 months | Oral | "]))

L("Nipple eczema",E,
  "Unilateral, persistent, non-responding nipple eczema in an adult needs biopsy to exclude Paget's disease. Avoid irritants; breastfeeding mothers: check latch, treat candida.",
  ("First line",[
   "Cream Hydrocortisone 1% / Mometasone 0.1% | Thin layer | BD | 1–2 weeks | Topical | Wipe off before breastfeeding",
   "Emollient / white soft paraffin | | After feeds | Ongoing | Topical | "]),
  ("Not responding",[
   "Ointment Tacrolimus 0.03% | Thin layer | BD | 2–4 weeks | Topical | ",
   "Cream Clotrimazole 1% / Mupirocin 2% | Thin layer | BD | 2 weeks | Topical | If candida / bacterial infection"]))

L("Nummular (discoid) eczema",E,
  "Emollients, soap substitute; often secondarily infected — treat staph. Look for xerosis, venous disease, contact allergy.",
  ("First line",[
   "Ointment Clobetasol 0.05% / Mometasone 0.1% | Thin layer | OD | 2–4 weeks | Topical | Potent steroid needed",
   "Cream Fusidic acid 2% | Thin layer | BD | 1 week | Topical | If crusted / oozing"]),
  ("Extensive or infected",[
   "Cap. Cephalexin 500 mg | 1 cap | QID | 7 days | Oral | ",
   "Narrowband UVB | | 2–3×/week | 2–3 months | Phototherapy | "]),
  ("Refractory",[
   "Tab. Methotrexate 7.5–15 mg | | Weekly | Months | Oral | Or cyclosporine short course"]))

L("Prurigo nodularis",E,
  "Look for the cause of itch: atopy, renal and liver disease, thyroid, HIV, iron deficiency, lymphoma, depression. Short nails, cover lesions.",
  ("Topical / intralesional",[
   "Ointment Clobetasol 0.05% | Thin layer | OD under occlusion | 4–8 weeks | Topical | ",
   "Inj. Triamcinolone 10 mg/mL | Into nodules | Every 3–4 weeks | | Intralesional | ",
   "Calcipotriol / capsaicin / cryotherapy | | | | Topical | Adjuncts"]),
  ("Widespread",[
   "Narrowband UVB / PUVA | | 3×/week | 3 months | Phototherapy | ",
   "Tab. Gabapentin 300 mg / Pregabalin 75 mg | Titrate | | 3 months | Oral | ",
   "Tab. Methotrexate 7.5–15 mg / Cap. Cyclosporine 3–5 mg/kg | | | Months | Oral | "]),
  ("Refractory",[
   "Inj. Dupilumab | 600 mg loading, then 300 mg | Every 2 weeks | Long-term | Subcutaneous | Approved for prurigo nodularis",
   "Tab. Thalidomide 100 mg | 50–100 mg | HS | Months | Oral | Strict pregnancy prevention; neuropathy monitoring"]))

L("Seborrhoeic dermatitis",E,
  "Chronic relapsing: control, not cure. Regular antifungal shampoo; stress, sleep loss and winter worsen. Severe or sudden-onset: check HIV, Parkinsonism.",
  ("Scalp / face – first line",[
   "Shampoo Ketoconazole 2% | Leave 5 min | 2–3×/week | 4 weeks, then weekly | Topical | ",
   "Cream Ketoconazole 2% | Thin layer | BD | 4 weeks | Topical | Face, folds",
   "Lotion Clobetasol (scalp) / Cream Hydrocortisone 1% (face) | | OD | 1–2 weeks | Topical | Short course for flares"]),
  ("Frequent flares",[
   "Cream Tacrolimus 0.1% / Pimecrolimus 1% | Thin layer | BD | 2–4 weeks | Topical | Steroid-sparing for face",
   "Shampoo Ciclopirox 1% / Zinc pyrithione / Coal tar | | Alternate | Ongoing | Topical | Rotate shampoos"]),
  ("Severe / extensive",[
   "Cap. Itraconazole 100 mg | 200 mg | OD | 1 week, then 200 mg on 2 days a month | Oral | ",
   "Cap. Isotretinoin 10 mg | 0.1–0.3 mg/kg | OD | 3–6 months | Oral | Refractory; contraception"]),
  "Infants (cradle cap): emollient / olive oil to soften scales, gentle brushing, mild shampoo; ketoconazole cream if needed.")

P="Papulosquamous & erythroderma"
L("Psoriasis",P,
  "Assess BSA, PASI, DLQI, nails, joints, metabolic syndrome, depression. Emollients, stop smoking and alcohol, weight loss. Avoid systemic steroids (pustular flare). Check triggers: beta-blockers, lithium, antimalarials, infections.",
  ("Limited (BSA <10%, PASI <10)",[
   "Ointment Clobetasol 0.05% + Calcipotriol | Thin layer | OD | 4 weeks, then weekends | Topical | Calcipotriol–betamethasone gel for scalp",
   "Coal tar 5% / Salicylic acid 3–6% ointment | | HS | 4–8 weeks | Topical | Thick scale",
   "Cream Tacrolimus 0.1% | Thin layer | BD | | Topical | Face, flexures, genitals"]),
  ("Moderate–severe (BSA >10%, PASI >10, DLQI >10) or difficult sites",[
   "Tab. Methotrexate 2.5 mg | 7.5 → 15–25 mg | Once weekly | Long-term | Oral | Folic acid 5 mg; CBC, LFT, creatinine — see Drug safety",
   "Narrowband UVB / PUVA | | 2–3×/week | 2–3 months | Phototherapy | ",
   "Cap. Cyclosporine 100 mg | 2.5–5 mg/kg/day | BD | Up to 12 months | Oral | Quick control (erythrodermic, pustular); BP, creatinine",
   "Cap. Acitretin 25 mg | 0.3–0.5 mg/kg | OD | Months | Oral | Pustular / palmoplantar; contraception for 3 years after"]),
  ("Failed / unsuitable for conventional systemics, or psoriatic arthritis",[
   "Tab. Apremilast 30 mg | Titrate over 5 days | BD | Long-term | Oral | No lab monitoring; GI upset, low mood",
   "Biologics: Adalimumab / Secukinumab / Itolizumab / Ustekinumab / Guselkumab / Risankizumab | per label | | Long-term | Subcutaneous | TB, hepatitis B/C, HIV screening first",
   "Tab. Tofacitinib / Deucravacitinib | per label | | | Oral | Alternative small molecules"]),
  "Pregnancy: emollients, topical steroids, NB-UVB; cyclosporine or certolizumab if systemic needed. No methotrexate (stop 3 months before conception) or acitretin. Children: topicals, NB-UVB, methotrexate 0.2–0.4 mg/kg/week.")

L("Erythroderma",P,
  "Admit if unwell. Fluids, temperature, nutrition (high protein), skin care: bland emollients, wet wraps. Find the cause: psoriasis, eczema, drugs, CTCL (Sézary), PRP, scabies. Stop all non-essential drugs.",
  ("All patients",[
   "Liquid paraffin / white soft paraffin | Liberal | QID | Throughout | Topical | ",
   "Cream Mometasone 0.1% (diluted / mid-potency) | Thin layer | BD | 2 weeks | Topical | Under wet wraps",
   "Tab. Hydroxyzine 25 mg | 1 tab | HS | | Oral | Itch; sedation"]),
  ("Treat the cause",[
   "Psoriatic: Cap. Cyclosporine 3–5 mg/kg/day or Tab. Methotrexate | | | | Oral | Avoid oral steroids",
   "Drug-induced: Tab. Prednisolone 0.5–1 mg/kg | | OD | Taper 2–4 weeks | Oral | After stopping the drug",
   "Eczematous: NB-UVB / methotrexate / cyclosporine once stable | | | | | "]),
  special="Check albumin, electrolytes, renal function, CBC; watch for sepsis, hypothermia, high-output cardiac failure.")

L("Lichen planus",P,
  "Stop suspected drugs; check hepatitis C. Oral LP: avoid spicy food, tobacco; dental check, metallic restorations. Pigmentation fades slowly.",
  ("Limited cutaneous",[
   "Ointment Clobetasol 0.05% | Thin layer | OD | 4 weeks | Topical | Hypertrophic: under occlusion or intralesional triamcinolone",
   "Tab. Levocetirizine 5 mg / Hydroxyzine 25 mg | | HS | 4 weeks | Oral | "]),
  ("Widespread or rapidly progressive",[
   "Tab. Prednisolone 20 mg | 0.5 mg/kg | OD | 4–6 weeks taper | Oral | Or betamethasone/dexamethasone oral mini-pulse 5 mg on 2 consecutive days a week",
   "Narrowband UVB | | 3×/week | 2–3 months | Phototherapy | "]),
  ("Refractory / chronic",[
   "Tab. Methotrexate 7.5–15 mg / Cap. Acitretin 25 mg | | Weekly / OD | Months | Oral | ",
   "Tab. Hydroxychloroquine 200 mg / Cap. Cyclosporine | | | | Oral | Oral LP: also topical tacrolimus 0.1%, clobetasol in orabase"]),
  "Oral erosive LP needs long-term follow-up (small SCC risk).")

L("Lichen striatus",P,
  "Self-limiting in 6–12 months in most children; reassure. Treatment is for itch or appearance.",
  ("If symptomatic",[
   "Cream Mometasone 0.1% | Thin layer | OD | 2–4 weeks | Topical | ",
   "Ointment Tacrolimus 0.03% | Thin layer | BD | 4–8 weeks | Topical | Face; hypopigmentation"]),
  ("Persistent",[
   "Watchful waiting | | | | | Residual hypopigmentation recovers slowly"]))

L("Parapsoriasis",P,
  "Small-plaque type is usually benign; large-plaque type can progress to mycosis fungoides — biopsy and follow every 6–12 months.",
  ("First line",[
   "Emollients + Cream Mometasone 0.1% | Thin layer | OD | 4–8 weeks | Topical | ",
   "Narrowband UVB | | 2–3×/week | 2–3 months | Phototherapy | Most effective"]),
  ("Large-plaque / persistent",[
   "PUVA | | 2–3×/week | | Phototherapy | Biopsy repeated if lesions change"]))

L("Pityriasis rosea",P,
  "Self-limiting in 6–8 weeks; reassure; exclude secondary syphilis (VDRL) and drug causes. In pregnancy, refer to obstetrician (early pregnancy risk).",
  ("Itchy",[
   "Calamine lotion | Apply | TDS | 2 weeks | Topical | ",
   "Cream Mometasone 0.1% | Thin layer | OD | 1–2 weeks | Topical | ",
   "Tab. Levocetirizine 5 mg | 1 tab | HS | 2 weeks | Oral | "]),
  ("Extensive or early with systemic symptoms",[
   "Tab. Acyclovir 800 mg | 1 tab | 5×/day | 7 days | Oral | Early in the course, may shorten it",
   "Narrowband UVB | | 3×/week | 2–4 weeks | Phototherapy | For extensive itchy disease"]))

L("Pityriasis rubra pilaris",P,
  "Emollients and keratolytics; rule out HIV in atypical (type VI). Slow response; type I often clears in 3 years.",
  ("Limited",[
   "Urea 10–20% / Salicylic acid 6% ointment | | BD | Long-term | Topical | ",
   "Ointment Clobetasol 0.05% / Calcipotriol | Thin layer | OD | 4–8 weeks | Topical | "]),
  ("Extensive – first systemic",[
   "Cap. Isotretinoin 20 mg | 0.5–1 mg/kg | OD | 4–6 months | Oral | Or acitretin 25–50 mg/day; contraception",
   "Tab. Methotrexate 10–25 mg | | Weekly | Months | Oral | Alone or with retinoid (watch liver)"]),
  ("Refractory",[
   "Biologics: IL-17 / IL-23 inhibitors / TNF inhibitors | per label | | | Subcutaneous | Case-series evidence"]))

R="Reactive & drug eruptions"
L("Urticaria & angioedema",R,
  "Find and avoid triggers (NSAIDs, foods only if clearly linked, infections). Acute: usually no tests. Chronic (>6 weeks): CBC, ESR/CRP; thyroid antibodies if indicated. Score with UAS7, control with UCT. Angioedema without wheals: check for ACE inhibitor, C4 (hereditary).",
  ("Standard-dose non-sedating H1 antihistamine",[
   "Tab. Levocetirizine 5 mg / Fexofenadine 180 mg / Bilastine 20 mg | 1 tab | OD | Daily till 3 months symptom-free | Oral | Regular, not as needed"]),
  ("Not controlled in 2–4 weeks: up-dose",[
   "Same H1 antihistamine | Up to 4 tabs a day | BD | 2–4 weeks, then step down | Oral | Avoid mixing different antihistamines",
   "Severe acute flare: Tab. Prednisolone 20 mg | 0.5 mg/kg | OD | 3–7 days | Oral | Short course only"]),
  ("Still not controlled",[
   "Inj. Omalizumab | 300 mg | Every 4 weeks | 6 months, reassess | Subcutaneous | Observe 2 h after dose; can increase to 600 mg / every 2 weeks",
   "Cap. Cyclosporine 100 mg | 3–5 mg/kg/day | BD | 3–6 months | Oral | If omalizumab not available or not effective; BP, creatinine",
   "Tab. Dapsone / Hydroxychloroquine / Montelukast | | | | Oral | Add-on options with weaker evidence"]),
  "Anaphylaxis/laryngeal angioedema: Inj. adrenaline 0.5 mg IM (1:1000) and emergency care. Pregnancy: loratadine/cetirizine preferred.")

L("Erythema multiforme",R,
  "Most cases follow herpes simplex; others mycoplasma or drugs. Mouth care: antiseptic and anaesthetic mouthwash, soft diet.",
  ("Minor",[
   "Cream Mometasone 0.1% | Thin layer | BD | 1 week | Topical | ",
   "Tab. Levocetirizine 5 mg | 1 tab | HS | 1–2 weeks | Oral | ",
   "Benzydamine / lignocaine 2% viscous mouthwash | 10 mL | Before meals | | Oral rinse | "]),
  ("Major / mucosal",[
   "Tab. Prednisolone 20 mg | 0.5–1 mg/kg | OD | Short taper over 1–2 weeks | Oral | Early in severe mucosal disease",
   "Mycoplasma: Tab. Azithromycin 500 mg | 10 mg/kg | OD | 3–5 days | Oral | If proven/suspected"]),
  ("Recurrent (≥6/yr)",[
   "Tab. Acyclovir 400 mg | 1 tab | BD | 6–12 months | Oral | Or valacyclovir 500 mg BD; continuous suppression",
   "Tab. Dapsone / Azathioprine / Thalidomide | | | | Oral | If antivirals fail"]))

L("Erythema nodosum",R,
  "Find the cause: streptococcal throat (ASO), TB (Mantoux, chest X-ray), sarcoid, IBD, pregnancy/OCP, drugs; in India also ENL (leprosy) to be excluded. Rest, elevate legs, compression stockings.",
  ("First line",[
   "Tab. Ibuprofen 400 mg / Naproxen 250 mg | 1 tab | TDS / BD | 2–3 weeks | Oral | After food",
   "Treat the cause (e.g. penicillin for strep, ATT for TB) | | | | | "]),
  ("Persistent / painful",[
   "Saturated solution of potassium iodide (SSKI) | 300–900 mg/day | TDS | 3–4 weeks | Oral | Check thyroid",
   "Tab. Colchicine 0.5 mg | 1 tab | BD | 4 weeks | Oral | "]),
  ("Severe, after excluding infection",[
   "Tab. Prednisolone 20 mg | 0.5 mg/kg | OD | Taper 2–3 weeks | Oral | Only once TB and other infection excluded"]))

L("Fixed drug eruption",R,
  "Identify and stop the drug (cotrimoxazole, NSAIDs, fluoroquinolones, tetracyclines, paracetamol); give a written drug-allergy card. Oral provocation only under supervision and not after generalised bullous FDE.",
  ("Localised",[
   "Cream Mometasone 0.1% | Thin layer | OD | 1–2 weeks | Topical | ",
   "Tab. Levocetirizine 5 mg | 1 tab | HS | 1 week | Oral | "]),
  ("Generalised bullous FDE",[
   "Manage as for SJS/TEN: admit, supportive care | | | | | ",
   "Cap. Cyclosporine | 3–5 mg/kg/day | BD | 7–10 days | Oral | Or short course of oral steroid"]))

L("Acute generalised exanthematous pustulosis (AGEP)",R,
  "Stop the drug (beta-lactams, macrolides, hydroxychloroquine, terbinafine, diltiazem). Usually resolves in 1–2 weeks. Check CBC, renal and liver function.",
  ("First line",[
   "Cream Mometasone 0.1% | Thin layer | BD | 1 week | Topical | ",
   "Emollients, antipyretics, fluids | | | | | "]),
  ("Severe / systemic involvement",[
   "Tab. Prednisolone 20 mg | 0.5–1 mg/kg | OD | Short taper | Oral | Or cyclosporine short course"]))

L("Stevens–Johnson syndrome / TEN",R,
  "Stop all suspect drugs immediately (allopurinol, carbamazepine, phenytoin, lamotrigine, nevirapine, sulfonamides). Admit — ICU/burns unit if >10% BSA. SCORTEN on day 1 and 3. Barrier nursing, warm room, fluids, nutrition, eye, mouth and genital care daily (ophthalmology review).",
  ("Supportive care + cyclosporine (start early)",[
   "Cap. Cyclosporine 100 mg | 3–5 mg/kg/day | BD | 7–10 days, then taper | Oral | First-line immunomodulator; check creatinine, BP",
   "Liquid paraffin / non-adherent dressings | | BD | Till re-epithelialised | Topical | Leave detached epidermis in place",
   "Eye: lubricant + topical steroid–antibiotic drops | | QID | | Ophthalmic | Daily ophthalmology review",
   "Mouth: chlorhexidine + lignocaine viscous rinse | | QID | | Oral rinse | "]),
  ("If cyclosporine cannot be used / progressing",[
   "Inj. Dexamethasone pulse / IV methylprednisolone | | | 3 days | IV | Early, short; avoid prolonged steroids",
   "Inj. Etanercept 50 mg | 25–50 mg | Single dose (repeat if needed) | | Subcutaneous | Growing evidence"]),
  ("Severe, refractory",[
   "Inj. IVIG | 0.5–1 g/kg/day | OD | 3–4 days | IV | Evidence mixed; costly"]),
  "Give a drug-allergy card; avoid the culprit and related drugs for life; HLA-B*15:02 screening before carbamazepine in at-risk groups.")

H="Hair & nail disorders"
L("Alopecia areata",H,
  "Explain unpredictable course and that hair often regrows. Check thyroid, vitamin D, B12, ferritin if indicated. Score with SALT. Wigs or caps are a valid choice.",
  ("Patchy (<50% scalp)",[
   "Inj. Triamcinolone 10 mg/mL (2.5–5 mg/mL for face) | 0.1 mL per site, 1 cm apart | Every 4–6 weeks | 3–6 months | Intralesional | ",
   "Lotion Clobetasol 0.05% | Few drops | OD | 3 months | Topical | Children, or with intralesional",
   "Solution Minoxidil 5% | 1 mL | BD | 6 months | Topical | Adjunct"]),
  ("Extensive or rapidly progressive",[
   "Tab. Betamethasone / Dexamethasone 5 mg oral mini-pulse | 5 mg | On 2 consecutive days a week | 3–6 months | Oral | Adults; children 2.5 mg",
   "Diphenylcyclopropenone (DPCP) / Squaric acid contact immunotherapy | | Weekly | 6 months | Topical | Specialist centres",
   "Tab. Methotrexate 15–25 mg | | Weekly | 6 months | Oral | ± low-dose prednisolone"]),
  ("Severe (SALT ≥50) / totalis / universalis",[
   "Tab. Baricitinib 4 mg | 1 tab | OD | Long-term | Oral | Approved for severe AA in adults; see Drug safety",
   "Tab. Tofacitinib 5 mg / Cap. Ritlecitinib 50 mg | | BD / OD | | Oral | Ritlecitinib from 12 years",
   "Cap. Cyclosporine / Azathioprine | | | | Oral | Older alternatives"]),
  "Children: topical steroids, minoxidil, intralesional only if cooperative, short-contact anthralin.")

L("Androgenetic alopecia",H,
  "Check iron/ferritin, thyroid, vitamin D; in women look for PCOS (menstrual history, acne, hirsutism). Results need 6 months; stopping treatment loses the gain.",
  ("First line",[
   "Solution Minoxidil 5% (men) / 2–5% (women) | 1 mL | BD (foam OD) | Long-term | Topical | Initial shedding for 4–8 weeks is expected",
   "Men: Tab. Finasteride 1 mg | 1 tab | OD | Long-term | Oral | Discuss sexual adverse effects, mood; not for women of child-bearing age"]),
  ("Add-on / alternatives",[
   "Tab. Minoxidil 2.5 mg (low-dose oral) | 0.625–2.5 mg (women) / 2.5–5 mg (men) | OD | Long-term | Oral | Check BP, pedal oedema, hypertrichosis",
   "Women: Tab. Spironolactone 50–100 mg | | OD | Long-term | Oral | Contraception; potassium if renal disease",
   "Platelet-rich plasma / microneedling | | Monthly | 3–4 sessions | Procedure | "]),
  ("Advanced / stable",[
   "Hair transplantation (FUE / FUT) | | | | Procedure | After 6–12 months of medical therapy",
   "Tab. Dutasteride 0.5 mg | 1 tab | OD | Long-term | Oral | Men; off-label"]))

L("Telogen effluvium",H,
  "Find the trigger 2–3 months earlier: fever (incl. COVID, dengue), childbirth, crash diet, surgery, stress, drugs, thyroid, iron deficiency. Reassure: regrowth in 3–6 months.",
  ("First line",[
   "Correct deficiencies (iron if ferritin <40, vitamin D, B12) | | | 3 months | Oral | ",
   "Adequate protein diet (1 g/kg/day) | | | | | "]),
  ("Chronic (>6 months)",[
   "Solution Minoxidil 2–5% | 1 mL | BD | 6 months | Topical | ",
   "Tab. Minoxidil 1.25 mg (low-dose oral) | | OD | 6 months | Oral | Check BP"]))

L("Paronychia",H,
  "Acute: usually staph — drain if pus. Chronic: wet work, candida, irritants — keep hands dry, gloves with cotton liners, do not push cuticles.",
  ("Acute",[
   "Warm soaks | 15 min | TDS | 3–5 days | | ",
   "Cap. Cephalexin 500 mg / Amoxicillin-clavulanate 625 mg | 1 | QID / BD | 7 days | Oral | Incision and drainage if fluctuant"]),
  ("Chronic",[
   "Cream Clobetasol 0.05% / Mometasone 0.1% | Thin layer | OD | 3–4 weeks | Topical | Anti-inflammatory is the key",
   "Cream Clotrimazole 1% / Lotion Amorolfine | Thin layer | BD | 6 weeks | Topical | Candida",
   "Tab. Fluconazole 150 mg | 1 tab | Weekly | 4–6 weeks | Oral | Resistant candidal"]),
  ("Refractory chronic",[
   "Inj. Triamcinolone into proximal nail fold / en bloc excision of nail fold | | | | Procedure | "]))

L("Trichotillomania",H,
  "Explain, without blame. Habit-reversal therapy / CBT is first line. Look for anxiety, OCD, depression. Children often grow out of it.",
  ("First line",[
   "Habit-reversal therapy / CBT | | Weekly | 8–12 weeks | | Keep a pulling diary, competing response",
   "Tab. N-acetylcysteine 600 mg | 1–2 tabs | BD | 3 months | Oral | Some evidence"]),
  ("With anxiety / OCD",[
   "Tab. Fluoxetine 20 mg | 1 tab | OD | 3–6 months | Oral | With psychiatry input; or clomipramine"]))

L("Twenty-nail dystrophy (trachyonychia)",H,
  "Often benign and self-limiting in children (alopecia areata, LP, psoriasis association). Reassure; nail polish/keep nails short.",
  ("If treatment desired",[
   "Lotion Clobetasol 0.05% | Apply to nail folds | OD | 3–6 months | Topical | ",
   "Inj. Triamcinolone 2.5–5 mg/mL into proximal nail fold | | Monthly | 4–6 sessions | Intralesional | Adults"]),
  ("Treat the associated disease",[
   "Systemic therapy only if associated LP / psoriasis / AA needs it | | | | | "]))

L("Yellow nail syndrome",H,
  "Associated lymphoedema and pleural effusion / bronchiectasis — refer for chest evaluation; screen for malignancy if adult onset.",
  ("First line",[
   "Tab. Vitamin E 400–800 IU | 1 | OD | 6 months | Oral | ",
   "Cap. Itraconazole 100 mg pulse / Fluconazole 150 mg weekly | | | 6 months | Oral | May improve nail growth"]),
  ("Add-on",[
   "Zinc sulphate / clarithromycin (for sinus/lung infection) | | | | Oral | Treat associated conditions"]))

G="Pigmentary disorders"
L("Melasma",G,
  "Daily broad-spectrum sunscreen (SPF 30+, tinted / iron oxide for visible light) every 3 hours outdoors, hat. Stop hormonal pills if possible, avoid irritant cosmetics and steroid creams. Score with MASI. Relapse is common — maintenance needed.",
  ("First line",[
   "Cream Hydroquinone 2% + Tretinoin 0.025% + Fluocinolone 0.01% (Kligman's triple) | Pea-size | HS | 8–12 weeks, then taper | Topical | Not beyond 12 weeks continuously (ochronosis, steroid damage)",
   "Sunscreen SPF 50 (tinted) | | Every 3 h | Long-term | Topical | "]),
  ("Maintenance / add-on",[
   "Cream Azelaic acid 20% / Kojic acid / Cysteamine 5% / Thiamidol | Thin layer | BD | Long-term | Topical | Non-hydroquinone maintenance",
   "Tab. Tranexamic acid 250 mg | 1 tab | BD | 3–6 months | Oral | Exclude clotting history, pregnancy, OCP use, smoking"]),
  ("Refractory",[
   "Chemical peels (glycolic 20–70%, salicylic 20–30%, TCA 10–15%) | | Every 2–3 weeks | 4–6 sessions | Procedure | With priming",
   "Q-switched / picosecond Nd:YAG low-fluence laser | | | | Procedure | Rebound and mottled hypopigmentation risk"]),
  "Pregnancy: sunscreen and azelaic acid only.")

L("Vitiligo",G,
  "Explain the course; counselling and camouflage. Assess activity (VIDA, trichrome/confetti lesions, Koebner) and extent (VASI). Check thyroid. Sunscreen for patches, avoid friction and trauma.",
  ("Limited / stable",[
   "Cream Mometasone 0.1% / Clobetasol 0.05% | Thin layer | OD | 2–3 months (or 2 weeks on, 1 week off) | Topical | Body",
   "Ointment Tacrolimus 0.1% | Thin layer | BD | 6 months | Topical | Face, eyelids, folds, genitals",
   "Cream Ruxolitinib 1.5% (if available) | Thin layer | BD | 6 months | Topical | Non-segmental, ≥12 years"]),
  ("Active / spreading or extensive",[
   "Tab. Betamethasone / Dexamethasone 2.5–5 mg oral mini-pulse | | On 2 consecutive days a week | 3–6 months | Oral | Stops spread",
   "Narrowband UVB (whole body) / targeted excimer | | 2–3×/week | 6–12 months | Phototherapy | Combine with topicals",
   "Tab. Methotrexate 10 mg / Tab. Azathioprine | | Weekly / OD | Months | Oral | Steroid-sparing for active disease"]),
  ("Stable ≥1 year, not responding (segmental, acral)",[
   "Surgery: suction blister / punch / split-thickness graft / non-cultured epidermal cell suspension | | | | Procedure | After 1 year of stability",
   "Tab. Ritlecitinib / Upadacitinib / Baricitinib + NB-UVB | | | | Oral | Emerging; specialist use"]),
  "Children: topical steroids / tacrolimus, NB-UVB; mini-pulse 2.5 mg. Depigmentation (monobenzone) only for >80% involvement.")

L("Lichen planus pigmentosus",G,
  "Avoid triggers: mustard/amla oils, hair dyes, henna, fragrances (patch test), sun. Chronic; partial response. Check hepatitis C, thyroid.",
  ("First line",[
   "Ointment Tacrolimus 0.1% | Thin layer | BD | 3–6 months | Topical | ",
   "Sunscreen SPF 50 | | Every 3 h | Long-term | Topical | ",
   "Cream Azelaic acid 20% / Niacinamide | | BD | Months | Topical | "]),
  ("Active / spreading",[
   "Tab. Betamethasone / Dexamethasone oral mini-pulse 5 mg | | 2 consecutive days a week | 3 months | Oral | ",
   "Tab. Tranexamic acid 250 mg | 1 tab | BD | 3 months | Oral | Some evidence"]),
  ("Refractory",[
   "Low-fluence Q-switched Nd:YAG / chemical peels | | | | Procedure | Limited evidence; post-inflammatory risk"]))

L("Acanthosis nigricans",G,
  "Treat the cause: weight loss and exercise in insulin resistance; screen for diabetes, PCOS, thyroid; sudden extensive or oral/palmar involvement in adults — look for internal malignancy. Stop causative drugs.",
  ("First line",[
   "Cream Tretinoin 0.025–0.05% / Urea 10–20% / Salicylic acid 6% | Thin layer | HS | 3 months | Topical | Neck, axillae; avoid scrubbing",
   "Weight loss + exercise | | | | | Most effective"]),
  ("Add-on",[
   "Tab. Metformin 500 mg | 1 tab | BD | 3–6 months | Oral | If insulin resistance / PCOS confirmed (check renal function)",
   "Chemical peel (TCA 15% / glycolic) / Q-switched laser | | | | Procedure | "]))

L("Freckles (ephelides)",G,
  "Harmless; darken in summer. Sun protection is the main treatment.",
  ("First line",[
   "Sunscreen SPF 50 | | Every 3 h | Long-term | Topical | ",
   "Cream Hydroquinone 2% / Azelaic acid 20% | Thin layer | HS | 2–3 months | Topical | "]),
  ("Cosmetic removal",[
   "Q-switched Nd:YAG 532 nm / picosecond laser / IPL | | | 1–3 sessions | Procedure | Recur without sun protection"]))

L("Lentigo",G,
  "Solar lentigines indicate sun damage; dermoscopy or biopsy for irregular or changing lesions (lentigo maligna).",
  ("First line",[
   "Sunscreen SPF 50 | | Daily | Long-term | Topical | ",
   "Cream Hydroquinone 4% / Tretinoin 0.05% | Thin layer | HS | 3 months | Topical | Partial lightening"]),
  ("Procedural",[
   "Cryotherapy (light freeze) / Q-switched 532 nm / picosecond laser / TCA 25–35% spot peel | | | 1–2 sessions | Procedure | Risk of hypopigmentation in dark skin"]))

L("Idiopathic guttate hypomelanosis",G,
  "Benign, sun-related, age-related. Reassure; sun protection.",
  ("If treatment desired",[
   "Ointment Tacrolimus 0.1% | Thin layer | BD | 3 months | Topical | ",
   "Spot cryotherapy / fractional CO₂ / spot dermabrasion | | | | Procedure | Limited evidence"]),
  ("Alternative",[
   "Cream Tretinoin 0.025% | Thin layer | HS | 3 months | Topical | "]))

L("Pityriasis alba",G,
  "Common in atopic children; reassure — repigments in months. Emollients and sunscreen, avoid harsh soaps.",
  ("First line",[
   "Emollient | | BD | Long-term | Topical | ",
   "Cream Hydrocortisone 1% | Thin layer | OD | 1–2 weeks | Topical | If scaly/inflamed"]),
  ("Persistent",[
   "Ointment Tacrolimus 0.03% / Cream Pimecrolimus 1% | Thin layer | BD | 4–8 weeks | Topical | "]))
