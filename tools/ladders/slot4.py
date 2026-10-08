# Treatment ladders, slot 4: common conditions that had an old template but no case format.
# Sources: IADVL Textbook, Rook's 10e, Wolverton 4e, NACO STI/RTI guidelines 2024. Own wording.
D = []
def L(case, group, general, l1, l2, l3=None, special=""):
    D.append(dict(case=case, group=group, general=general, lines=[x for x in (l1, l2, l3) if x], special=special))

L("Syphilis","Sexually transmitted infections",
  "Confirm with VDRL/RPR (titre) + TPHA. Test for HIV; examine and treat partners (primary: 3 months, secondary: 6 months, early latent: 1 year). Follow titres at 3, 6, 12 months — expect 4-fold fall.",
  ("Early (primary, secondary, early latent <2 yr)",[
   "Inj. Benzathine penicillin 2.4 MU | 1.2 MU in each buttock | Single dose | Once | IM | After test dose per NACO; warn about Jarisch–Herxheimer reaction"]),
  ("Late latent / unknown duration",[
   "Inj. Benzathine penicillin 2.4 MU | 2.4 MU | Weekly | 3 doses | IM | "]),
  ("Penicillin allergy (non-pregnant)",[
   "Cap. Doxycycline 100 mg | 1 cap | BD | 14 days (early) / 28 days (late) | Oral | ",
   "Neurosyphilis: Inj. Aqueous crystalline penicillin 18–24 MU/day (3–4 MU 4-hourly) | | | 14 days | IV | Admit"]),
  "Pregnancy: penicillin only — desensitise if allergic; treat partner; newborn evaluation.")

L("Vaginal discharge","Sexually transmitted infections",
  "Syndromic management (NACO). Speculum exam; check pH, KOH whiff, wet mount if possible. Treat partner for trichomonas. Pregnancy: avoid single-dose 2 g metronidazole in first trimester per local protocol.",
  ("Vaginitis (BV + trichomonas + candida) – NACO kit 2",[
   "Tab. Secnidazole 2 g | 2 g | Single dose | Once | Oral | Or metronidazole 400 mg BD × 7 days; no alcohol for 48 h",
   "Tab. Fluconazole 150 mg | 1 tab | Single dose | Once | Oral | Candida"]),
  ("Cervicitis also suspected – NACO kit 1",[
   "Tab. Cefixime 400 mg / Inj. Ceftriaxone 500 mg IM + Tab. Azithromycin 1 g | | Single dose | Once | Oral/IM | "]),
  ("Recurrent candidiasis (≥4/yr)",[
   "Tab. Fluconazole 150 mg | 1 tab | Day 1, 4, 7, then weekly | 6 months | Oral | Check diabetes"]))

L("Vulvovaginal candidiasis","Sexually transmitted infections",
  "Check diabetes, antibiotics, steroids, pregnancy, HIV. Cotton underwear, avoid douching.",
  ("Uncomplicated",[
   "Tab. Fluconazole 150 mg | 1 tab | Single dose | Once | Oral | ",
   "Clotrimazole 500 mg vaginal pessary / 2% vaginal cream | 1 | HS | Single dose / 7 days | Vaginal | Pregnancy: topical only, 7 days"]),
  ("Recurrent / severe",[
   "Tab. Fluconazole 150 mg | 1 tab | Every 72 h × 3, then weekly | 6 months | Oral | Culture for non-albicans if failing"]))

L("Oral candidiasis","Oral & mucosal disorders",
  "Look for cause: dentures, inhaled steroids (rinse after use), diabetes, antibiotics, HIV. Clean dentures and remove at night.",
  ("First line",[
   "Clotrimazole 10 mg troche / Nystatin suspension 1 mL (1 lakh IU) | | QID / 5×/day | 7–14 days | Oral | Swish and swallow",
   "Miconazole oral gel 2% | | QID | 7 days | Oral | Not with warfarin"]),
  ("Extensive / immunocompromised",[
   "Tab. Fluconazole 150 mg | 100–200 mg | OD | 7–14 days | Oral | Oesophageal: 14–21 days"]))

L("Hirsutism","Hair & nail disorders",
  "Score (modified Ferriman–Gallwey). Check for PCOS (cycles, ultrasound), and if rapid onset/virilisation: testosterone, DHEAS, 17-OHP, prolactin, TSH. Weight loss if overweight. Results take 6 months.",
  ("Mild / cosmetic",[
   "Laser hair reduction (diode / Nd:YAG for dark skin) | | Every 4–6 weeks | 6–8 sessions | Procedure | Maintenance needed",
   "Cream Eflornithine 13.9% | Thin layer | BD | 2 months, continue if helpful | Topical | Face"]),
  ("Moderate–severe / PCOS",[
   "Combined OCP (ethinyl estradiol + cyproterone acetate / drospirenone) | 1 tab | OD (21/7) | ≥6 months | Oral | Check contraindications (clots, migraine with aura, smoking)",
   "Tab. Metformin 500 mg | 1 tab | BD | 6 months | Oral | Insulin resistance"]),
  ("Add anti-androgen after 6 months",[
   "Tab. Spironolactone 50 mg | 50–100 mg | BD | ≥6 months | Oral | Always with contraception",
   "Tab. Finasteride 2.5–5 mg | | OD | | Oral | Only with reliable contraception"]))

HOLD=1
if False: L("Palmar / plantar hyperhidrosis","Acne & appendageal disorders",
  "Check for secondary causes if generalised, unilateral, night sweats or late onset (thyroid, diabetes, TB, lymphoma, drugs). Score with HDSS.",
  ("First line",[
   "Aluminium chloride hexahydrate 15–20% | Apply to dry skin | HS | Daily till dry, then 1–2×/week | Topical | Wash off in morning; irritation"]),
  ("Not controlled",[
   "Tap-water iontophoresis | 15–20 mA, 20–30 min | 3×/week, then weekly | | Procedure | Palms and soles",
   "Tab. Glycopyrrolate 1 mg | 1–2 mg | BD | As needed | Oral | Dry mouth, blurred vision, urinary retention; avoid in glaucoma"]),
  ("Refractory",[
   "Botulinum toxin A | 50–100 U per palm/axilla (intradermal) | Every 6–9 months | | Intradermal | Nerve block for palms",
   "Tab. Oxybutynin 2.5–5 mg / microwave thermolysis (axilla) / sympathectomy (last resort) | | | | | Compensatory sweating after surgery"]))

L("Post-inflammatory hyperpigmentation","Pigmentary disorders",
  "Treat and control the underlying disease first (acne, eczema, LP). Strict sun protection. Avoid harsh products; fades over months.",
  ("First line",[
   "Sunscreen SPF 50 (tinted) | | Every 3 h | Long-term | Topical | ",
   "Cream Azelaic acid 20% / Hydroquinone 2–4% / Retinoid | Thin layer | HS | 2–3 months | Topical | Hydroquinone not beyond 3 months"]),
  ("Persistent",[
   "Superficial chemical peels (glycolic / salicylic / lactic) | | Every 2–3 weeks | 4–6 sessions | Procedure | Priming; dark skin — low concentrations",
   "Low-fluence Q-switched Nd:YAG | | | | Procedure | Dermal pigment; risk of worsening"]))

L("Periorbital hyperpigmentation","Pigmentary disorders",
  "Mixed causes: pigment, vascular, shadowing, rubbing (atopy). Sleep, stop rubbing, sunscreen, treat allergy.",
  ("First line",[
   "Cream Azelaic acid / Vitamin C / Niacinamide / Kojic acid | Thin layer | HS | 3 months | Topical | Gentle products only",
   "Sunscreen / sunglasses | | Daily | | | "]),
  ("Procedural",[
   "Glycolic / lactic peel (low strength), Q-switched Nd:YAG, hyaluronic filler for tear trough | | | | Procedure | "]))

L("Polymorphic light eruption","Reactive & drug eruptions",
  "Sun protection (SPF 50, broad spectrum incl. UVA), clothing, avoid midday sun; gradual sun exposure in spring. Rule out lupus (ANA, Ro) if atypical.",
  ("Episodes",[
   "Cream Mometasone 0.1% | Thin layer | OD | 1 week | Topical | ",
   "Tab. Levocetirizine 5 mg | 1 tab | HS | 1–2 weeks | Oral | "]),
  ("Severe or frequent",[
   "Prophylactic NB-UVB / PUVA hardening in early summer | | 3×/week | 4–6 weeks | Phototherapy | ",
   "Tab. Prednisolone 20–30 mg | | OD | 5–7 days | Oral | Short course for severe flares"]),
  ("Refractory",[
   "Tab. Hydroxychloroquine 200 mg | | BD | Summer months | Oral | Or nicotinamide, beta-carotene (weak evidence)"]))

L("Stasis (venous) dermatitis","Eczemas",
  "Treat venous insufficiency: leg elevation, walking, compression stockings once eczema settles, weight loss; venous Doppler. Avoid neomycin and many topicals (high contact allergy risk) — patch test if not settling.",
  ("First line",[
   "Ointment Mometasone 0.1% | Thin layer | OD | 2 weeks | Topical | ",
   "Emollient (paraffin based) | | BD | Long-term | Topical | ",
   "Compression stockings (class II) | | Daily | Long-term | | After acute phase; check ABPI"]),
  ("Not settling / ulcerated",[
   "Treat infection per culture; patch test for contact allergy | | | | | ",
   "Venous ablation / surgery | | | | Procedure | "]))

L("Topical steroid–damaged face","Acne & appendageal disorders",
  "Stop the steroid (taper potent steroids over 2–4 weeks to lessen rebound). Explain rebound flare, redness and burning for weeks. Gentle cleanser, moisturiser, sunscreen; no 'fairness' creams.",
  ("Withdrawal",[
   "Ointment Tacrolimus 0.03% / Cream Pimecrolimus 1% | Thin layer | BD | 4–8 weeks | Topical | Eases rebound",
   "Cap. Doxycycline 100 mg | 1 cap | OD | 6–8 weeks | Oral | Papulopustular rosacea-like eruption",
   "Tab. Levocetirizine 5 mg | 1 tab | HS | 2–4 weeks | Oral | "]),
  ("Persistent redness / pigmentation",[
   "Gel Brimonidine 0.33% / Azelaic acid 15% / Ivermectin 1% | | OD | | Topical | ",
   "Vascular laser / IPL | | | | Procedure | Telangiectasia"]))

L("Generalised pustular psoriasis","Papulosquamous & erythroderma",
  "Admit. Fluids, electrolytes, calcium, albumin; watch sepsis, ARDS, hypocalcaemia. Stop triggers (steroid withdrawal, infection, drugs). Avoid systemic steroids. Bland emollients, wet dressings.",
  ("First line",[
   "Cap. Cyclosporine 100 mg | 3–5 mg/kg/day | BD | Till controlled, then taper | Oral | Fastest",
   "Cap. Acitretin 25 mg | 0.5–1 mg/kg | OD | Months | Oral | Contraception for 3 years",
   "Tab. Methotrexate | 0.2–0.4 mg/kg | Weekly | | Oral | "]),
  ("Refractory / recurrent",[
   "Inj. Spesolimab 900 mg | 900 mg | Single dose, repeat after 1 week if needed | | IV | IL-36 receptor blocker; TB screening",
   "Infliximab / Adalimumab / Secukinumab / Ixekizumab | per label | | | IV/SC | "]),
  "Pregnancy (impetigo herpetiformis): prednisolone is acceptable here; cyclosporine; early delivery may be needed. Children: acitretin, cyclosporine, methotrexate.")

L("Papular urticaria (insect bite hypersensitivity)","Infestations",
  "Insect control at home (bedbugs, fleas from pets, mosquitoes), bed nets, deworm and de-flea pets, light full-sleeve clothes. Explain recurrent crops till tolerance develops.",
  ("First line",[
   "Cream Mometasone 0.1% | Thin layer | OD | 1 week | Topical | ",
   "Tab. Levocetirizine 5 mg / Syp. Cetirizine | | HS | 2 weeks | Oral | ",
   "Insect repellent (DEET / picaridin) | | Daily | | Topical | "]),
  ("Infected / nodular",[
   "Cream Mupirocin 2% | | BD | 5–7 days | Topical | ",
   "Inj. Triamcinolone into persistent nodules | | | | Intralesional | Adults"]))

L("Pityrosporum (Malassezia) folliculitis","Fungal infections",
  "Itchy monomorphic papules on upper back/chest, worse with sweat, oils, antibiotics, steroids. KOH shows yeast. Prophylaxis to prevent relapse.",
  ("First line",[
   "Shampoo Ketoconazole 2% as body wash | Leave 5 min | OD | 2–4 weeks | Topical | ",
   "Cream Ketoconazole 2% | Thin layer | BD | 4 weeks | Topical | "]),
  ("Extensive / not responding",[
   "Cap. Itraconazole 100 mg | 2 caps | OD | 1–3 weeks | Oral | Or fluconazole 100–200 mg/day × 1–4 weeks",
   "Prophylaxis: ketoconazole wash weekly / itraconazole 200 mg monthly | | | | | "]))

L("Pityriasis lichenoides chronica","Papulosquamous & erythroderma",
  "Chronic, relapsing; children often improve with time. Biopsy if atypical.",
  ("First line",[
   "Cap. Doxycycline 100 mg (adults) / Tab. Erythromycin 30–50 mg/kg/day (children) | | BD | 2–3 months | Oral | ",
   "Cream Mometasone 0.1% / Tacrolimus 0.1% | | OD | | Topical | Itch"]),
  ("Not responding",[
   "Narrowband UVB / natural sunlight | | 3×/week | 2–3 months | Phototherapy | Most effective"]),
  ("Refractory",[
   "Tab. Methotrexate 7.5–20 mg | | Weekly | | Oral | Also for PLEVA / febrile ulceronecrotic (admit)"]))

L("Urticarial vasculitis","Reactive & drug eruptions",
  "Wheals lasting >24 h, burning, leaving bruising. Biopsy; check C3, C4, C1q (hypocomplementaemic type), ANA, hepatitis B/C, urine, renal function.",
  ("Normocomplementaemic, skin-limited",[
   "Tab. Levocetirizine 5 mg | 1–4 tabs | OD–BD | | Oral | Symptom relief",
   "Tab. Dapsone 100 mg / Colchicine 0.5 mg / Hydroxychloroquine 200 mg | | OD–BD | 3 months | Oral | Check G6PD before dapsone"]),
  ("Systemic / hypocomplementaemic",[
   "Tab. Prednisolone 0.5–1 mg/kg + Azathioprine / Mycophenolate | | | | Oral | With rheumatology/nephrology"]),
  ("Refractory",[
   "Inj. Omalizumab / Rituximab | per label | | | SC/IV | Limited evidence"]))

L("Maculopapular drug eruption","Reactive & drug eruptions",
  "Identify and stop the culprit (onset 4–14 days after starting). Look for red flags of DRESS (fever, facial oedema, lymph nodes, eosinophilia, liver) or SJS (mucosa, blisters, skin pain). Give a drug-allergy card.",
  ("Mild",[
   "Cream Mometasone 0.1% | Thin layer | OD–BD | 1 week | Topical | ",
   "Tab. Levocetirizine 5 mg | 1 tab | HS | 1–2 weeks | Oral | "]),
  ("Extensive / DRESS",[
   "Tab. Prednisolone 0.5–1 mg/kg | | OD | Slow taper over 6–8 weeks for DRESS | Oral | Monitor liver, kidney, CBC, thyroid later",
   "Cap. Cyclosporine 3–5 mg/kg/day | | BD | 1–2 weeks | Oral | Steroid-sparing alternative in DRESS"]))

L("Bullous pemphigoid","Vesicobullous diseases",
  "Elderly; biopsy + DIF, BP180/230 ELISA. Stop DPP-4 inhibitors (gliptins) and other suspect drugs. Wound care, bone protection, watch for infection; check sugar and BP on steroids.",
  ("First line",[
   "Cream Clobetasol 0.05% | Whole body except face, up to 40 g/day (20–30 g if <45 kg) | OD | Taper over 4 months | Topical | As effective as oral steroids, safer",
   "Cap. Doxycycline 100 mg + Tab. Nicotinamide 500 mg | 2 caps / 1–2 tabs | OD / TDS | Months | Oral | Mild–moderate, steroid-sparing"]),
  ("Extensive or not controlled",[
   "Tab. Prednisolone 20 mg | 0.5 mg/kg | OD | Taper over months | Oral | ",
   "Tab. Methotrexate 5–15 mg / Azathioprine / Mycophenolate | | | | Oral | Steroid-sparing"]),
  ("Refractory",[
   "Inj. Dupilumab / Omalizumab / Rituximab / IVIG | per label | | | SC/IV | "]))
