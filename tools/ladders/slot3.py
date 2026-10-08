# Treatment ladders, slot 3: connective tissue, bullous, leprosy & TB, vascular, nutritional, keratinisation,
# tumours, oral, granulomatous, psychocutaneous, benign tumours, selected genodermatoses and nevi.
# Sources: IADVL Textbook (new edition), Rook's 10e, Wolverton 4e, NLEP/WHO, current guidelines. Own wording.
D = []
def L(case, group, general, l1, l2, l3=None, special=""):
    D.append(dict(case=case, group=group, general=general, lines=[x for x in (l1, l2, l3) if x], special=special))

C="Connective tissue diseases"
L("Discoid lupus erythematosus",C,
  "Strict photoprotection (SPF 50, hat, clothing), stop smoking (reduces antimalarial response). Check ANA, CBC, urine for systemic lupus. Treat early to prevent scarring alopecia.",
  ("Localised",[
   "Ointment Clobetasol 0.05% | Thin layer | OD | 4 weeks, then intermittent | Topical | Face: tacrolimus 0.1% BD",
   "Inj. Triamcinolone 10 mg/mL | 0.1 mL per cm² | Every 4–6 weeks | | Intralesional | Thick or scalp lesions"]),
  ("Widespread or scarring",[
   "Tab. Hydroxychloroquine 200 mg | ≤5 mg/kg real body weight | OD–BD | Long-term | Oral | Baseline eye exam, yearly after 5 years (see Drug safety)",
   "Add Tab. Chloroquine 250 mg / quinacrine if partial response | | | | Oral | Do not combine HCQ with chloroquine"]),
  ("Refractory",[
   "Tab. Methotrexate 7.5–25 mg | | Weekly | Months | Oral | ",
   "Cap. Acitretin 25 mg / Isotretinoin / Thalidomide 50–100 mg / Mycophenolate | | | | Oral | Hypertrophic DLE: retinoids; contraception"]))

L("Systemic lupus erythematosus",C,
  "Co-managed with rheumatology/medicine. Assess organ involvement (kidney, blood, CNS). Photoprotection, vitamin D and calcium, vaccinations, contraception counselling. Hydroxychloroquine for all unless contraindicated.",
  ("Skin and mild disease",[
   "Tab. Hydroxychloroquine 200 mg | ≤5 mg/kg | OD–BD | Long-term | Oral | Backbone of therapy",
   "Cream Mometasone 0.1% / Ointment Tacrolimus 0.1% | Thin layer | OD–BD | | Topical | Skin lesions",
   "Tab. Prednisolone 5–10 mg | Lowest effective | OD | Short | Oral | For flares; taper"]),
  ("Moderate (arthritis, serositis, resistant skin)",[
   "Tab. Methotrexate 7.5–15 mg | | Weekly | Months | Oral | ",
   "Tab. Azathioprine 50 mg / Mycophenolate mofetil 1–2 g/day | | | Months | Oral | Steroid-sparing"]),
  ("Severe organ disease (nephritis, CNS, haematological)",[
   "Inj. Methylprednisolone 500–1000 mg pulse × 3 days, then Mycophenolate or Cyclophosphamide (Euro-Lupus) | | | | IV | Specialist care",
   "Inj. Belimumab / Rituximab / Anifrolumab | per label | | | IV/SC | Refractory"]),
  "Pregnancy: continue hydroxychloroquine; azathioprine safe; no mycophenolate, methotrexate, cyclophosphamide. Check anti-Ro (neonatal lupus) and antiphospholipid antibodies.")

L("Dermatomyositis",C,
  "Screen for malignancy in adults (age-appropriate + CT chest/abdomen, CA-125 in women) at diagnosis and yearly for 3 years; check CK, aldolase, LFT, pulmonary function (ILD), myositis antibodies. Strict photoprotection; physiotherapy.",
  ("First line",[
   "Tab. Prednisolone 20 mg | 1 mg/kg | OD | 4–6 weeks then slow taper over 6–12 months | Oral | Calcium, vitamin D, PPI; IV methylprednisolone if severe",
   "Tab. Hydroxychloroquine 200 mg | ≤5 mg/kg | OD | Long-term | Oral | Skin disease; higher drug-rash rate in DM",
   "Ointment Tacrolimus 0.1% / mid-potency steroid | | BD | | Topical | Skin"]),
  ("Steroid-sparing (start early)",[
   "Tab. Methotrexate 15–25 mg | | Weekly | Long-term | Oral | ",
   "Tab. Azathioprine 2 mg/kg / Mycophenolate mofetil 2 g/day | | | | Oral | MMF if ILD"]),
  ("Refractory / severe",[
   "Inj. IVIG | 2 g/kg | Over 2–5 days, monthly | 3–6 months | IV | Effective for skin and muscle",
   "Inj. Rituximab / Tab. Tofacitinib | per label | | | IV/Oral | "]),
  "Juvenile DM: steroids + methotrexate early; watch for calcinosis.")

L("Systemic sclerosis (scleroderma)",C,
  "Co-managed with rheumatology. Screen yearly: lungs (PFT, HRCT), heart (echo for pulmonary hypertension), kidneys (BP — renal crisis; avoid high-dose steroids >15 mg). Keep warm, stop smoking, emollients, physiotherapy for hands and mouth.",
  ("Raynaud's / digital ulcers",[
   "Tab. Nifedipine SR 10–20 mg / Amlodipine 5–10 mg | | OD–BD | Long-term | Oral | Warm gloves, avoid cold, beta-blockers",
   "Tab. Sildenafil 20 mg / Tadalafil 10–20 mg | | TDS / OD | | Oral | Digital ulcers; or IV iloprost; bosentan prevents new ulcers"]),
  ("Skin thickening (early diffuse)",[
   "Tab. Methotrexate 15–25 mg | | Weekly | | Oral | ",
   "Tab. Mycophenolate mofetil 500 mg | 1–1.5 g | BD | Long-term | Oral | Preferred if lung disease"]),
  ("Progressive / organ disease",[
   "Inj. Cyclophosphamide / Rituximab / Tab. Nintedanib (ILD) | | | | IV/Oral | Specialist",
   "Autologous stem-cell transplant | | | | | Selected rapidly progressive diffuse disease"]),
  "GI reflux: PPI. Renal crisis: ACE inhibitor (captopril) urgently.")

L("Morphea (localised scleroderma)",C,
  "Assess activity (erythema, new lesions) vs damage. Linear morphea on face/limb in children needs early systemic treatment (growth, joint, eye, brain involvement). Physiotherapy for contractures.",
  ("Limited plaque, active",[
   "Ointment Clobetasol 0.05% / Tacrolimus 0.1% | Thin layer | OD–BD | 3 months | Topical | ",
   "Calcipotriol 0.005% ointment | | BD | 3 months | Topical | Alone or with steroid"]),
  ("Generalised plaque",[
   "UVA1 / PUVA / NB-UVB | | 3–4×/week | 2–3 months | Phototherapy | ",
   "Tab. Methotrexate 15 mg/m² (child) or 15–25 mg (adult) | | Weekly | 1–2 years | Oral | "]),
  ("Linear / deep / pansclerotic",[
   "Tab. Methotrexate weekly + Tab. Prednisolone 0.5–1 mg/kg (or IV methylprednisolone pulses) | | | Steroid 3 months | Oral/IV | Standard combination",
   "Mycophenolate mofetil | 1–2 g/day | BD | | Oral | If methotrexate fails"]))

L("Parry–Romberg syndrome",C,
  "Progressive hemifacial atrophy; check eye and brain (MRI, seizures). Treat while active; reconstruct once stable 1–2 years.",
  ("Active disease",[
   "Tab. Methotrexate 15 mg/m² (child) / 15–25 mg | | Weekly | 1–2 years | Oral | With oral or pulse steroid initially (as for linear morphea)"]),
  ("Stable – reconstruction",[
   "Autologous fat grafting / dermal fillers (hyaluronic acid) / flaps | | | | Procedure | After 1–2 years without progression"]))

L("Lichen sclerosus et atrophicus",C,
  "Genital LS: lifelong follow-up (SCC risk, especially vulvar). Soap substitute, emollient, avoid irritants. Circumcision in men with phimosis.",
  ("First line",[
   "Ointment Clobetasol 0.05% | Thin layer (fingertip unit for genital area per month as a guide) | OD | 3 months (OD 1 month, alternate days 1 month, twice weekly 1 month) | Topical | Then maintenance 1–2×/week",
   "Emollient / petrolatum | | | Long-term | Topical | "]),
  ("Not responding",[
   "Ointment Tacrolimus 0.1% | Thin layer | BD | 3 months | Topical | Second line",
   "Inj. Triamcinolone 10 mg/mL | | Monthly | | Intralesional | Hypertrophic areas"]),
  ("Refractory",[
   "Cap. Acitretin 25 mg / Methotrexate | | | | Oral | Extragenital extensive",
   "Surgery for complications (adhesions, meatal stenosis, circumcision) | | | | Procedure | Not a cure"]))

L("Striae distensae",C,
  "Early red striae respond better than white ones. Treatment improves, does not erase.",
  ("Early (red)",[
   "Cream Tretinoin 0.05–0.1% | Thin layer | HS | 3–6 months | Topical | Not in pregnancy",
   "Pulsed dye laser / IPL | | Monthly | 3–4 sessions | Procedure | "]),
  ("Mature (white)",[
   "Fractional CO₂ / Er:YAG laser / microneedling ± PRP / radiofrequency | | Monthly | 3–6 sessions | Procedure | "]),
  special="Pregnancy: emollients only (hyaluronic acid, centella); evidence for prevention is weak.")

V="Vesicobullous diseases"
L("Vesicobullous diseases (pemphigus / pemphigoid)",V,
  "Confirm with biopsy + DIF (and ELISA for Dsg1/Dsg3, BP180/230). Score PDAI/BPDAI. Wound care, oral hygiene, nutrition; screen TB, hepatitis B, diabetes, bone health; PPI, calcium + vitamin D with steroids.",
  ("Pemphigus – first line",[
   "Inj. Rituximab | 1 g IV, repeat after 2 weeks (RA protocol) | | Maintenance 500 mg at 6 and 12 months if needed | IV | First-line in moderate–severe pemphigus",
   "Tab. Prednisolone 20 mg | 0.5–1 mg/kg | OD | Taper over 3–6 months | Oral | With rituximab"]),
  ("Pemphigus – steroid-sparing / no rituximab",[
   "Tab. Azathioprine 50 mg | 2–2.5 mg/kg (TPMT) | OD | Long-term | Oral | ",
   "Tab. Mycophenolate mofetil 500 mg | 2–3 g/day | BD | Long-term | Oral | ",
   "Dexamethasone–cyclophosphamide pulse (DCP) | | Monthly | | IV | Indian regimen, still used where rituximab is not affordable"]),
  ("Refractory",[
   "Inj. IVIG 2 g/kg / Immunoadsorption / repeat rituximab | | | | IV | "]),
  "Bullous pemphigoid: Ointment Clobetasol 0.05% whole body (≤40 g/day, taper over 4 months) is first line; oral prednisolone 0.5 mg/kg if extensive; doxycycline 200 mg/day + nicotinamide as steroid-sparing; methotrexate, dupilumab or omalizumab if refractory. Stop DPP-4 inhibitors (gliptins).")

M="Leprosy & mycobacterial"
L("Hansen's disease (leprosy)",M,
  "Notify; counsel (curable, not hereditary, stop discrimination). Examine contacts — single-dose rifampicin chemoprophylaxis for contacts per NLEP. Nerve function assessment at every visit; self-care for anaesthetic hands and feet. Check G6PD before dapsone if possible.",
  ("Multidrug therapy (uniform 3-drug MDT, NLEP/WHO)",[
   "Rifampicin 600 mg | 600 mg | Once a month, supervised | PB 6 months / MB 12 months | Oral | Urine turns orange",
   "Clofazimine | 300 mg once a month supervised + 50 mg | Daily | PB 6 months / MB 12 months | Oral | Skin darkening, reversible",
   "Dapsone 100 mg | 100 mg | Daily | PB 6 months / MB 12 months | Oral | Watch for anaemia, hepatitis, DRESS"]),
  ("Reactions",[
   "Type 1 (reversal): Tab. Prednisolone 40 mg | 0.5–1 mg/kg | OD | Taper over 12–20 weeks | Oral | Continue MDT",
   "Type 2 (ENL): Tab. Prednisolone 40 mg + Clofazimine 300 mg/day | | | Prednisolone 12 weeks; clofazimine up to 12 months tapering | Oral | Thalidomide 100–400 mg/day if steroid-dependent (men, women not of child-bearing potential)"]),
  ("Rifampicin resistance / intolerance",[
   "Ofloxacin 400 mg + Minocycline 100 mg + Clofazimine 50 mg | | Daily | 6 months, then clofazimine + one of them for 18 months | Oral | Specialist / NLEP referral"]),
  "Children 10–14 yr: rifampicin 450 mg monthly, clofazimine 150 mg monthly + 50 mg alternate days, dapsone 50 mg daily; under 10 yr: dose by weight (see NLEP chart / Dose by weight).")

L("Cutaneous tuberculosis",M,
  "Confirm (biopsy, culture/GeneXpert, IGRA/Mantoux); look for systemic TB (chest X-ray). Notify (Nikshay), HIV test, treat under NTEP with daily fixed-dose combinations.",
  ("Drug-sensitive TB (NTEP)",[
   "Intensive phase: Isoniazid + Rifampicin + Pyrazinamide + Ethambutol (FDC) | by weight band | Daily | 2 months | Oral | ",
   "Continuation phase: Isoniazid + Rifampicin + Ethambutol | by weight band | Daily | 4 months (extend to 9–12 for extensive / bone) | Oral | Pyridoxine 10–25 mg/day"]),
  ("Response check / drug resistance",[
   "Reassess at 2 months; if no response — repeat biopsy, culture with sensitivity, GeneXpert for rifampicin resistance | | | | | Refer to DR-TB centre"]),
  special="Tuberculids (lichen scrofulosorum, papulonecrotic): full ATT for underlying focus. Scrofuloderma/lupus vulgaris may need surgery after ATT for deformity.")

VS="Vascular & ulcers"
L("Leg ulcers",VS,
  "Find the type: venous (ABPI ≥0.8 before compression), arterial, neuropathic (diabetes, leprosy), vasculitic, pyoderma gangrenosum, infection, malignancy (biopsy non-healing). Leg elevation, walking, weight loss, nutrition, control diabetes.",
  ("Venous ulcer",[
   "Compression bandaging (4-layer / short-stretch) | | Change weekly | Till healed, then stockings | | Only if ABPI ≥0.8",
   "Non-adherent dressing / hydrocolloid; Potassium permanganate soaks for exudate | | | | Topical | Avoid topical antibiotics/neomycin (sensitisation)",
   "Tab. Pentoxifylline 400 mg | 1 tab | TDS | 6 months | Oral | Speeds healing with compression"]),
  ("Infected or slow",[
   "Systemic antibiotic only if cellulitis (per culture) | | | | Oral | ",
   "Topical steroid to surrounding stasis eczema | | | | Topical | "]),
  ("Not healing in 12 weeks",[
   "Biopsy edge; Doppler and venous surgery / endovenous ablation | | | | Procedure | ",
   "Split-skin / punch grafting, NPWT | | | | Procedure | "]))

L("Infantile haemangioma & vascular malformations",VS,
  "Most infantile haemangiomas involute; treat early (first 5 months is the proliferation window) if risk: periocular, airway (beard area), lip, nasal tip, large facial (PHACE — echo, MRI brain), ulcerated, multiple (>5 — liver ultrasound). Vascular malformations do not involute.",
  ("Small, superficial, low-risk",[
   "Timolol 0.5% gel-forming drops | 1 drop | BD | 6 months | Topical | Thin superficial lesions",
   "Watchful waiting with photographs | | | | | "]),
  ("Problematic haemangioma",[
   "Syp. Propranolol | 1 mg/kg/day → 2–3 mg/kg/day in 2 doses | BD | Till 12–18 months of age | Oral | Give with feeds; hold if not eating (hypoglycaemia); check HR, BP at start",
   "Ulcer care: barrier dressings, topical antibiotic, pain relief | | | | Topical | "]),
  ("Not responding / malformations",[
   "Pulsed dye laser (port-wine stain, residual telangiectasia) | | Every 4–8 weeks | | Procedure | Port-wine stain: start in infancy",
   "Oral prednisolone 2–3 mg/kg / Sirolimus (lymphatic & complex malformations) / sclerotherapy / surgery | | | | | Specialist"]))

L("Henoch–Schönlein purpura (IgA vasculitis)",VS,
  "Mostly self-limiting in children. Urine dipstick and BP at every visit for 6 months (nephritis). Rest, leg elevation.",
  ("Skin + joints",[
   "Tab. Paracetamol / Ibuprofen | | | As needed | Oral | Avoid NSAIDs if renal involvement",
   "Rest, elevation | | | | | "]),
  ("Severe abdominal pain, scrotal or extensive skin necrosis",[
   "Tab. Prednisolone 20 mg | 1–2 mg/kg | OD | 2 weeks, taper | Oral | Does not prevent nephritis",
   "Tab. Dapsone 50–100 mg / Colchicine 0.5 mg BD | | | | Oral | Persistent skin disease"]),
  ("Nephritis",[
   "Nephrology: steroids ± mycophenolate / cyclophosphamide; ACE inhibitor for proteinuria | | | | | "]))

L("Lipodermatosclerosis",VS,
  "Sign of chronic venous insufficiency. Compression is essential once acute pain settles; venous duplex.",
  ("First line",[
   "Compression stockings (class II, 20–30 mmHg) | | Daily | Long-term | | ",
   "Tab. Pentoxifylline 400 mg | 1 tab | TDS | 3–6 months | Oral | "]),
  ("Acute painful / refractory",[
   "Tab. Stanozolol / Danazol 200 mg | | BD | 2–3 months | Oral | Androgens; monitor liver, lipids",
   "Venous ablation / surgery | | | | Procedure | "]))

L("Pigmented purpuric dermatosis",VS,
  "Benign and chronic; look for venous insufficiency, drugs (paracetamol, aspirin), contact allergy (dyes, rubber). Compression if on legs.",
  ("First line",[
   "Cream Mometasone 0.1% | Thin layer | OD | 4 weeks | Topical | Itch",
   "Tab. Rutoside 50 mg + Ascorbic acid 500 mg | 1 each | BD | 3 months | Oral | Capillary-stabilising"]),
  ("Extensive",[
   "Narrowband UVB / PUVA | | 3×/week | 2–3 months | Phototherapy | ",
   "Tab. Pentoxifylline 400 mg | 1 tab | TDS | 2–3 months | Oral | "]))

L("Pyogenic granuloma (lobular capillary haemangioma)",VS,
  "Bleeds easily; send for histology. Check for causes: pregnancy, isotretinoin, ingrown nail, drugs (EGFR inhibitors).",
  ("Small",[
   "Timolol 0.5% drops / Imiquimod 5% cream | | BD | 4–6 weeks | Topical | Small lesions, children",
   "Silver nitrate cautery | | | | Procedure | "]),
  ("Standard",[
   "Shave excision + electrocautery / curettage of base | | Once | | Procedure | Low recurrence",
   "Full-thickness excision / pulsed dye laser / Nd:YAG | | | | Procedure | Recurrent lesions"]),
  special="Pregnancy: often regresses after delivery — treat only if bleeding.")

N="Nutritional & metabolic"
L("Pellagra",N,
  "Look for cause: alcoholism, maize/jowar diet, malabsorption, isoniazid, carcinoid, Hartnup. Sun protection; high-protein diet; also give B-complex (other deficiencies coexist).",
  ("Treatment",[
   "Tab. Nicotinamide 100 mg | 100 mg | TDS (QID if severe) | Till symptoms resolve (2–4 weeks), then 50 mg BD | Oral | Prefer nicotinamide — no flushing",
   "Tab. Vitamin B-complex + zinc | 1 | OD | 3 months | Oral | "]),
  ("Severe / neurological",[
   "Admit; parenteral nicotinamide + fluids | | | | IV | Dementia, diarrhoea"]))

L("Macular and lichen amyloidosis",N,
  "Stop friction (nylon scrubs, towels); treat itch. Chronic; partial response.",
  ("First line",[
   "Ointment Clobetasol 0.05% under occlusion / Tacrolimus 0.1% | Thin layer | OD | 4–8 weeks | Topical | ",
   "Tab. Levocetirizine 5 mg / Hydroxyzine 25 mg | | HS | | Oral | "]),
  ("Lichen amyloidosis (thick)",[
   "Cap. Acitretin 25 mg | 0.5 mg/kg | OD | 3 months | Oral | Contraception",
   "Salicylic acid / urea / DMSO / calcipotriol topical; NB-UVB / PUVA | | | | | "]),
  ("Refractory",[
   "Dermabrasion / fractional CO₂ / Q-switched Nd:YAG | | | | Procedure | "]))

L("Phrynoderma",N,
  "Vitamin A and EFA deficiency (often with other nutritional deficiencies). Dietary counselling (green leafy vegetables, carrot, papaya, milk, eggs). Check night blindness, Bitot's spots.",
  ("Treatment",[
   "Vitamin A 2,00,000 IU (≥1 yr; 1,00,000 IU 6–12 months) | | Day 1, 2 and 14 (if eye signs) | | Oral | NOT in pregnancy (use 10,000 IU daily)",
   "Cream Urea 10% / Salicylic acid 3% | Thin layer | BD | 4–8 weeks | Topical | "]),
  ("Add-on",[
   "Tab. Vitamin B-complex + Vitamin E + Zinc | | OD | 3 months | Oral | "]))

L("Xanthomas",N,
  "Fasting lipid profile, sugar, thyroid, liver and renal function (secondary causes). Treat the lipid disorder with physician; diet, exercise, weight loss.",
  ("Treat the lipid disorder",[
   "Tab. Atorvastatin 10–40 mg / Rosuvastatin 5–20 mg | | HS | Long-term | Oral | Hypercholesterolaemia",
   "Tab. Fenofibrate 145–160 mg | | OD | | Oral | Hypertriglyceridaemia (eruptive xanthomas)"]),
  ("Persistent lesions (xanthelasma, tuberous)",[
   "TCA 35–50% / Q-switched or CO₂ / Er:YAG laser / surgical excision | | | | Procedure | Recurrence common"]))

K="Disorders of keratinisation"
L("Ichthyosis",K,
  "Daily bath then emollient within 3 minutes; humidify; avoid hot water and soaps. Collodion baby: incubator humidity, emollient, watch hypernatraemia and infection.",
  ("First line",[
   "Emollient (white soft paraffin / liquid paraffin) | Liberal | BD–TDS | Lifelong | Topical | ",
   "Cream Urea 10% / Lactic acid 12% / Propylene glycol 40–60% | Thin layer | BD | Long-term | Topical | Not urea on infants' broken skin"]),
  ("Thick scale",[
   "Salicylic acid 3–6% ointment | | OD | | Topical | Limit area in children (salicylism)",
   "Cream Tretinoin 0.025% / Tazarotene 0.05% | | HS | | Topical | Small areas"]),
  ("Severe (lamellar, epidermolytic, Harlequin)",[
   "Cap. Acitretin 10–25 mg | 0.3–0.5 mg/kg | OD | Long-term, lowest dose | Oral | Monitor growth, lipids, LFT; contraception"]))

L("Keratosis pilaris",K,
  "Harmless and improves with age; soap substitute, avoid scrubbing hard.",
  ("First line",[
   "Cream Urea 10–20% / Lactic acid 12% / Salicylic acid 3% | Thin layer | BD | 2–3 months | Topical | Maintenance needed"]),
  ("Persistent",[
   "Cream Tretinoin 0.025% / Adapalene 0.1% | Thin layer | HS | 2–3 months | Topical | ",
   "Erythema: pulsed dye laser / IPL | | | | Procedure | "]))

L("Lichen spinulosus",K,
  "Often self-limiting in children; associated with atopy.",
  ("First line",[
   "Salicylic acid 3–6% / Urea 10–20% / Lactic acid 12% | Thin layer | BD | 4–8 weeks | Topical | "]),
  ("Persistent",[
   "Cream Tretinoin 0.025% / mild topical steroid | | HS | 4 weeks | Topical | "]))

L("Palmoplantar keratoderma",K,
  "Classify: hereditary vs acquired (eczema, psoriasis, tinea, hypothyroidism, arsenic, malignancy). Treat the cause; regular paring, comfortable footwear, treat fungal infection.",
  ("First line",[
   "Salicylic acid 6–12% / Urea 20–40% ointment under occlusion | | HS | Long-term | Topical | ",
   "Mechanical paring / pumice after soaking | | Weekly | | | "]),
  ("Thick / painful",[
   "Cap. Acitretin 10–25 mg | Low dose | OD | Long-term | Oral | Contraception; low dose (blistering in epidermolytic PPK)",
   "Topical retinoid / calcipotriol | | | | Topical | Psoriasiform types"]))

L("Porokeratosis",K,
  "Sun protection; follow-up — small risk of SCC (higher in linear and large lesions). Check immunosuppression.",
  ("First line",[
   "Cream 5-fluorouracil 5% / Imiquimod 5% | Thin layer | OD | 4–6 weeks | Topical | ",
   "Calcipotriol / Tretinoin / Diclofenac 3% gel | | BD | 3 months | Topical | DSAP"]),
  ("Limited lesions",[
   "Cryotherapy / CO₂ laser / excision | | | | Procedure | "]),
  ("Extensive",[
   "Cap. Acitretin 25 mg | | OD | Months | Oral | Recurrence after stopping",
   "Topical 2% lovastatin + 2% cholesterol | | BD | 3 months | Topical | Compounded; newer pathogenesis-based"]))

L("Callus (callosity)",K,
  "Remove pressure and friction: footwear, insoles, gloves; correct foot deformity (podiatry). Diabetics/leprosy: careful — no self-paring.",
  ("First line",[
   "Salicylic acid 20–40% plaster / 12% ointment | | HS | 2–4 weeks | Topical | Not in diabetes or poor circulation",
   "Cream Urea 40% | Thin layer | BD | | Topical | "]),
  ("Persistent",[
   "Paring by doctor / podiatrist | | Every 4–6 weeks | | Procedure | "]))

L("Corn (clavus)",K,
  "Find and remove pressure point: footwear, toe spacers, padding; X-ray for bony prominence if recurrent.",
  ("First line",[
   "Salicylic acid 40% plaster | | Every 48 h after soaking | 2 weeks | Topical | Not in diabetes or neuropathy",
   "Paring / enucleation of core | | | | Procedure | "]),
  ("Recurrent",[
   "Surgical correction of bony prominence (orthopaedics) | | | | Procedure | "]))

T="Premalignant & malignant tumours"
L("Actinic keratosis",T,
  "Strict sun protection; examine whole skin; biopsy thick, tender or rapidly growing lesions (SCC). Immunosuppressed: closer follow-up.",
  ("Single / few lesions",[
   "Cryotherapy | 1 freeze–thaw | Once | Repeat in 4–6 weeks | Procedure | ",
   "Curettage and cautery | | | | Procedure | Hypertrophic"]),
  ("Field (many lesions)",[
   "Cream 5-fluorouracil 5% | Thin layer | BD | 3–4 weeks | Topical | Expect inflammation",
   "Cream Imiquimod 5% / 3.75% | Thin layer | 2–3×/week | 4–16 weeks | Topical | "]),
  ("Refractory / extensive",[
   "Photodynamic therapy (ALA / MAL) | | | 1–2 sessions | Procedure | ",
   "Tab. Nicotinamide 500 mg | 1 tab | BD | Long-term | Oral | Reduces new keratinocyte cancers in high-risk"]))

L("Basal cell carcinoma",T,
  "Biopsy; classify low vs high risk (site H-zone, size, aggressive subtype, recurrence). Sun protection, full-skin check yearly. Tumour board for advanced cases.",
  ("Standard",[
   "Surgical excision with 4 mm margins | | | | Procedure | Low-risk BCC",
   "Mohs micrographic surgery | | | | Procedure | High-risk / H-zone / recurrent"]),
  ("Superficial / low-risk, or not fit for surgery",[
   "Cream Imiquimod 5% | Thin layer | 5×/week | 6 weeks | Topical | Superficial BCC",
   "Cream 5-FU 5% / PDT / curettage-cautery / cryosurgery / radiotherapy | | | | | "]),
  ("Locally advanced / metastatic",[
   "Cap. Vismodegib 150 mg / Sonidegib 200 mg | 1 | OD | | Oral | Hedgehog inhibitor; contraception (see Drug safety)",
   "Inj. Cemiplimab | per label | | | IV | After hedgehog-inhibitor failure"]))

L("Squamous cell carcinoma",T,
  "Biopsy; stage; examine regional lymph nodes; ultrasound/CT if high risk. In India also consider arsenic, chronic scars/ulcers (Marjolin), HPV. Oncology/surgery co-management.",
  ("Standard",[
   "Surgical excision with 4–6 mm margins (≥6 mm high-risk) | | | | Procedure | Mohs for high-risk sites",
   "SCC in situ (Bowen's): 5-FU / imiquimod / PDT / cryotherapy / curettage | | | | | "]),
  ("Not fit for surgery / adjuvant",[
   "Radiotherapy | | | | | Perineural invasion, positive margins, elderly"]),
  ("Advanced / metastatic",[
   "Inj. Cemiplimab / Pembrolizumab | per label | | | IV | Immunotherapy first line",
   "Cetuximab / platinum chemotherapy | | | | IV | "]))

L("Recurrent aphthous stomatitis","Oral & mucosal disorders",
  "Check CBC, iron, B12, folate, coeliac screen if frequent; ask about genital ulcers, eye symptoms (Behçet's), HIV. Avoid trauma, spicy/acidic foods, SLS toothpaste.",
  ("Minor RAS",[
   "Triamcinolone 0.1% in orabase / Clobetasol 0.05% gel | Thin layer on ulcer | TDS–QID | 5–7 days | Oral mucosa | ",
   "Chlorhexidine 0.2% mouthwash + Benzydamine / lignocaine gel | 10 mL | BD–TDS | 1–2 weeks | Oral rinse | "]),
  ("Frequent or major RAS",[
   "Tab. Colchicine 0.5 mg | 1 tab | BD | 3 months | Oral | ",
   "Tab. Dapsone 50–100 mg / Pentoxifylline 400 mg TDS | | | 3 months | Oral | ",
   "Tab. Prednisolone 20–40 mg | | OD | 5–7 days | Oral | Major aphthae, short course"]),
  ("Refractory / Behçet's",[
   "Tab. Apremilast 30 mg BD / Tab. Thalidomide 100 mg | | | | Oral | Apremilast for Behçet's oral ulcers; thalidomide with strict pregnancy prevention"]))

L("Granuloma annulare","Granulomatous disorders",
  "Localised GA often clears in 2 years — reassure. Generalised: check sugar, lipids, thyroid; HIV/hepatitis if risk factors.",
  ("Localised",[
   "Ointment Clobetasol 0.05% under occlusion | Thin layer | OD | 4–8 weeks | Topical | ",
   "Inj. Triamcinolone 2.5–5 mg/mL | 0.1 mL per site | Every 4–6 weeks | | Intralesional | ",
   "Cryotherapy | | | | Procedure | "]),
  ("Generalised",[
   "Narrowband UVB / PUVA | | 3×/week | 3 months | Phototherapy | ",
   "Tab. Hydroxychloroquine 200 mg | 1 tab | BD | 3–6 months | Oral | Or dapsone 100 mg; doxycycline"]),
  ("Refractory",[
   "Isotretinoin / Methotrexate / Tofacitinib / TNF inhibitors | | | | Oral/SC | Limited evidence"]))

L("Dermatitis artefacta","Psychocutaneous disorders",
  "Non-confrontational, supportive approach; build trust and see regularly. Do not accuse. Involve psychiatry when the patient accepts. Look for stressors, depression, personality disorder, abuse.",
  ("Skin care",[
   "Occlusive dressings / zinc paste bandage | | | Weekly | Topical | Protects and allows healing",
   "Mupirocin 2% for secondary infection | | BD | 1 week | Topical | "]),
  ("Psychological",[
   "Tab. Fluoxetine 20 mg / Sertraline 50 mg | 1 tab | OD | 6 months | Oral | With psychiatry; for associated depression/anxiety",
   "Low-dose atypical antipsychotic (e.g. aripiprazole) | | | | Oral | Psychiatrist-led"]))

B="Benign tumours & cysts"
L("Keloid and hypertrophic scar",B,
  "Prevent: avoid elective surgery/piercing in keloid-prone patients, silicone after wounds. Combination treatment works best; recurrence common.",
  ("First line",[
   "Inj. Triamcinolone 10–40 mg/mL | 0.1–0.2 mL per cm | Every 3–4 weeks | 4–6 sessions | Intralesional | Atrophy, hypopigmentation, telangiectasia",
   "Silicone gel / sheet | | 12–24 h a day | 3–6 months | Topical | Pressure garments for burn scars"]),
  ("Add-on",[
   "Inj. 5-fluorouracil 50 mg/mL (+ triamcinolone) | | Weekly–monthly | | Intralesional | Not in pregnancy",
   "Cryotherapy (intralesional / contact) + steroid | | | | Procedure | "]),
  ("Refractory / large",[
   "Excision + immediate post-op radiotherapy or intralesional steroid | | | | Procedure | Never excise alone",
   "Pulsed dye / fractional laser, botulinum toxin, verapamil IL | | | | | "]))

L("Seborrhoeic keratosis",B,
  "Benign; reassure. Sudden eruption of many (Leser–Trélat) needs check for internal malignancy. Biopsy atypical lesions.",
  ("Cosmetic removal",[
   "Cryotherapy / curettage / shave removal | | Once | | Procedure | ",
   "Radiofrequency / electrocautery / CO₂ laser | | | | Procedure | DPN in dark skin: fine-tip electrodesiccation"]),
  ("Topical (limited evidence)",[
   "Hydrogen peroxide 40% / Tazarotene 0.1% | | | | Topical | "]))

L("Milium / colloid milium",B,
  "Primary milia in infants clear by themselves. Secondary milia follow blistering, steroid damage, trauma.",
  ("Milia",[
   "Extraction with needle / comedone extractor | | Once | | Procedure | ",
   "Cream Tretinoin 0.025% / Adapalene 0.1% | | HS | 2–3 months | Topical | Many lesions"]),
  ("Colloid milium",[
   "Sun protection; dermabrasion / CO₂ or Er:YAG laser | | | | Procedure | Limited evidence"]))

L("Sebaceous hyperplasia",B,
  "Benign; dermoscopy distinguishes from BCC. Treatment is cosmetic.",
  ("Cosmetic",[
   "Electrocautery / radiofrequency (fine needle) / CO₂ laser | | | 1–2 sessions | Procedure | ",
   "TCA 35–50% spot application / cryotherapy | | | | Procedure | "]),
  ("Many lesions",[
   "Cream Tretinoin 0.05% / Adapalene 0.1% | | HS | 3 months | Topical | Partial response"]))

G="Genodermatoses"
L("Darier's disease",G,
  "Avoid heat, sweating, sunburn, friction; cotton clothes. Treat secondary bacterial/HSV infection promptly. Genetic counselling (autosomal dominant).",
  ("Mild",[
   "Emollient + Cream Tretinoin 0.025% / Adapalene 0.1% | | HS | | Topical | Irritation common; alternate nights",
   "Cream Mometasone 0.1% + antiseptic | | OD | Flares | Topical | "]),
  ("Moderate–severe",[
   "Cap. Acitretin 10–25 mg | 0.2–0.5 mg/kg | OD | Long-term | Oral | Contraception for 3 years after; or isotretinoin in women"]),
  ("Refractory",[
   "Cap. Cyclosporine / CO₂ laser / dermabrasion (localised) | | | | | "]))

L("Hailey–Hailey disease",G,
  "Reduce sweating and friction (weight loss, cotton, keep folds dry); treat infection (bacterial, candida, HSV).",
  ("Flares",[
   "Cream Mometasone 0.1% + Clotrimazole / Fusidic acid | | BD | 2 weeks | Topical | ",
   "Cap. Doxycycline 100 mg | 1 cap | BD | 4 weeks | Oral | "]),
  ("Chronic / recurrent",[
   "Ointment Tacrolimus 0.1% | | BD | | Topical | ",
   "Botulinum toxin A to folds (reduces sweating) | | Every 4–6 months | | Intradermal | "]),
  ("Refractory",[
   "CO₂ / Er:YAG laser, dermabrasion / Tab. Naltrexone 4.5 mg (low dose) | | | | | Low-dose naltrexone: case series"]))

L("Tuberous sclerosis complex",G,
  "Multidisciplinary (neurology, renal, eye, cardiology); surveillance per international guidelines; genetic counselling.",
  ("Facial angiofibromas",[
   "Sirolimus 0.2–1% topical gel / ointment | Thin layer | OD–BD | Long-term | Topical | Best started early in childhood; relapse on stopping",
   "Sun protection | | | | Topical | "]),
  ("Established angiofibromas",[
   "CO₂ / pulsed dye laser, shave, electrocautery | | | | Procedure | Combine with topical sirolimus afterwards"]),
  special="Systemic everolimus (specialist) for SEGA, renal angiomyolipoma, seizures — skin lesions also improve.")

L("Xeroderma pigmentosum",G,
  "Strict lifelong UV protection: avoid daylight outdoors, UV-blocking clothing, visors, window films, SPF 50+; vitamin D supplements. Skin and eye checks every 3–6 months. Genetic counselling.",
  ("Prevention",[
   "Sunscreen SPF 50+ broad spectrum | | Every 2 h | Lifelong | Topical | ",
   "Tab. Nicotinamide 500 mg | 1 tab | BD | Long-term | Oral | Reduces new skin cancers (adults; limited data in XP)"]),
  ("Premalignant lesions",[
   "Cryotherapy / 5-FU / Imiquimod | | | | Topical/Procedure | AKs"]),
  ("Skin cancers",[
   "Excision / Mohs; oral retinoid (acitretin / isotretinoin) chemoprevention | | | | | Specialist"]))

NV="Nevi & hamartomas"
L("Nevus of Ota / Ito / Hori",NV,
  "Check eye pressure (glaucoma) and eye pigmentation in nevus of Ota. Explain several sessions are needed; start earlier for better results.",
  ("Treatment",[
   "Q-switched Nd:YAG 1064 nm / picosecond laser | | Every 6–8 weeks | 5–10 sessions | Procedure | Risk of PIH; sun protection",
   "Camouflage cosmetics | | | | Topical | "]),
  ("Hori's nevus",[
   "Q-switched Nd:YAG 1064 nm (± prior hydroquinone priming) | | | Several sessions | Procedure | "]))
