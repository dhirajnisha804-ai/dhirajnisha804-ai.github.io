# Extra viva questions appended to the 14 small cases that had only 5 questions (target ≥9 each).
# Own words; facts from IADVL 5e and standard references. make.py appends these to the existing case posts.
D = [
dict(case="Freckles (ephelides)", qa=[
 ("Why do freckles darken in summer? Explain at cell level.", ["UV upregulates POMC/α-MSH and MC1R signalling → more tyrosinase activity and larger, more numerous eumelanin/pheomelanin melanosomes transferred to keratinocytes; melanocyte number is not increased, so pigment fades when UV stimulus falls in winter"]),
 ("What is the role of MC1R?", ["Melanocortin-1 receptor on melanocytes; α-MSH binding raises cAMP → eumelanin synthesis", "Loss-of-function variants (R151C, R160W, D294H — 'red hair colour' alleles) give red hair, fair skin, freckling, poor tanning and higher melanoma and NMSC risk independent of UV"]),
 ("Dermoscopy of a freckle?", ["Light-brown homogeneous or faint reticular pattern with sharp moth-eaten border; no globules or dots — helps distinguish from naevi"]),
 ("What is the significance of freckling in xeroderma pigmentosum?", ["Freckle-like pigmentation in the first 1–2 years of life with severe sunburn on minimal exposure; followed by poikiloderma, actinic keratoses and skin cancers in the first decade — DNA repair (NER) defect; needs strict photoprotection"]),
 ]),
dict(case="Idiopathic guttate hypomelanosis", qa=[
 ("What are the proposed causes of IGH?", ["Chronic UV exposure (photoageing — focal melanocyte loss), ageing/somatic mutation of melanocytes, genetic predisposition (familial), HLA-DQ3, local trauma, autoimmunity (debated)"]),
 ("What does dermoscopy show?", ["Well-demarcated white areas with amoeboid/petaloid ('cloudy sky' or 'feathery') margins and absent or reduced pigment network; no perifollicular pigmentation"]),
 ("How do you differentiate IGH from guttate vitiligo by Wood's lamp?", ["IGH: off-white, less bright, no enhancement of surrounding activity; vitiligo: bright chalk-white fluorescence with sharp border; histology — vitiligo has complete absence of melanocytes"]),
 ("Is IGH a marker of any systemic disease?", ["No — it is benign; indicates cumulative sun damage, so counsel sun protection; patients with many IGH lesions often have other photodamage signs (solar lentigines, actinic keratoses)"]),
 ]),
dict(case="Linear and whorled nevoid hypermelanosis", qa=[
 ("What are Blaschko's lines and why does LWNH follow them?", ["Lines of embryonic migration/proliferation of ectodermal cells — V on the back, S-shaped on the trunk sides, linear on limbs; a post-zygotic mutation in a melanocyte or keratinocyte clone becomes visible along these lines (cutaneous mosaicism)"]),
 ("Name other disorders following Blaschko's lines.", ["Incontinentia pigmenti, hypomelanosis of Ito, epidermal naevus/ILVEN, nevus sebaceous, lichen striatus, linear LP, linear porokeratosis, Goltz syndrome, CHILD syndrome, X-linked dominant chondrodysplasia punctata (Conradi–Hünermann), segmental Darier's disease, blaschkitis"]),
 ("What investigations are needed when LWNH has extracutaneous features?", ["Neurological assessment, EEG if seizures, MRI brain; echocardiography; skeletal survey for asymmetry; ophthalmology; karyotype on cultured skin fibroblasts (blood karyotype may be normal in mosaicism) — genetic counselling"]),
 ("Does pigment fade?", ["Pigmentation is usually stable after early childhood, sometimes fades partially with age; no malignant potential"]),
 ]),
dict(case="Reticulate acropigmentation of Kitamura", qa=[
 ("What is the pathogenesis?", ["ADAM10 (a disintegrin and metalloprotease 10) loss-of-function → impaired Notch signalling in skin, affecting melanocyte homeostasis and epidermal differentiation"]),
 ("Clinical clues helping diagnosis.", ["Onset first/second decade, autosomal dominant family history, freckle-like angulated macules that are slightly atrophic/depressed, on dorsa of hands and feet, gradually extending to forearms, neck and face; palmar pits and interruptions of dermatoglyphics; darkens with sun"]),
 ("How does dyschromatosis symmetrica hereditaria differ?", ["DSH (Dohi): both hyper- and hypopigmented small macules (mottled) on dorsa of hands and feet, ADAR1 mutation, East Asians, no palmar pits; RAPK: only hyperpigmented atrophic angulated macules with palmar pits"]),
 ("Is there any malignant association?", ["No — benign cosmetic disorder; overlap with Dowling–Degos disease (shared features in some families) is recognised"]),
 ]),
dict(case="Acne excoriée", qa=[
 ("Which scale/tool helps assess skin picking?", ["Skin Picking Scale–Revised, Skin Picking Impact Scale; screen for depression (PHQ-9), anxiety (GAD-7), OCD (Y-BOCS) and body dysmorphic disorder (BDD questionnaire)"]),
 ("What is the role of SSRIs and other drugs?", ["SSRIs (fluoxetine, sertraline, fluvoxamine — often higher doses) for underlying OCD/anxiety/depression; N-acetylcysteine 1200–3000 mg/day (glutamate modulator) helps picking behaviour; doxepin/hydroxyzine for itch; low-dose antipsychotics (olanzapine, aripiprazole) in resistant cases"]),
 ("What is habit reversal therapy?", ["Behavioural therapy: awareness training (recognising triggers and urges), competing response (e.g. clenching fists, holding an object for 1 min), social support — combined with CBT; often the most effective long-term approach"]),
 ("How do you manage the skin itself?", ["Treat even mild acne effectively (topical retinoids, benzoyl peroxide, oral antibiotics or isotretinoin when indicated — reduces triggers), occlusive hydrocolloid dressings to stop picking, keep nails short, treat secondary infection; later scar and pigment treatment (peels, lasers, microneedling) once picking stops"]),
 ]),
dict(case="Perioral dermatitis", qa=[
 ("Describe the clinical features in detail.", ["Young women (also children): grouped small (1–2 mm) erythematous papules, papulovesicles and pustules on a red, mildly scaly base around the mouth, nasolabial folds and chin, characteristically sparing a narrow zone of skin next to the vermilion border; periocular/perinasal variants ('periorificial dermatitis'); burning more than itching"]),
 ("What is granulomatous periorificial dermatitis?", ["Childhood variant (prepubertal, often darker skin) with yellow-brown monomorphic papules around mouth, nose, eyes; histology granulomatous; treat with topical metronidazole/erythromycin, oral erythromycin (children <8 y) or azithromycin"]),
 ("Why do topical steroids worsen it?", ["Steroids give initial improvement (vasoconstriction, anti-inflammation) but cause rebound flare on stopping and perpetuate barrier damage, follicular overgrowth of Demodex/fusiform bacteria — steroid addiction; must stop all facial steroids (taper potent ones or switch to hydrocortisone/tacrolimus) — 'zero therapy'"]),
 ("What doses of oral tetracyclines are used?", ["Doxycycline 50–100 mg/day or minocycline 50–100 mg/day for 6–12 weeks, tapering; erythromycin/azithromycin in children and pregnancy"]),
 ]),
dict(case="Callus (callosity)", qa=[
 ("Histopathology of a callus.", ["Compact orthohyperkeratosis without parakeratosis plug, thickened granular layer may be thin, mild acanthosis; no viral cytopathic changes (vs wart); dermis may show fibrosis"]),
 ("What occupational calluses are known?", ["Occupational marks: guitar/violin players' fingertips, tailor's/cobbler's calluses, prayer nodules (knees, forehead — 'prayer mark' in Muslims), 'surfer's knots', writer's callus on middle finger, sitting calluses (ischial — Indian squatting), Russell's sign (knuckle calluses from self-induced vomiting — bulimia)"]),
 ("How do you assess the foot biomechanics?", ["Examine footwear and gait, pressure points, foot deformities (hallux valgus, hammer toes, pes cavus), podoscope/pedobarography; refer to podiatrist/orthotist for offloading insoles"]),
 ("Complications in insensate feet.", ["Callus acts like a stone in the shoe — haemorrhage beneath the callus (pre-ulcerative sign) → neuropathic (mal perforans) ulcer, infection, osteomyelitis; routine paring and protective MCR footwear are preventive"]),
 ]),
dict(case="Corn (clavus)", qa=[
 ("Histopathology of a corn.", ["Cup-shaped depression of the epidermis filled with a dense central column of parakeratotic keratin (the core) pressing into the dermis; surrounding hyperkeratosis; thinned granular layer beneath the core"]),
 ("Why are corns painful?", ["The central keratin core (inverted cone) presses on dermal nerve endings and bursa over a bony prominence; soft corns can macerate and become infected"]),
 ("Where do soft corns occur and why?", ["Between toes (usually 4th web space) where a bony prominence (condyle of proximal phalanx) presses on the adjacent toe; moisture keeps them soft and white (macerated); may mimic interdigital tinea"]),
 ("What surgical or orthopaedic options exist for recurrent corns?", ["Correct underlying deformity — exostectomy, condylectomy, hammer-toe correction; silicone toe separators and padding; avoid tight pointed footwear"]),
 ]),
dict(case="Lichen spinulosus", qa=[
 ("Describe the clinical features.", ["Children/adolescents (boys more): grouped skin-coloured to slightly red follicular papules each topped by a fine horny spine, forming well-defined round plaques 2–6 cm on neck, trunk, extensor limbs, buttocks; feel like a nutmeg grater; asymptomatic or mildly itchy; symmetrical"]),
 ("Name the associations.", ["Atopy, seborrhoeic dermatitis; also reported with HIV, Hodgkin lymphoma, alcoholism, Crohn's disease, vitamin A deficiency (phrynoderma-like), drugs (gold, thallium); 'generalised lichen spinulosus' in adults should prompt systemic evaluation"]),
 ("Which other disorders produce follicular spiny papules?", ["Keratosis pilaris, phrynoderma, PRP, Darier's disease, lichen planopilaris, follicular eczema, trichodysplasia spinulosa (polyomavirus in immunosuppressed), multiple minute digitate hyperkeratoses, spiny keratoderma, myeloma-associated follicular spicules"]),
 ("Prognosis?", ["Self-limiting — often resolves by puberty; recurrences possible; keratolytics speed improvement"]),
 ]),
dict(case="Nevus comedonicus", qa=[
 ("What is the genetic basis?", ["Post-zygotic mosaic mutation of NEK9 (also FGFR2 in some) in the follicular unit — a follicular hamartoma; NEK9 mutations also seen in nevus comedonicus syndrome"]),
 ("What is nevus comedonicus syndrome?", ["Nevus comedonicus with extracutaneous anomalies — CNS (seizures, developmental delay, EEG abnormalities), ocular (cataract), skeletal (scoliosis, hemivertebrae, syndactyly) — an epidermal naevus syndrome; needs neurological/orthopaedic assessment"]),
 ("Complications.", ["Inflammatory variant with recurrent cysts, abscesses, sinuses and scarring (acne conglobata/hidradenitis-like), secondary infection; rarely malignancy in long-standing lesions"]),
 ("Dermoscopy findings.", ["Multiple keratin plugs ('comedo-like openings') — dark-brown to black round plugs, clustered in a linear distribution"]),
 ]),
dict(case="Nevus sebaceous (of Jadassohn)", qa=[
 ("What is the genetic basis?", ["Post-zygotic HRAS (≈ 90%) or KRAS mutations — RAS mosaicism; same mutations in Schimmelpenning syndrome and phacomatosis pigmentokeratotica"]),
 ("Which tumours develop in nevus sebaceous?", ["Mostly benign, after puberty: trichoblastoma (commonest — previously misdiagnosed as BCC), syringocystadenoma papilliferum (second commonest), sebaceoma, apocrine adenoma/hidrocystoma, tricholemmoma", "Malignant (rare <1–2%): BCC, SCC, sebaceous carcinoma, apocrine carcinoma, porocarcinoma — usually in adults"]),
 ("Clinical appearance at birth vs puberty.", ["Birth/infancy: smooth, hairless, yellow-orange, waxy, slightly raised plaque on scalp (linear/oval) — alopecic; Puberty: verrucous, pebbly, thicker (sebaceous gland hyperplasia under androgen influence); adulthood: tumour development (nodules within)"]),
 ("Timing of excision — current view?", ["Prophylactic excision in childhood is no longer mandatory as malignant change is rare; excise for cosmesis, symptoms, or new nodules/ulceration; observation with periodic examination is acceptable; if excising, before adolescence gives smaller scars under local anaesthesia"]),
 ]),
dict(case="Nevus spilus (speckled lentiginous nevus)", qa=[
 ("Histopathology.", ["Background macule: lentigo-simplex-like basal hyperpigmentation with slightly increased melanocytes; dark speckles: junctional, compound or intradermal naevi, sometimes Spitz/blue naevi"]),
 ("What is phacomatosis pigmentokeratotica?", ["Co-existence of speckled lentiginous naevus (papular type) and nevus sebaceous (HRAS mosaicism), sometimes with neurological and skeletal anomalies"]),
 ("What is phacomatosis pigmentovascularis?", ["Co-existence of vascular malformation (port-wine stain/ cutis marmorata) with pigmentary naevi — dermal melanocytosis (cesioflammea), nevus spilus (spilorosea), or both; GNA11/GNAQ mosaicism; may have Sturge–Weber/KT features"]),
 ("How should you follow a large nevus spilus?", ["Photography and dermoscopy annually; examine dark speckles for change; biopsy any enlarging, irregular or nodular area — melanoma risk is low but higher in large/zosteriform/papular types"]),
 ]),
dict(case="Acrochordon (skin tag)", qa=[
 ("What is Birt–Hogg–Dubé syndrome?", ["Autosomal dominant FLCN mutation: multiple fibrofolliculomas, trichodiscomas and acrochordons on face/neck, lung cysts with spontaneous pneumothorax, renal tumours (chromophobe/oncocytic) — screen kidneys with MRI"]),
 ("Can skin tags be a marker of systemic disease?", ["Multiple skin tags associated with insulin resistance/type 2 diabetes, obesity, metabolic syndrome, acanthosis nigricans, dyslipidaemia, pregnancy (hormonal), and possibly colonic polyps (controversial); check fasting sugar, lipids in multiple tags"]),
 ("What causes a skin tag to become painful and dark?", ["Torsion of the stalk with infarction — black, tender, may auto-amputate; differentiate from a thrombosed haemangioma or melanoma (biopsy if doubtful)"]),
 ("Dermoscopy of a skin tag.", ["Pedunculated lesion with central or 'comma'/hairpin vessels and skin-coloured/light-brown structureless areas; cerebriform features if seborrhoeic keratosis-like"]),
 ]),
dict(case="Milium / colloid milium", qa=[
 ("What are the types of colloid milium?", ["Adult type (commonest): sun-exposed face/dorsa of hands, middle-aged men with heavy sun exposure or petroleum/hydroquinone exposure — degenerated elastic fibres (elastotic)", "Juvenile (childhood, before puberty — keratinocyte-derived, amyloid-like, familial/ligneous conjunctivitis association), nodular colloid degeneration (single large nodule), pigmented colloid milium (hydroquinone-related ochronosis-like)"]),
 ("Histopathology of colloid milium.", ["Fissured homogeneous pale eosinophilic colloid masses in the papillary dermis with clefts, separated from the epidermis by a thin grenz zone; adult type — elastic origin; juvenile — derived from keratinocytes (keratin positive); Congo red may be weakly positive"]),
 ("What is milia en plaque?", ["Multiple milia grouped on an erythematous oedematous plaque, usually behind the ears/eyelids — associated with DLE, lichen planopilaris, pseudoxanthoma elasticum; treated by extraction, retinoids, minocycline, surgery"]),
 ("Which conditions cause secondary milia?", ["Subepidermal blistering diseases healing with milia — epidermolysis bullosa (dystrophic), porphyria cutanea tarda, bullous pemphigoid, EBA, bullous LP; after dermabrasion, laser resurfacing, burns, potent topical steroids, radiotherapy"]),
 ]),
]
