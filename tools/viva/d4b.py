# Viva — slot D4 (part B): Dowling–Degos, freckles, IGH, lentigo, LWNH, pityriasis alba, RAPK
# Own words. Topics guided by the previous-year question book (Sahana P Raju) — pigmentary chapter (types of lentigines,
# genetic hyper/hypopigmentation, non-naevoid hyperpigmentation, reticulate pigmentary disorders); facts checked with IADVL 5e.
PYQ = "Previous-year PG question papers (Sahana P Raju, Solved Papers Dermatology)"
IA = "IADVL Textbook of Dermatology 5e"
RETIC = ["Dowling–Degos disease (flexural), reticulate acropigmentation of Kitamura (dorsa of hands/feet with palmar pits), Galli–Galli disease (DDD + acantholysis), dyschromatosis symmetrica hereditaria (Dohi — acral hypo+hyperpigmented macules, ADAR1), dyschromatosis universalis hereditaria, Naegeli–Franceschetti–Jadassohn and dermatopathia pigmentosa reticularis (keratin 14, absent dermatoglyphics), dyskeratosis congenita (reticulate pigmentation, nail dystrophy, leukoplakia), X-linked reticulate pigmentary disorder, incontinentia pigmenti stage 3, confluent and reticulated papillomatosis, prurigo pigmentosa, macular amyloidosis, erythema ab igne, poikiloderma"]

D = [
dict(case="Dowling–Degos disease", src=f"{PYQ}; {IA} (Reticulate pigmentary disorders)",
 qa=[
 ("What is Dowling–Degos disease (DDD)?", ["Rare autosomal dominant reticulate pigmentary disorder of flexures ('reticulate pigmented anomaly of the flexures'), onset in adolescence/adulthood, slowly progressive", "Genes: KRT5 (loss of function), POFUT1, POGLUT1, PSENEN (latter also with hidradenitis suppurativa)"]),
 ("Clinical features.", ["Small brown-black macules coalescing into reticulate (net-like) pigmentation in axillae, groin, neck, inframammary, antecubital, inner thighs; may extend to trunk and face", "Comedo-like dark follicular papules on back/neck, pitted perioral acneiform scars, epidermoid cysts, hidradenitis suppurativa (PSENEN), mild itch"]),
 ("Histopathology.", ["Filiform/antler-like elongation of thin, pigmented rete ridges ('finger-like' downgrowths) with basal hyperpigmentation, including follicular infundibula; horn cysts; no increase in melanocytes", "Galli–Galli disease: same + suprabasal acantholysis"]),
 ("Enumerate reticulate pigmentary disorders.", RETIC),
 ("Differential diagnosis.", ["Acanthosis nigricans (velvety, not reticulate), reticulate acropigmentation of Kitamura (acral), Haber's syndrome (rosacea-like face + DDD-like), frictional pigmentation, confluent and reticulated papillomatosis, Galli–Galli, erythrasma, LPP inverse"]),
 ("Treatment.", ["Difficult; reassurance; topical retinoids, hydroquinone, azelaic acid (modest); Er:YAG/CO2/Q-switched lasers (variable); oral retinoids for comedonal component; treat associated hidradenitis"]),
 ],
 spot=["Reticulate flexural pigmentation + comedo-like papules + perioral pits — Dowling–Degos", "Antler-like pigmented rete ridges"]),

dict(case="Freckles (ephelides)", src=f"{PYQ}; {IA} (Melanocytic macules)",
 qa=[
 ("What are freckles?", ["Small (1–5 mm) light-brown, well-defined macules on sun-exposed skin (face, arms, shoulders) of fair-skinned people (Fitzpatrick I–II), appearing in early childhood (2–4 y), darkening in summer and fading in winter"]),
 ("Genetics and pathogenesis.", ["MC1R variants (red hair colour phenotype — red hair, fair skin), IRF4, ASIP; UV-induced increase in melanin synthesis and transfer by a normal number of melanocytes (increased activity, larger melanosomes)", "Marker of UV sensitivity and higher melanoma/NMSC risk"]),
 ("Histopathology.", ["Increased melanin in basal keratinocytes; melanocyte number normal (sometimes fewer but larger), no elongation of rete ridges — unlike lentigo"]),
 ("Differentiate freckle from lentigo simplex and solar lentigo.", ["Freckle: sun-dependent darkening, fades in winter, normal melanocyte number, no rete elongation, childhood, fair skin", "Lentigo simplex: not sun-dependent, any site incl. mucosa, does not fade, increased melanocytes along elongated rete ridges", "Solar lentigo: older adults, chronic sun damage, larger, persistent, elongated club-shaped pigmented rete"]),
 ("Syndromic freckling.", ["Axillary/inguinal freckling — NF1 (Crowe's sign), Legius syndrome", "Xeroderma pigmentosum — early, severe freckling and poikiloderma in sun-exposed skin of infants", "Centrofacial lentiginosis, Peutz–Jeghers (lentigines, not freckles)"]),
 ("Management.", ["Reassurance; photoprotection (sunscreen, hats); cosmetic — Q-switched/picosecond lasers (532 nm), IPL, cryotherapy, depigmenting creams; recurrence with sun exposure", "Skin cancer awareness and self-examination in people with many freckles"]),
 ],
 spot=["Small brown macules that darken in summer and fade in winter — freckles; normal melanocyte count"]),

dict(case="Idiopathic guttate hypomelanosis", src=f"{PYQ}; {IA} (Acquired hypomelanoses)",
 qa=[
 ("What is idiopathic guttate hypomelanosis (IGH)?", ["Common acquired leucoderma with multiple small (2–5 mm), discrete, porcelain-white, round/angular macules on chronically sun-exposed extensor forearms and shins; increases with age (>40 y), women more; considered a sign of photoageing"]),
 ("Pathogenesis.", ["Chronic UV exposure, ageing (somatic mutations of melanocytes), local trauma/friction; HLA-DQ3 association; reduced number of melanocytes and melanin in lesions"]),
 ("Histopathology.", ["Basket-weave orthokeratosis, flattened rete, reduced melanin and decreased (not absent) DOPA-positive melanocytes"]),
 ("Differential diagnosis.", ["Vitiligo punctata/confetti vitiligo (progressive, Koebner), leprosy (sensory loss), pityriasis versicolor (scale, KOH), post-inflammatory hypopigmentation, progressive macular hypomelanosis (trunk, red follicular fluorescence — Cutibacterium acnes), lichen sclerosus (atrophic), chemical leucoderma, achromic verrucae (flat warts), tinea, guttate morphoea, Darier's (leukoderma)"]),
 ("Treatment.", ["Reassurance — benign, cosmetic", "Photoprotection to prevent new lesions", "Options: superficial cryotherapy (2–5 s), focal dermabrasion/needling, fractional CO2/Er:YAG laser, excimer laser 308 nm, topical tacrolimus/retinoids, 88% phenol spot application, 5-FU, mini-punch grafts — variable results"]),
 ],
 spot=["Multiple porcelain-white guttate macules on shins/forearms of older adults — IGH"]),

dict(case="Lentigo", src=f"{PYQ}; {IA} (Lentigines)",
 qa=[
 ("Define lentigo.", ["Small, well-circumscribed, uniformly brown-black macule (1–5 mm, solar types larger) due to increased number of melanocytes along the basal layer with elongated pigmented rete ridges; does not fade in winter"]),
 ("Discuss the various types of lentigines (PYQ).", ["Lentigo simplex: childhood, any site including mucosa/palms, not sun-related", "Solar (senile/actinic) lentigo — 'age spots/liver spots': middle-aged/elderly, sun-exposed dorsa of hands, face; PUVA lentigines (after PUVA — larger, darker, atypical), sunburn (ink-spot) lentigo — reticulate black ('ink-spot') after sunburn", "Mucosal (labial/genital) melanotic macules/lentigines", "Agminated (segmental cluster)", "Lentigo maligna — melanoma in situ on chronically sun-damaged face of elderly (not a true lentigo)", "Syndromic lentiginoses: Peutz–Jeghers (perioral, lips, buccal mucosa, digits; GI hamartomatous polyps, cancer risk — STK11), LEOPARD/Noonan syndrome with multiple lentigines (PTPN11; Lentigines, ECG abnormalities, Ocular hypertelorism, Pulmonary stenosis, Abnormal genitalia, Retarded growth, Deafness), Carney complex (LAMB/NAME — lentigines, atrial myxomas, blue naevi, endocrine overactivity, PRKAR1A), Laugier–Hunziker (oral/lip lentigines + longitudinal melanonychia, benign), Cowden, Bannayan–Riley–Ruvalcaba (penile lentigines, PTEN), centrofacial lentiginosis (Touraine), inherited patterned lentiginosis (black skin), xeroderma pigmentosum"]),
 ("Histopathology of solar lentigo.", ["Elongated club-shaped/budding rete ridges with heavy basal pigmentation and slightly increased melanocytes, solar elastosis, no nests (vs junctional naevus)"]),
 ("Differential diagnosis.", ["Freckle, junctional naevus (nests), seborrhoeic keratosis (flat — reticulated SK), pigmented actinic keratosis, lentigo maligna (asymmetric, variegated, irregular border, dermoscopy — annular granular, asymmetric follicular openings, rhomboid structures), lichen planus-like keratosis, café-au-lait macule"]),
 ("Dermoscopy.", ["Solar lentigo: light-brown fingerprint-like or reticular pattern, moth-eaten sharp border, homogeneous structureless areas; mucosal: parallel/ring-like patterns"]),
 ("Treatment.", ["Benign — photoprotection", "Cryotherapy, Q-switched (532/755 nm) or picosecond lasers, IPL, chemical peels (TCA, glycolic), topical retinoids, hydroquinone/triple cream, thiamidol", "Biopsy any atypical lesion before destructive treatment (to exclude lentigo maligna)", "Syndromic: screening for associated systemic disease (Peutz–Jeghers — endoscopy; Carney — echocardiography)"]),
 ],
 spot=["Perioral and buccal lentigines + GI polyps — Peutz–Jeghers (STK11)", "Lentigines + myxomas + endocrine overactivity — Carney complex", "Biopsy atypical facial 'lentigo' in elderly — lentigo maligna"]),

dict(case="Linear and whorled nevoid hypermelanosis", src=f"{PYQ}; {IA} (Mosaic pigmentary disorders)",
 qa=[
 ("What is linear and whorled nevoid hypermelanosis (LWNH)?", ["Sporadic mosaic disorder of pigmentation with streaks and whorls of hyperpigmentation along Blaschko's lines, appearing within the first weeks of life, progressing for 1–2 years then stabilising; no preceding inflammation or verrucous stage", "Caused by cutaneous mosaicism (chromosomal mosaicism — trisomy 7, 14, 18, 20, X-chromosome abnormalities; KITLG mutations)"]),
 ("Clinical features.", ["Brown macules arranged in linear streaks and whorls along Blaschko's lines on trunk and limbs; midline demarcation; spares palms, soles, mucosa, eyes", "Usually isolated; ~20–30% have extracutaneous anomalies — CNS (intellectual disability, seizures, cerebral palsy), cardiac (septal defects), musculoskeletal (asymmetry, scoliosis) — 'pigmentary mosaicism'"]),
 ("Histopathology.", ["Increased basal layer pigmentation, prominent melanocytes, absence of pigment incontinence (unlike incontinentia pigmenti)"]),
 ("Differential diagnosis.", ["Incontinentia pigmenti stage 3 (preceded by vesicles and verrucous lesions, female, NEMO), epidermal naevus (raised, verrucous), hypomelanosis of Ito (hypopigmented whorls — the reverse pattern), linear morphoea, lichen striatus (papular, self-limited), linear LP pigmentosus, segmental café-au-lait, Goltz syndrome, X-linked reticulate pigmentary disorder, Naegeli syndrome"]),
 ("Management.", ["Reassurance; examine for systemic anomalies (development, neurology, heart, skeleton); chromosomal analysis/karyotype of skin fibroblasts or blood if anomalies", "Pigmentation tends to persist (may fade slightly); camouflage; lasers ineffective in general"]),
 ],
 spot=["Whorled brown streaks along Blaschko's lines from infancy without blisters — LWNH", "Hypomelanosis of Ito is the hypopigmented counterpart"]),

dict(case="Pityriasis alba", src=f"{PYQ}; {IA} (Hypomelanoses; eczemas)",
 qa=[
 ("What is pityriasis alba?", ["Common, benign, low-grade eczematous dermatitis in children (3–16 y) causing ill-defined, round/oval, hypopigmented, finely scaly patches on face (cheeks), upper arms, neck; minor criterion of atopic dermatitis"]),
 ("Aetiology.", ["Atopy and xerosis, sun exposure (more visible after summer tanning of surrounding skin), excessive bathing/soaps, low serum copper, Malassezia/ Streptococcus hypotheses (unproven)", "Hypopigmentation is post-inflammatory — reduced melanin transfer and smaller melanosomes"]),
 ("Clinical stages.", ["Early: slightly erythematous patches with ill-defined raised border", "Later: hypopigmented, fine branny scales; multiple 0.5–5 cm patches; asymptomatic or mild itch", "Extensive pityriasis alba — trunk in older children/adults"]),
 ("Differential diagnosis.", ["Vitiligo (depigmented, sharp border, no scale, Wood's lamp bright), pityriasis versicolor (KOH positive, upper trunk), indeterminate leprosy (sensory loss, nerve thickening — important in India), nevus depigmentosus (stable since birth), post-inflammatory hypopigmentation, hypopigmented MF (persistent, trunk, adults), progressive macular hypomelanosis, seborrhoeic dermatitis, tinea faciei"]),
 ("Investigations.", ["Clinical; Wood's lamp (no accentuation like vitiligo), KOH to exclude PV/tinea, sensation testing; biopsy only for atypical persistent lesions"]),
 ("Management.", ["Reassurance — self-limiting over months to years", "Emollients, mild soaps, gentle photoprotection", "Mild topical steroid (hydrocortisone 1%) for short periods or tacrolimus/pimecrolimus — speeds resolution", "Extensive/persistent: NB-UVB or PUVAsol (older children)"]),
 ],
 spot=["Ill-defined scaly hypopigmented patches on a child's cheeks — pityriasis alba", "Check sensation to exclude indeterminate leprosy"]),

dict(case="Reticulate acropigmentation of Kitamura", src=f"{PYQ}; {IA} (Reticulate pigmentary disorders)",
 qa=[
 ("What is reticulate acropigmentation of Kitamura (RAK)?", ["Rare autosomal dominant disorder (ADAM10 mutation) with reticulate, slightly depressed (atrophic) brown macules on the dorsa of hands and feet, appearing in childhood/adolescence and slowly spreading proximally; first described in Japan, reported from India"]),
 ("Clinical features.", ["Angulated, freckle-like, slightly atrophic pigmented macules in a reticulate pattern on dorsa of hands and feet, extending to limbs, neck, face with age; darkens with sun", "Palmoplantar pits and breaks in dermatoglyphics (characteristic); no hypopigmentation; no systemic disease", "Overlap with Dowling–Degos disease reported"]),
 ("Histopathology.", ["Thinned epidermis with elongated thin rete ridges, increased basal melanin and melanocytes, mild hyperkeratosis — like a 'mini Dowling–Degos'"]),
 ("Enumerate reticulate pigmentary disorders and key differentials.", RETIC + ["Key differentials for acral reticulate pigmentation: dyschromatosis symmetrica hereditaria (hypo + hyperpigmented, no pits), Dowling–Degos (flexural), Naegeli syndrome (no dermatoglyphics, hypohidrosis), acropigmentation of Dohi, freckles, lentigines"]),
 ("Treatment.", ["No effective therapy; photoprotection; topical depigmenting agents and retinoids may lighten; Q-switched lasers variably helpful; reassurance and genetic counselling"]),
 ],
 spot=["Reticulate atrophic pigmentation on dorsa of hands + palmar pits — Kitamura (ADAM10)"]),
]
