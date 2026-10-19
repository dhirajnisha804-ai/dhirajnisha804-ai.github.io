# Short-case expansion S8 (target ≥15 Qs): bacterial (5), dermatitis artefacta, reactive/drug (5), granuloma annulare.
# Own words; viva-length bullets. Facts from IADVL 5e and standard references.
STAPH = ("Describe Staphylococcus aureus virulence factors.", ["Surface: protein A (binds IgG Fc), clumping factor, fibronectin-binding proteins, capsule", "Toxins: exfoliative toxins A/B (SSSS, bullous impetigo), superantigens (TSST-1, enterotoxins — toxic shock syndrome, AD flares), PVL (necrotising infections), haemolysins, leukocidins", "Enzymes: coagulase, catalase, hyaluronidase, lipase, staphylokinase, β-lactamase; MRSA — mecA gene (PBP2a)"])
TSS = ("What is toxic shock syndrome?", ["Superantigen-mediated (TSST-1/ enterotoxins of S. aureus; streptococcal pyrogenic exotoxins) — fever ≥38.9 °C, hypotension, diffuse macular erythroderma ('sunburn'), desquamation of palms/soles 1–2 weeks later, multiorgan involvement (GI, muscle, mucosal hyperaemia, renal, hepatic, CNS); tampon, wound, post-surgical, nasal packing", "Treat: remove source, fluids/ ICU, anti-staphylococcal β-lactam/ vancomycin + clindamycin (switches off toxin), IVIG in severe"])
SCAR = ("Classify cutaneous adverse drug reactions by Gell–Coombs (revised).", ["Type I (IgE): urticaria, angioedema, anaphylaxis", "Type II (cytotoxic antibody): drug-induced pemphigus, immune thrombocytopenic purpura", "Type III (immune complex): serum sickness, vasculitis", "Type IV T-cell: IVa (Th1 — contact dermatitis), IVb (Th2/ eosinophils — DRESS, MPE), IVc (cytotoxic — SJS/TEN, FDE, MPE), IVd (neutrophilic — AGEP)", "Non-immune: pseudo-allergy (MRGPRX2), phototoxic, pigmentation, overdose/ side effects"])
D = [
dict(case="Furuncle and carbuncle", qa=[
 STAPH,
 ("What is community-acquired MRSA (CA-MRSA) and its treatment?", ["MRSA strains (e.g. USA300, SCCmec IV) causing skin infections in healthy people (athletes, prisoners, military), often PVL-positive — recurrent boils/ abscesses; treat by incision and drainage + oral cotrimoxazole, doxycycline, clindamycin or linezolid; decolonisation for recurrence"]),
 ]),
dict(case="Ecthyma", qa=[
 STAPH,
 ("Describe Streptococcus pyogenes virulence factors.", ["M protein (anti-phagocytic; nephritogenic/ rheumatogenic types), hyaluronic acid capsule, streptolysin O and S, streptokinase, DNases, hyaluronidase, pyrogenic exotoxins (SpeA/B/C — scarlet fever, toxic shock-like syndrome), C5a peptidase"]),
 ("What is ecthyma gangrenosum workup?", ["Blood cultures, biopsy for histology and tissue culture (Pseudomonas, also Aeromonas, Klebsiella, E. coli, fungi — Aspergillus, Mucor, Fusarium in neutropenia), absolute neutrophil count, HIV; start empirical anti-pseudomonal therapy immediately"]),
 ("Ecthyma in India — common settings.", ["Children with scabies/ insect bites and poor hygiene, rural barefoot workers with minor trauma, diabetics, IV drug users; often secondary to pediculosis or scabies — treat the underlying infestation"]),
 ("Prevention advice.", ["Treat insect bites and scabies promptly, keep nails short, hygiene, avoid scratching, protective footwear, nutritional support"]),
 ("What is pseudomonal hot-foot syndrome?", ["Painful red plantar nodules in children after wading in contaminated pool water (Pseudomonas aeruginosa) — self-limiting; analgesics; antibiotics in severe cases"]),
 ]),
dict(case="Erysipelas and cellulitis", qa=[
 TSS,
 ]),
dict(case="Pitted keratolysis", qa=[
 ("What is the natural course if untreated?", ["Persists as long as predisposing factors (sweating, occlusion) continue; may resolve when feet are kept dry; recurrence common after stopping treatment unless footwear and sweating are managed"]),
 ("Which occupational groups need prevention advice?", ["Soldiers, athletes, sailors, rice-field farmers, factory workers in boots, police — moisture-wicking socks changed twice daily, antiperspirants (aluminium chloride), antiseptic foot soaps, alternate footwear to allow drying"]),
 ("Explain why topical azoles work in pitted keratolysis.", ["Imidazoles (clotrimazole, miconazole) have activity against Gram-positive bacteria (Kytococcus, Corynebacterium, Dermatophilus) in addition to fungi; benzoyl peroxide is also antibacterial and drying"]),
 ("Differentiate from plantar pitting of basal cell naevus syndrome.", ["Gorlin pits are on palms/ soles as small shallow 'pink' pits from childhood with jaw cysts and BCCs, not related to sweat/ smell; pitted keratolysis pits are on weight-bearing sole with malodour and sweating"]),
 ("Corynebacterial infections of skin — the triad.", ["Erythrasma (C. minutissimum), pitted keratolysis (Kytococcus/ Corynebacterium), trichomycosis (C. tenuis) — often coexist in hyperhidrotic patients; all respond to topical antibacterials/ azoles and drying measures"]),
 ]),
dict(case="Erythrasma", qa=[
 ("Describe the organism and its fluorescence.", ["Corynebacterium minutissimum — Gram-positive, non-spore-forming diphtheroid rod (lipophilic); produces coproporphyrin III which fluoresces coral-red under Wood's lamp (washed off by bathing)"]),
 ("Interdigital erythrasma — features and complex.", ["Commonest form — macerated white scaling and fissuring in 3rd/4th toe webs, often with dermatophytes, Candida and Gram-negative bacteria ('dermatophytosis complex'); treat with topical azoles (cover all organisms) and keep webs dry"]),
 ("Histopathology/ Gram stain findings.", ["Gram stain of scrapings: Gram-positive rods/ filaments in stratum corneum; histology rarely needed — organisms in upper stratum corneum on PAS/ Gram stain, minimal inflammation"]),
 ("Erythrasma and diabetes — significance.", ["Disciform/ generalised erythrasma is commoner in diabetics and obese — screen blood sugar in extensive or recurrent disease"]),
 ("Systemic treatment doses.", ["Erythromycin 250 mg four times daily for 14 days, or single-dose clarithromycin 1 g; tetracyclines alternative; topical fusidic acid/ clindamycin/ erythromycin/ azoles for localised"]),
 ("Prevention of recurrence.", ["Keep folds dry, loose cotton clothing, antibacterial soap washes, absorbent powders, weight loss, control diabetes, treat hyperhidrosis"]),
 ]),
dict(case="Dermatitis artefacta", qa=[
 ("Describe dermatitis simulata and dermatitis passivata.", ["Dermatitis simulata: mimicking skin disease without damaging skin (applying dyes, make-up to simulate lesions)", "Dermatitis passivata: self-induced but passive (e.g. allowing a wound to become infected by not treating it)"]),
 ("Factitious disorder imposed on another (Munchausen by proxy).", ["Carer (usually mother) fabricates or induces illness in a child — repeated unexplained lesions, symptoms only in carer's presence, failure to respond to treatment, improvement when separated; child protection referral mandatory"]),
 ("Body-focused repetitive behaviours (BFRBs).", ["Trichotillomania, excoriation (skin-picking) disorder, onychophagia (nail biting), onychotillomania, lip/ cheek biting — DSM-5 OCD-related disorders; treat with habit reversal, CBT, NAC, SSRIs"]),
 ("Signs on histology suggesting self-infliction.", ["Foreign material (polarisable particles — talc, starch, fibres), epidermal necrosis with sharp cut-off, burns pattern (flattened elongated keratinocytes), haemorrhage without vasculitis, injected substances in fat (oil — lipogranulomas)"]),
 ("Prognosis of dermatitis artefacta.", ["Chronic relapsing course (years) especially with personality disorders; better outcome in adolescents with acute stress triggers and early psychological support"]),
 ]),
dict(case="Erythema multiforme", qa=[
 ("Recurrent and persistent EM.", ["Recurrent EM: ≥6 episodes/year, usually HSV — continuous suppressive antivirals for ≥6–12 months; persistent EM (continuous lesions without remission) — associated with occult HSV, EBV, IBD, malignancy; dapsone, thalidomide, azathioprine, MMF, JAK inhibitors"]),
 ("Oral EM — features and management.", ["Painful erosions/ haemorrhagic crusts of lips, buccal mucosa, tongue (may occur without skin); topical steroid gels, anaesthetic/ antiseptic mouthwashes, soft diet, oral acyclovir if HSV-triggered"]),
 SCAR,
 ]),
dict(case="Erythema nodosum", qa=[
 ("Erythema nodosum leprosum vs EN.", ["ENL: in BL/LL leprosy, crops of evanescent tender nodules anywhere (face, arms, trunk), may ulcerate (necrotic ENL), systemic symptoms (fever, neuritis, iritis, orchitis), smear positive; histology — neutrophilic vasculitis with foamy macrophages and AFB", "EN: shins, does not ulcerate, septal panniculitis without vasculitis or bacilli"]),
 ("EN in pregnancy and OCP use.", ["Oestrogen-related EN in first/ second trimester or with OCPs — supportive care, stop OCP; NSAIDs avoided in third trimester (ductus closure) — use rest, compression, short steroid if needed"]),
 ("Chronic/ migratory EN variants.", ["Erythema nodosum migrans (subacute nodular migratory panniculitis of Vilanova — unilateral migratory plaques with central clearing on legs of women; responds to potassium iodide)"]),
 ("EN and TB in India.", ["Strongly positive Mantoux/ IGRA with EN — look for primary TB (hilar lymphadenopathy, pulmonary focus) especially in children; treat TB if confirmed; EN usually resolves"]),
 ("EN in IBD — features.", ["More with Crohn's (5–15%) than UC; parallels bowel activity; treat the bowel disease (steroids, anti-TNF); differentiate from pyoderma gangrenosum (ulcerates, independent of activity)"]),
 ]),
dict(case="Fixed drug eruption", qa=[
 ("Generalised bullous FDE (GBFDE) in detail.", ["Multiple large dusky patches with blisters involving >10% BSA, few mucosal sites, elderly with comorbidities; mortality ~20% (similar to SJS/TEN); history of previous FDE at same sites; manage in burns unit, cyclosporine, avoid culprit"]),
 ("Non-pigmenting FDE — features.", ["Large symmetrical erythematous plaques without residual pigmentation, often on hips, limbs; classically pseudoephedrine; also NSAIDs, piroxicam"]),
 ("Oral provocation test — protocol and contraindications.", ["Start with 1/10–1/4 therapeutic dose under observation, increase stepwise; reaction within 30 min–8 h confirms; contraindicated in GBFDE, extensive mucosal involvement, pregnancy; informed consent"]),
 ("Fixed food eruption — examples.", ["Cashew, peanut, lentils, strawberries, tonic water (quinine), food colours (tartrazine), aspartame; diagnosis by elimination and challenge"]),
 SCAR,
 ("Why does FDE heal with pigmentation more in Indians?", ["Basal keratinocyte damage leads to pigment incontinence — melanophages in dermis; darker skin with more melanin gives more prominent and prolonged slate-grey pigmentation"]),
 ]),
dict(case="Acute generalised exanthematous pustulosis (AGEP)", qa=[
 ("What is the patch test protocol for AGEP?", ["Patch test with suspected drugs (5–10% in petrolatum) 6 weeks–6 months after recovery on previously affected back; read at 48, 72, 96 h — pustular reaction at site confirms; positivity ~50%; delayed readings important"]),
 ("Localised AGEP (ALEP).", ["Acute localised exanthematous pustulosis — pustules confined to face/ neck/ chest after drugs (amoxicillin, clindamycin) — same mechanism, milder"]),
 ("Differentiate AGEP from DRESS with pustules.", ["DRESS: latency 2–8 weeks, facial oedema, lymphadenopathy, eosinophilia, atypical lymphocytes, internal organ involvement (liver), prolonged course >2 weeks; AGEP: latency <48 h (antibiotics), resolves in <2 weeks, neutrophilia"]),
 SCAR,
 ("Why are antibiotics often wrongly continued in AGEP?", ["Fever with pustules and neutrophilia suggests sepsis, so antibiotics (often the culprit) are escalated — recognise sterile pustules (Gram stain/ culture negative), stop suspected drugs"]),
 ]),
dict(case="Tattoo & tattoo reactions", qa=[
 ("Infections from tattooing — prevention.", ["Use licensed studios with sterile single-use needles/ ink caps, gloves, hand hygiene, autoclaving; risks — hepatitis B/ C, HIV, NTM (contaminated ink/ dilution water), syphilis, leprosy (historically), warts; check hepatitis B vaccination"]),
 ("Granulomatous tattoo reaction and sarcoidosis.", ["Papules/ nodules within tattoo (often black or red) with sarcoidal granulomas; may be first sign of systemic sarcoidosis (lungs, eyes — uveitis, 'tattoo-associated uveitis'); investigate with chest X-ray, ACE, eye exam; treat with intralesional steroids, HCQ, methotrexate"]),
 ("MRI and tattoos.", ["Iron-oxide pigments may cause burning/ swelling during MRI (heating, ferromagnetic artefacts) — rare, mild; inform radiographer; cold compress"]),
 ("Laser removal complications in detail.", ["Blistering, pinpoint bleeding, textural change, hypopigmentation (dark skin — 1064 nm safer), hyperpigmentation, scarring, allergic reaction from pigment release (anaphylaxis rare), paradoxical darkening (white/ flesh/ red-brown ferric oxide), ink darkening of cosmetic tattoos, incomplete removal (green/ blue harder)"]),
 ("Legal and ethical aspects.", ["Minors require parental consent (varies by state/ country); document medical history (bleeding disorders, keloid tendency, pregnancy, immunosuppression, active skin disease) before tattooing"]),
 ("Cosmetic tattoos (permanent make-up) — specific issues.", ["Eyebrow microblading, lip liner, eyeliner — allergic granulomas, infections, migration, unnatural colour change with time, paradoxical darkening on laser removal; eyelid tattoo risks corneal injury"]),
 ]),
dict(case="Granuloma annulare", qa=[
 ("Dermoscopy findings.", ["Pinkish-yellow/ orange structureless areas with dotted/ linear irregular vessels, peripheral white/ pink annular rim; no scale (vs tinea)"]),
 ("What is 'interstitial granuloma annulare' vs interstitial granulomatous dermatitis?", ["Interstitial GA: histiocytes between collagen bundles with mucin, patch-type clinical lesions", "Interstitial granulomatous dermatitis: linear cords ('rope sign') on trunk/ flanks with arthritis, associated with RA/ autoimmune disease/ drugs (drug-induced IGDR — ACE inhibitors, statins, TNF inhibitors); differentiate by mucin (less in IGD)"]),
 ("Drug-induced GA.", ["TNF inhibitors, allopurinol, amlodipine, gold, diclofenac, PD-1 inhibitors, vaccines (BCG, influenza, hepatitis B) — remove trigger"]),
 ("GA and HIV.", ["Generalised/ perforating GA can occur in HIV (often CD4 low) — offer HIV test in generalised or atypical GA"]),
 ("Classify cutaneous granulomas (linked question).", ["Infectious: TB, leprosy, NTM, deep fungi, leishmaniasis, syphilis", "Non-infectious: sarcoidal (sarcoidosis), palisading (GA, necrobiosis lipoidica, rheumatoid nodule, necrobiotic xanthogranuloma), foreign body (tattoo, silica, suture, keratin), tuberculoid (rosacea, LMDF), xanthogranulomatous, granulomatous vasculitis, granulomatous mycosis fungoides"]),
 ]),
]
