# Treatment ladders, slot 1: acne & appendageal, bacterial, fungal, infestations, viral, STI.
# Drafted from Wolverton 4e (2020) and standard Indian practice; to be cross-checked with IADVL / Rook's.
# Each rx line: "Drug | dose | freq | duration | route | note"
D = []
def L(case, group, general, l1, l2, l3=None, special=""):
    D.append(dict(case=case, group=group, general=general, lines=[x for x in (l1, l2, l3) if x], special=special))

# ---------------- Acne & appendageal ----------------
L("Acne vulgaris","Acne & appendageal disorders",
  "Gentle non-comedogenic cleanser twice daily, oil-free moisturiser and sunscreen. Do not squeeze lesions. Topicals take 8–12 weeks to work.",
  ("Mild–moderate (comedones, papulopustules)",[
   "Gel Adapalene 0.1% + Benzoyl peroxide 2.5% | Pea-size | HS | 12 weeks | Topical | Whole face, not just spots",
   "Gel Clindamycin 1% | Thin layer | Morning | 12 weeks | Topical | Always with benzoyl peroxide; avoid antibiotic alone"]),
  ("Moderate–severe papulopustular / truncal",[
   "Cap. Doxycycline 100 mg | 1 cap | OD | 8–12 weeks | Oral | After food with water, stay upright 30 min; with a topical retinoid + BPO",
   "Gel Adapalene 0.1% + Benzoyl peroxide 2.5% | Pea-size | HS | 12 weeks | Topical | Continue as maintenance after antibiotic"]),
  ("Severe nodulocystic, scarring or failed oral antibiotic",[
   "Cap. Isotretinoin 20 mg | 0.25–0.5 mg/kg | OD | Till 120–150 mg/kg cumulative | Oral | After a fatty meal; pregnancy test, LFT, lipids at baseline; strict contraception",
   "Women with hormonal features: Tab. Spironolactone 50 mg | 1 tab | OD | 3–6 months | Oral | Or combined OCP; check potassium if renal disease"]),
  "Pregnancy: azelaic acid 20% or topical clindamycin + BPO; erythromycin/azithromycin if oral needed. No retinoids, no tetracyclines. Children under 8: no tetracyclines.")

L("Acne excoriée","Acne & appendageal disorders",
  "Explain the picking–scarring cycle. Keep nails short. Treat the underlying acne and screen for anxiety, depression or OCD.",
  ("Treat acne + habit reversal",[
   "Gel Adapalene 0.1% + Benzoyl peroxide 2.5% | Pea-size | HS | 12 weeks | Topical | ",
   "Cream Mupirocin 2% | Thin layer | BD | 7 days | Topical | Open excoriations only"]),
  ("Persistent picking",[
   "Tab. N-acetylcysteine 600 mg | 1 tab | BD | 3 months | Oral | Some evidence in skin-picking",
   "Tab. Fluoxetine 20 mg | 1 tab | OD | 3–6 months | Oral | With psychiatry input; or CBT / habit-reversal therapy"]))

L("Fox–Fordyce disease","Acne & appendageal disorders",
  "Avoid heat, tight clothing and friction. Response is often partial.",
  ("Topical",[
   "Cream Tretinoin 0.025% | Thin layer | HS (alternate nights at first) | 8–12 weeks | Topical | Axillae; irritation common",
   "Cream Clindamycin 1% | Thin layer | BD | 8 weeks | Topical | Or a mild topical steroid for itch flares"]),
  ("Refractory",[
   "Topical Pimecrolimus 1% cream | Thin layer | BD | 8 weeks | Topical | ",
   "Botulinum toxin A, fractional laser or microwave thermolysis | | Once | | Procedure | Specialist procedures for refractory cases"]))

L("Hidradenitis suppurativa","Acne & appendageal disorders",
  "Weight loss, stop smoking, loose clothing, antiseptic wash (chlorhexidine 4%). Stage with Hurley; score with IHS4. Screen for diabetes, metabolic syndrome, depression.",
  ("Hurley I / mild",[
   "Lotion Clindamycin 1% | Thin layer | BD | 12 weeks | Topical | To all lesions",
   "Inj. Triamcinolone 10 mg/mL | 0.2–1 mL | Once | Repeat in 3–4 weeks | Intralesional | For a painful inflamed nodule"]),
  ("Hurley II / moderate",[
   "Cap. Doxycycline 100 mg | 1 cap | BD | 12 weeks | Oral | Or tetracycline",
   "If no response: Tab. Clindamycin 300 mg + Tab. Rifampicin 300 mg | 1 tab each | BD | 10–12 weeks | Oral | Rifampicin colours urine orange; many interactions"]),
  ("Hurley III / refractory",[
   "Inj. Adalimumab | 160 mg wk 0, 80 mg wk 2, then 40 mg weekly | | Long-term | Subcutaneous | TB screening first",
   "Deroofing or wide surgical excision of sinus tracts | | | | Procedure | Combine with medical therapy"]),
  "Women: consider metformin, spironolactone or anti-androgen OCP. Avoid isotretinoin (poor response).")

L("Miliaria","Acne & appendageal disorders",
  "Cool environment, loose cotton clothing, frequent cool baths, avoid occlusive creams and over-wrapping infants.",
  ("All types",[
   "Calamine lotion | Apply | TDS | 1 week | Topical | Soothes miliaria rubra",
   "Lotion Clobetasone 0.05% | Thin layer | BD | 3–5 days | Topical | Short course for itchy miliaria rubra"]),
  ("Miliaria pustulosa / profunda",[
   "Cream Clindamycin 1% | Thin layer | BD | 7 days | Topical | If secondary infection",
   "Anhydrous lanolin | Thin layer | BD | 1–2 weeks | Topical | Helps miliaria profunda"]))

L("Perioral dermatitis","Acne & appendageal disorders",
  "Stop all topical steroids (expect a flare for 1–2 weeks), stop heavy creams and fluoridated toothpaste if implicated. 'Zero therapy' alone often works.",
  ("Mild",[
   "Gel Metronidazole 0.75% | Thin layer | BD | 8 weeks | Topical | ",
   "Cream Pimecrolimus 1% / Tacrolimus 0.03% | Thin layer | BD | 4–6 weeks | Topical | Eases steroid-withdrawal flare"]),
  ("Moderate–severe",[
   "Cap. Doxycycline 100 mg | 1 cap | OD | 6–8 weeks | Oral | Taper once clear",
   "Children / pregnancy: Tab. Erythromycin 250 mg / Azithromycin | per weight | | 4–6 weeks | Oral | Avoid tetracyclines"]))

L("Pyoderma faciale (rosacea fulminans)","Acne & appendageal disorders",
  "Sudden severe facial eruption in young women; check pregnancy and IBD. Stop cosmetics.",
  ("Start",[
   "Tab. Prednisolone 20 mg | 0.5–1 mg/kg | OD | 1–2 weeks then taper | Oral | Start 1–2 weeks before isotretinoin",
   "Cap. Isotretinoin 10 mg | 0.2–0.5 mg/kg | OD | 3–4 months | Oral | Pregnancy test and contraception mandatory"]),
  ("If isotretinoin cannot be used",[
   "Cap. Doxycycline 100 mg | 1 cap | BD | 4–6 weeks | Oral | With systemic steroid",
   "Gel Metronidazole 0.75% | Thin layer | BD | 8 weeks | Topical | "]),
  special="Pregnancy: oral prednisolone ± azithromycin; no isotretinoin, no tetracyclines.")

L("Rosacea","Acne & appendageal disorders",
  "Daily broad-spectrum sunscreen, gentle cleanser, avoid triggers (heat, spicy food, alcohol, steroids). Treat by phenotype.",
  ("Papulopustular – mild/moderate",[
   "Cream Ivermectin 1% | Thin layer | OD | 12 weeks | Topical | ",
   "Gel Metronidazole 0.75% / Azelaic acid 15% | Thin layer | BD | 12 weeks | Topical | Alternatives"]),
  ("Moderate–severe papulopustular / ocular",[
   "Cap. Doxycycline 40 mg MR (or 50–100 mg) | 1 cap | OD | 8–12 weeks | Oral | With topical ivermectin",
   "Persistent erythema: Gel Brimonidine 0.33% | Pea-size | OD morning | As needed | Topical | Effect lasts ~12 h; rebound possible"]),
  ("Refractory / phymatous / telangiectasia",[
   "Cap. Isotretinoin 10 mg | 0.1–0.3 mg/kg | OD | 4–6 months | Oral | Low dose; contraception",
   "Vascular laser / IPL; ablative laser or surgery for rhinophyma | | | | Procedure | "]),
  "Pregnancy: azelaic acid, metronidazole; azithromycin if oral needed.")

# ---------------- Bacterial ----------------
L("Impetigo","Bacterial infections",
  "Gently remove crusts with saline soaks, separate towels, keep child off school until crusts dry or 48 h of antibiotic.",
  ("Localised (few lesions)",[
   "Cream Mupirocin 2% / Fusidic acid 2% | Thin layer | TDS | 5–7 days | Topical | "]),
  ("Extensive, bullous or many contacts",[
   "Syp./Cap. Cephalexin | 25–50 mg/kg/day in 3–4 doses (adult 500 mg QID) | QID | 7 days | Oral | ",
   "Tab. Amoxicillin-clavulanate 625 mg | 1 tab | BD | 7 days | Oral | Children: 25–45 mg/kg/day amoxicillin"]),
  ("Penicillin allergy / suspected MRSA",[
   "Tab. Azithromycin 500 mg | 10 mg/kg/day | OD | 3–5 days | Oral | Or clindamycin / cotrimoxazole per sensitivity"]))

L("Folliculitis","Bacterial infections",
  "Stop shaving, waxing, oils and occlusive clothing for a few weeks. Antiseptic wash (chlorhexidine / BPO wash). Rule out fungal (Malassezia) and gram-negative causes if not responding.",
  ("Superficial, limited",[
   "Cream Mupirocin 2% / Fusidic acid 2% | Thin layer | BD | 7–10 days | Topical | ",
   "Benzoyl peroxide 5% wash | Lather 2 min | OD | 2–4 weeks | Topical | "]),
  ("Extensive or recurrent",[
   "Cap. Cephalexin 500 mg | 1 cap | QID | 7–10 days | Oral | Or cloxacillin",
   "Recurrent: Mupirocin nasal ointment | Small amount | BD | 5 days each month | Nasal | Decolonise; also family members"]))

L("Furuncle and carbuncle","Bacterial infections",
  "Warm compresses; incision and drainage of fluctuant lesions is the key treatment. Check blood sugar.",
  ("Small furuncle",[
   "Warm compress | | QID | Till drains | | ",
   "Cream Mupirocin 2% | Thin layer | BD | 7 days | Topical | Surrounding skin"]),
  ("Large, multiple, carbuncle or fever",[
   "Incision and drainage | | Once | | Procedure | Send pus for culture",
   "Cap. Cloxacillin 500 mg / Cephalexin 500 mg | 1 cap | QID | 7–10 days | Oral | Children: 50 mg/kg/day"]),
  ("Recurrent / MRSA",[
   "Tab. Cotrimoxazole DS 960 mg | 1 tab | BD | 7–10 days | Oral | Or clindamycin / doxycycline per culture",
   "Mupirocin nasal + chlorhexidine body wash | | | 5 days | Topical | Decolonise patient and household"]))

L("Ecthyma","Bacterial infections",
  "Clean ulcer, remove crust, treat insect bites and poor hygiene; heals with scarring.",
  ("Standard",[
   "Cap. Cloxacillin 500 mg / Cephalexin 500 mg | 1 cap | QID | 10 days | Oral | Children: 50 mg/kg/day",
   "Cream Mupirocin 2% | Thin layer | BD | 10 days | Topical | "]),
  ("Penicillin allergy",[
   "Tab. Azithromycin 500 mg | 1 tab | OD | 5 days | Oral | Or clindamycin 300 mg QID"]))

L("Erysipelas and cellulitis","Bacterial infections",
  "Rest and elevate limb, mark the edge, look for and treat a portal of entry (tinea pedis, fissures). Admit if systemic toxicity, rapid spread, immunocompromise or facial involvement.",
  ("Mild – outpatient",[
   "Tab. Amoxicillin-clavulanate 625 mg | 1 tab | TDS | 7–10 days | Oral | Or cephalexin / cloxacillin 500 mg QID",
   "Tab. Paracetamol 650 mg | 1 tab | SOS | 3–5 days | Oral | "]),
  ("Moderate–severe – admit",[
   "Inj. Ceftriaxone 1 g | 1–2 g | OD | Till afebrile, then oral | IV | Or IV cloxacillin / cefazolin",
   "Penicillin allergy: Inj./Tab. Clindamycin 300–600 mg | | TDS–QID | 10–14 days | IV/Oral | "]),
  ("Recurrent (≥2 episodes/yr)",[
   "Inj. Benzathine penicillin 1.2 MU | 1 dose | Every 3–4 weeks | 6–12 months | IM | Or oral penicillin V 250 mg BD prophylaxis"]))

L("Pitted keratolysis","Bacterial infections",
  "Keep feet dry, change socks daily, cotton socks, alternate shoes, treat hyperhidrosis.",
  ("First line",[
   "Gel Clindamycin 1% + Benzoyl peroxide 5% | Thin layer | BD | 2–4 weeks | Topical | Or erythromycin 2% / fusidic acid",
   "Aluminium chloride 20% | Thin layer | HS | Till dry, then weekly | Topical | For hyperhidrosis"]),
  ("Extensive / resistant",[
   "Tab. Erythromycin 500 mg | 1 tab | BD | 7–10 days | Oral | Or clarithromycin"]))

L("Erythrasma","Bacterial infections",
  "Confirm with coral-red Wood's lamp fluorescence. Keep folds dry; treat coexisting tinea / candida.",
  ("Localised",[
   "Gel Fusidic acid 2% / Clindamycin 1% / Erythromycin 2% | Thin layer | BD | 2 weeks | Topical | "]),
  ("Extensive / recurrent",[
   "Tab. Clarithromycin 1 g | 1 g | Single dose | Once | Oral | Or erythromycin 250 mg QID × 14 days",
   "Benzoyl peroxide 5% wash | | 3×/week | Ongoing | Topical | Prevents relapse"]))

# ---------------- Fungal ----------------
L("Tinea corporis / cruris / faciei","Fungal infections",
  "Loose cotton clothes, dry folds after bathing, wash clothes in hot water and sun-dry, treat all family members, no topical steroid combinations. Treat 2 weeks beyond clinical cure.",
  ("Limited, first episode",[
   "Cream Luliconazole 1% / Sertaconazole 2% | Thin layer, 2 cm beyond edge | OD–BD | 4 weeks | Topical | ",
   "Tab. Levocetirizine 5 mg | 1 tab | HS | 2 weeks | Oral | For itch"]),
  ("Extensive, recurrent or chronic",[
   "Cap. Itraconazole 100 mg | 2 caps (200 mg) | OD | 4–6 weeks | Oral | After a fatty meal, avoid antacids/PPIs; check interactions",
   "Tab. Terbinafine 250 mg | 1 tab | BD (500 mg/day) | 4–6 weeks | Oral | Alternative; check LFT if prolonged"]),
  ("Not responding",[
   "Cap. Itraconazole 100 mg | 2 caps | BD (400 mg/day) | 4 weeks | Oral | Check adherence, formulation, contacts; send KOH/culture ± sensitivity",
   "Cream Amorolfine 0.25% | Thin layer | OD | 4 weeks | Topical | Combine with oral"]),
  "Pregnancy: topicals only (clotrimazole, luliconazole); avoid oral azoles. Children: terbinafine 3–6 mg/kg or itraconazole 3–5 mg/kg.")

L("Tinea capitis","Fungal infections",
  "Always systemic treatment. Ketoconazole/selenium shampoo for patient and household to reduce spread. Examine and treat contacts; brushes, combs and caps to be cleaned.",
  ("First line",[
   "Tab. Griseofulvin (ultramicrosize) | 10–15 mg/kg/day (microsize 20–25 mg/kg/day) | OD | 6–12 weeks | Oral | After a fatty meal; best for Microsporum",
   "Shampoo Ketoconazole 2% | Leave 5 min | 3×/week | 4 weeks | Topical | Patient and contacts"]),
  ("Alternative / Trichophyton",[
   "Tab. Terbinafine | <20 kg 62.5 mg, 20–40 kg 125 mg, >40 kg 250 mg | OD | 4 weeks | Oral | Better for Trichophyton",
   "Cap. Itraconazole | 5 mg/kg/day | OD | 4–8 weeks | Oral | Alternative"]),
  ("Kerion",[
   "Tab. Prednisolone | 1 mg/kg | OD | 1–2 weeks | Oral | With antifungal; do not incise",
   "Antibiotic only if proven bacterial superinfection | | | | Oral | "]))

L("Tinea pedis & onychomycosis","Fungal infections",
  "Dry between toes, cotton socks, antifungal powder in shoes. Confirm nail infection by KOH/culture before oral treatment. Nails grow slowly: judge cure at 9–12 months.",
  ("Tinea pedis / ≤50% of nail, no matrix",[
   "Cream Luliconazole 1% | Thin layer | OD | 4 weeks | Topical | Feet",
   "Lacquer Amorolfine 5% / Ciclopirox 8% | Thin coat | Weekly / daily | 6–12 months | Topical | File nail first"]),
  ("Nail – matrix involved or many nails",[
   "Tab. Terbinafine 250 mg | 1 tab | OD | 12 weeks toenails, 6 weeks fingernails | Oral | Baseline LFT",
   "Cap. Itraconazole 200 mg pulse | 200 mg BD | 1 week a month | 3–4 pulses | Oral | Alternative; check interactions"]),
  ("Refractory / dermatophytoma",[
   "Nail avulsion (chemical / surgical) + oral antifungal | | | | Procedure | Or fluconazole 150–300 mg weekly × 6–12 months"]))

L("Pityriasis versicolor","Fungal infections",
  "Explain colour takes months to return after cure. Prophylaxis in hot season prevents recurrence.",
  ("First line",[
   "Shampoo Ketoconazole 2% / Selenium sulphide 2.5% | Lather on body, leave 10 min | OD | 1–2 weeks | Topical | ",
   "Cream Ketoconazole 2% | Thin layer | BD | 2 weeks | Topical | Small areas"]),
  ("Extensive / recurrent",[
   "Cap. Itraconazole 100 mg | 2 caps | OD | 5–7 days | Oral | Or fluconazole 300 mg weekly × 2",
   "Prophylaxis: ketoconazole shampoo | | Weekly | Hot months | Topical | Or itraconazole 400 mg once a month"]))

L("Cutaneous candidiasis / intertrigo","Fungal infections",
  "Keep folds dry and separated, weight loss, control diabetes, check for and treat oral/genital candida.",
  ("Localised",[
   "Cream Clotrimazole 1% / Miconazole 2% | Thin layer | BD | 2 weeks | Topical | ",
   "Powder Clotrimazole 1% | Dust | BD | 4 weeks | Topical | To keep folds dry"]),
  ("Extensive or recurrent",[
   "Tab. Fluconazole 150 mg | 1 tab | Weekly | 2–4 weeks | Oral | Or 50–100 mg OD × 14 days"]))

L("Mycetoma (Madura foot)","Fungal infections",
  "Grain colour, KOH, culture and biopsy decide actinomycetoma vs eumycetoma. MRI/X-ray for bone involvement. Long treatment; adherence is the key.",
  ("Actinomycetoma (bacterial)",[
   "Tab. Cotrimoxazole DS 960 mg | 1 tab | BD | Till cure (months) | Oral | Welsh regimen: + amikacin 15 mg/kg/day IV in 3-week cycles",
   "Tab. Dapsone 100 mg / Rifampicin 600 mg | | OD | Months | Oral | Common alternatives / additions"]),
  ("Eumycetoma (fungal)",[
   "Cap. Itraconazole 200 mg | 1 cap | BD | 9–12 months | Oral | ",
   "Surgical excision / debulking after 6 months | | | | Procedure | Itraconazole before and after surgery"]))

L("Sporotrichosis","Fungal infections",
  "Usually lymphocutaneous after thorn/soil injury.",
  ("First line",[
   "Cap. Itraconazole 100 mg | 2 caps (200 mg) | OD | 2–4 weeks beyond cure (3–6 months) | Oral | "]),
  ("Alternative",[
   "Saturated solution of potassium iodide (SSKI) | 5 drops TDS, increase to 40–50 drops TDS | TDS | 3–6 months | Oral | In milk/juice; watch for iodism, thyroid",
   "Tab. Terbinafine 250 mg | 1 tab | BD | 3–6 months | Oral | "]),
  ("Disseminated / immunocompromised",[
   "Inj. Amphotericin B | per protocol | | | IV | Admit; specialist care"]),
  "Pregnancy: local heat therapy; avoid itraconazole and SSKI.")

L("Chromoblastomycosis","Fungal infections",
  "Chronic verrucous plaques; muriform (Medlar) bodies on KOH/biopsy. Small lesions are best excised or destroyed.",
  ("Small lesion",[
   "Cryotherapy / surgical excision | | | | Procedure | With antifungal cover"]),
  ("Extensive",[
   "Cap. Itraconazole 200 mg | 1 cap | BD | 6–12 months | Oral | ",
   "Tab. Terbinafine 250 mg | 1–2 tabs | OD | 6–12 months | Oral | Alone or with itraconazole"]))

# ---------------- Infestations ----------------
L("Scabies","Infestations",
  "Treat all household contacts at the same time. Apply from neck to toes (include scalp and face in infants and elderly), under nails. Wash clothes and bedding in hot water or seal in a bag for 3 days. Itch can continue 2–4 weeks.",
  ("First line",[
   "Cream Permethrin 5% | Whole body | Once, leave 8–12 h | Repeat after 7 days | Topical | ",
   "Tab. Levocetirizine 5 mg | 1 tab | HS | 2 weeks | Oral | "]),
  ("Alternative / crusted / institutional",[
   "Tab. Ivermectin 6 mg | 200 µg/kg | Single dose | Repeat after 7–14 days | Oral | Empty stomach; not <15 kg or in pregnancy",
   "Crusted scabies: ivermectin on days 1, 2, 8, 9, 15 (+22, 29) + permethrin | | | | Oral + Topical | Admit/isolate; keratolytic to crusts"]),
  ("Nodular scabies",[
   "Cream Mometasone 0.1% / intralesional triamcinolone | | OD | 2–3 weeks | Topical | Nodules persist after cure"]),
  "Infants <2 months and pregnancy: permethrin 5% (or precipitated sulphur 5–10% ointment for 3 nights).")

L("Pediculosis","Infestations",
  "Treat all affected contacts. Wet-comb with a fine-tooth comb every 3 days for 2 weeks. Wash combs, caps, pillow covers in hot water.",
  ("Head lice – first line",[
   "Lotion Permethrin 1% | Apply to damp hair | Leave 10 min, rinse | Repeat day 7–10 | Topical | ",
   "Wet combing with nit comb | | Every 3 days | 2 weeks | | "]),
  ("Resistant / treatment failure",[
   "Tab. Ivermectin 6 mg | 200 µg/kg | Single dose | Repeat day 8 | Oral | Not <15 kg or in pregnancy",
   "Dimeticone 4% lotion | Apply 8 h | Once | Repeat day 7 | Topical | Physical action, no resistance"]),
  special="Pubic lice: permethrin 5% to all hairy areas, treat partner, screen for STIs. Eyelashes: petroleum jelly BD × 10 days.")

# ---------------- Viral ----------------
L("Herpes simplex","Viral infections",
  "Start antivirals within 72 h for best effect. Avoid contact with lesions; condoms for genital disease.",
  ("First episode",[
   "Tab. Acyclovir 400 mg | 1 tab | TDS | 7–10 days | Oral | Or valacyclovir 1 g BD × 7–10 days",
   "Cream Acyclovir 5% | Thin layer | 5×/day | 5 days | Topical | Labial only; limited benefit"]),
  ("Recurrent episode",[
   "Tab. Valacyclovir 500 mg | 4 tabs (2 g) | BD | 1 day | Oral | Herpes labialis; genital: 500 mg BD × 3 days",
   "Tab. Acyclovir 400 mg | 1 tab | TDS | 5 days | Oral | Alternative"]),
  ("Frequent recurrences (≥6/yr) / erythema multiforme trigger",[
   "Tab. Acyclovir 400 mg | 1 tab | BD | 6–12 months | Oral | Suppressive; or valacyclovir 500 mg OD",
   "Severe / immunocompromised / eczema herpeticum: Inj. Acyclovir 5–10 mg/kg | | 8-hourly | 7–10 days | IV | Admit"]),
  "Pregnancy: acyclovir is safe; suppression from 36 weeks for recurrent genital herpes.")

L("Molluscum contagiosum","Viral infections",
  "Self-limiting in 6–18 months; watchful waiting is acceptable in children. Avoid sharing towels, do not scratch. Genital lesions in adults: screen for STIs; extensive facial lesions: check HIV.",
  ("Few lesions",[
   "Curettage / needle extraction | | Once | Repeat as needed | Procedure | Topical anaesthetic cream first in children",
   "Cryotherapy | | Every 2–3 weeks | | Procedure | "]),
  ("Many lesions",[
   "Potassium hydroxide 10% solution | Dab on lesions | HS | Till inflamed | Topical | Stop when lesions redden",
   "Cream Tretinoin 0.05% / Cantharidin (in clinic) | | | | Topical | Alternatives"]))

L("Chickenpox (varicella)","Viral infections",
  "Isolate till all lesions crust, calamine, short nails, paracetamol for fever (no aspirin in children, avoid NSAIDs). Antivirals help most if started within 24 h.",
  ("Adolescents, adults, smokers, chronic skin/lung disease",[
   "Tab. Acyclovir 800 mg | 1 tab | 5×/day | 7 days | Oral | Or valacyclovir 1 g TDS × 7 days",
   "Calamine lotion | Apply | TDS | 1 week | Topical | "]),
  ("Healthy child",[
   "Syp. Acyclovir | 20 mg/kg (max 800 mg) | QID | 5 days | Oral | Optional if seen within 24 h"]),
  ("Pregnancy, immunocompromised, pneumonia or encephalitis",[
   "Inj. Acyclovir | 10 mg/kg | 8-hourly | 7–10 days | IV | Admit"]),
  "Exposed pregnant/immunocompromised non-immune: VZIG within 10 days of exposure.")

L("Warts (verruca)","Viral infections",
  "Many clear spontaneously in children. Pare thick warts before treatment. Choose by site and number; persistence matters more than agent.",
  ("Common / plantar – first line",[
   "Salicylic acid 16.7% + lactic acid 16.7% paint | Apply after soaking and paring | HS | 12 weeks | Topical | Protect surrounding skin",
   "Cryotherapy (liquid nitrogen) | 1–2 freeze-thaw cycles | Every 2–3 weeks | 3–4 sessions | Procedure | "]),
  ("Plane warts",[
   "Cream Tretinoin 0.05% | Thin layer | HS | 8 weeks | Topical | ",
   "Cream Imiquimod 5% | Thin layer | 3×/week | 8–12 weeks | Topical | "]),
  ("Recalcitrant / multiple",[
   "Intralesional immunotherapy (MMR / Candida antigen / PPD / vitamin D3) | 0.1–0.5 mL into largest wart | Every 2–4 weeks | 3–5 sessions | Intralesional | ",
   "Radiofrequency ablation / electrocautery / CO₂ laser | | | | Procedure | Risk of scar on soles"]))

L("Herpes zoster","Viral infections",
  "Start antiviral within 72 h (later if new lesions still appearing, eye involvement or immunocompromised). Keep lesions clean and dry. Ophthalmic zoster: refer to ophthalmology.",
  ("Standard",[
   "Tab. Valacyclovir 1 g | 1 tab | TDS | 7 days | Oral | Or acyclovir 800 mg 5×/day × 7 days; adjust in renal impairment",
   "Tab. Paracetamol 650 mg ± Tab. Pregabalin 75 mg | | TDS / HS | As needed | Oral | Acute pain"]),
  ("Disseminated, immunocompromised, severe ophthalmic",[
   "Inj. Acyclovir | 10 mg/kg | 8-hourly | 7–10 days | IV | Admit"]),
  ("Post-herpetic neuralgia",[
   "Tab. Pregabalin 75 mg | 75 mg BD → up to 300 mg/day | BD | 1–3 months | Oral | Or gabapentin / amitriptyline 10–25 mg HS",
   "Lidocaine 5% plaster / capsaicin | | 12 h on, 12 h off | | Topical | "]),
  "Prevention: recombinant zoster vaccine for ≥50 years and immunocompromised adults.")

# ---------------- STI ----------------
L("Anogenital warts","Sexually transmitted infections",
  "Screen for other STIs (HIV, syphilis), examine partner, condoms. Biopsy atypical, pigmented or non-responding warts. Recurrence is common.",
  ("Few, soft, non-keratinised",[
   "Podophyllotoxin 0.5% solution | Apply to warts | BD × 3 days, then 4 days off | Up to 4 cycles | Topical | Self-applied; not in pregnancy",
   "Cream Imiquimod 5% | Thin layer at night, wash off after 6–10 h | 3×/week | Up to 16 weeks | Topical | "]),
  ("Keratinised, many or failed topical",[
   "Cryotherapy | | Weekly | Till clear | Procedure | ",
   "Trichloroacetic acid 80–90% | Apply in clinic | Weekly | Till clear | Procedure | Safe in pregnancy"]),
  ("Extensive / giant",[
   "Electrocautery / radiofrequency / CO₂ laser / surgical excision | | | | Procedure | "]),
  "Pregnancy: cryotherapy or TCA only; no podophyllin, podophyllotoxin or imiquimod.")

L("Chancroid","Sexually transmitted infections",
  "Treat partners of the past 10 days. Test for HIV and syphilis. Re-examine in 3–7 days.",
  ("First line",[
   "Tab. Azithromycin 1 g | 1 g | Single dose | Once | Oral | Or Inj. ceftriaxone 250 mg IM single dose"]),
  ("Alternative",[
   "Tab. Ciprofloxacin 500 mg | 1 tab | BD | 3 days | Oral | Not in pregnancy",
   "Fluctuant bubo: needle aspiration | | | | Procedure | "]))

L("Genital ulcer disease","Sexually transmitted infections",
  "Syndromic management (NACO kit) when lab tests are not available; test for syphilis and HIV; treat partners.",
  ("Non-herpetic GUD (syphilis + chancroid)",[
   "Inj. Benzathine penicillin 2.4 MU | 2.4 MU (1.2 MU each buttock) | Single dose | Once | IM | After test dose per protocol",
   "Tab. Azithromycin 1 g | 1 g | Single dose | Once | Oral | Covers chancroid"]),
  ("Penicillin allergy",[
   "Cap. Doxycycline 100 mg | 1 cap | BD | 14 days | Oral | Not in pregnancy",
   "Tab. Azithromycin 1 g | 1 g | Single dose | Once | Oral | "]),
  ("Herpetic GUD",[
   "Tab. Acyclovir 400 mg | 1 tab | TDS | 7 days | Oral | "]))

L("Gonorrhoea / urethral discharge","Sexually transmitted infections",
  "Treat for both gonorrhoea and chlamydia (syndromic). Abstain 7 days, treat partners of the past 60 days, test for HIV and syphilis.",
  ("First line",[
   "Inj. Ceftriaxone 500 mg | 500 mg | Single dose | Once | IM | (1 g if >150 kg)",
   "Cap. Doxycycline 100 mg | 1 cap | BD | 7 days | Oral | Chlamydia cover"]),
  ("Pregnancy / doxycycline not possible",[
   "Tab. Azithromycin 1 g | 1 g | Single dose | Once | Oral | With ceftriaxone",
   "If injection not possible: Tab. Cefixime 800 mg | 800 mg | Single dose | Once | Oral | NACO 2024 alternative"]),
  ("Persistent discharge",[
   "Tab. Metronidazole 2 g | 2 g | Single dose | Once | Oral | Trichomonas; re-test, check adherence and re-exposure"]))

L("Lymphogranuloma venereum","Sexually transmitted infections",
  "Treat partners of the past 60 days. Test for HIV, syphilis, hepatitis B/C.",
  ("First line",[
   "Cap. Doxycycline 100 mg | 1 cap | BD | 21 days | Oral | "]),
  ("Pregnancy / alternative",[
   "Tab. Erythromycin 500 mg | 1 tab | QID | 21 days | Oral | Or azithromycin 1 g weekly × 3",
   "Fluctuant buboes: needle aspiration through healthy skin | | | | Procedure | Do not incise"]))
