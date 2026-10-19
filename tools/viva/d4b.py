# Viva — slot D4 (part B): Dowling–Degos, freckles, IGH, lentigo, LWNH, pityriasis alba, RAPK
# Own words. Topics guided by the previous-year question book (Sahana P Raju) — pigmentary chapter (types of
# lentigines, genetically determined/ reticulate pigmentary disorders, hypomelanoses); facts checked with IADVL 5e.
PYQ = "Previous-year PG question papers (Sahana P Raju, Solved Papers Dermatology)"
IA = "IADVL Textbook of Dermatology 5e"
RETIC = ["Dowling–Degos disease (flexural reticulate pigmentation, comedo-like pits — KRT5, POFUT1, POGLUT1)", "Reticulate acropigmentation of Kitamura (dorsa of hands/feet, palmar pits — ADAM10)", "Galli–Galli disease (DDD with acantholysis)", "Dyschromatosis symmetrica hereditaria (Dohi — acral mottled hypo/hyper — ADAR1) and dyschromatosis universalis hereditaria", "Naegeli–Franceschetti–Jadassohn syndrome and dermatopathia pigmentosa reticularis (KRT14 — absent dermatoglyphics)", "Dyskeratosis congenita (reticulate pigmentation, nail dystrophy, oral leukoplakia — telomere genes)", "Incontinentia pigmenti stage 3, X-linked reticulate pigmentary disorder, Haber syndrome, confluent and reticulated papillomatosis (acquired)"]

D = [
dict(case="Dowling–Degos disease", src=f"{PYQ}; {IA} (Reticulate pigmentary disorders)",
 qa=[
 ("What is Dowling–Degos disease (DDD)?", ["Rare autosomal dominant genodermatosis ('reticulate pigmented anomaly of the flexures') with progressive reticulate hyperpigmentation of flexures; genes — KRT5 (keratin 5), POFUT1, POGLUT1, PSENEN", "Onset usually 3rd–4th decade, slowly progressive"]),
 ("Clinical features.", ["Reticulate brown-black macules coalescing in axillae, groin, neck, inframammary, antecubital and intergluteal folds", "Comedo-like dark follicular papules on back and neck, pitted perioral acneiform scars; occasionally epidermoid cysts, hidradenitis suppurativa association, seborrhoeic keratosis-like papules"]),
 ("Histopathology.", ["Filiform (finger-like/antler-like) downward elongation of thin pigmented rete ridges from epidermis and follicular infundibula ('antler-like'), with pigment at the tips, horn cysts; no increase in melanocyte number", "Galli–Galli disease: same + suprabasal acantholysis"]),
 ("Enumerate reticulate pigmentary disorders (PYQ: genetically determined pigmentary disorders).", RETIC),
 ("Differential diagnosis.", ["Acanthosis nigricans (velvety, no comedones), RAPK (acral), Galli–Galli, confluent and reticulated papillomatosis, Haber syndrome (rosacea-like face + flexural DDD-like), frictional melanosis, Addison's", "Histology distinguishes from adenoid seborrhoeic keratosis (similar pattern)"]),
 ("Treatment.", ["Difficult; cosmetic concern: topical retinoids (adapalene/tretinoin), hydroquinone, azelaic acid, Er:YAG/ CO2 or Q-switched lasers, IPL (variable)", "Genetic counselling"]),
 ],
 spot=["Flexural reticulate pigmentation + comedo-like papules + perioral pits — Dowling–Degos", "Antler-like rete ridges"]),

dict(case="Freckles (ephelides)", src=f"{PYQ}; {IA} (Hypermelanoses)",
 qa=[
 ("What are freckles?", ["Small (1–5 mm) light-brown/red-brown macules on sun-exposed skin of fair-skinned (Fitzpatrick I–II) individuals; appear in early childhood (~age 3), darken in summer and fade in winter", "Strongly associated with red hair/ MC1R variants (red hair colour alleles) — markers of UV sensitivity and melanoma risk"]),
 ("Histopathology.", ["Increased melanin in basal keratinocytes with normal number of melanocytes (which are larger and more active); no elongation of rete ridges — unlike lentigo"]),
 ("Differentiate freckles from lentigines.", ["Freckles: childhood onset, sun-dependent (fade in winter), sun-exposed sites only, lighter colour, normal melanocyte number, no rete elongation", "Lentigines: any age, not sun-dependent, can be on any site including mucosa, darker, increased melanocytes along basal layer, elongated rete ridges"]),
 ("Associations.", ["Axillary/inguinal freckling (Crowe's sign — NF1), xeroderma pigmentosum (freckling in first years of life with marked photosensitivity), Peutz–Jeghers (perioral lentigines — not true freckles), LEOPARD/Noonan with multiple lentigines"]),
 ("Management.", ["Reassurance — benign; photoprotection (broad-spectrum sunscreen, clothing) — also reduces skin cancer risk; counsel skin self-examination in fair, freckled individuals", "Cosmetic: hydroquinone/azelaic acid, chemical peels, cryotherapy, Q-switched/picosecond lasers, IPL — recurrence with sun exposure"]),
 ],
 spot=["Sun-exposed tiny brown macules darkening in summer in fair child — freckles", "Axillary freckling — NF1"]),

dict(case="Idiopathic guttate hypomelanosis", src=f"{PYQ}; {IA} (Hypomelanoses)",
 qa=[
 ("What is idiopathic guttate hypomelanosis (IGH)?", ["Common acquired benign condition of multiple small (2–5 mm), well-defined porcelain-white guttate macules on chronically sun-exposed extensor forearms and shins; increases with age (>40 years), women noticed earlier", "Considered a sign of photoageing (UV-induced melanocyte senescence), also genetic and HLA-DQ3 association"]),
 ("Clinical features.", ["Round/angular white macules with sharp borders, no scaling, no inflammation, stable size, do not enlarge or coalesce; asymptomatic", "Shins and forearms (dorsal), occasionally face, trunk; never on palms/soles or mucosa"]),
 ("Histopathology.", ["Basket-weave hyperkeratosis, epidermal atrophy with flattened rete ridges, decreased melanin and reduced number of DOPA-positive melanocytes"]),
 ("Differential diagnosis.", ["Vitiligo (larger, progressive, any site), guttate morphoea/lichen sclerosus (atrophic, shiny), pityriasis versicolor (scale, KOH), post-inflammatory hypopigmentation, leucoderma punctata (after PUVA), progressive macular hypomelanosis (trunk, confluent), tuberous sclerosis confetti macules, chemical leucoderma, indeterminate leprosy (sensory)"]),
 ("Treatment.", ["Reassurance and sun protection", "Options for cosmetic improvement: superficial cryotherapy (2–5 s), topical tacrolimus/pimecrolimus, topical retinoids, localised dermabrasion, fractional CO2 or excimer laser, 88% phenol spot application, 5-FU with microneedling, suction blister grafts (variable results)"]),
 ],
 spot=["Multiple tiny porcelain-white macules on sun-exposed shins of middle-aged — IGH"]),

dict(case="Lentigo", src=f"{PYQ}; {IA} (Lentigines)",
 qa=[
 ("Define lentigo.", ["Small (usually <5 mm), well-circumscribed, uniformly brown to brown-black macule due to increased number of melanocytes along the basal layer with elongated pigmented rete ridges; does not darken with sun (unlike freckle)"]),
 ("Discuss the various types of lentigines (PYQ).", ["Lentigo simplex: childhood onset, any site including mucosa, not sun-related", "Solar (actinic/senile) lentigo — 'age/liver spots': sun-exposed areas of older adults (dorsa of hands, face), larger, irregular; marker of photodamage; may evolve to reticulated seborrhoeic keratosis or lichen planus-like keratosis", "PUVA lentigines: stellate dark lentigines after PUVA — atypical melanocytes", "Ink-spot (reticulated black solar) lentigo: very dark, irregular, fair skin after sunburn", "Mucosal: labial melanotic macule, genital (penile/vulval) lentiginosis, oral", "Lentiginosis syndromes: Peutz–Jeghers (perioral/buccal lentigines + hamartomatous GI polyps — STK11; GI, breast, pancreatic cancer risk), LEOPARD/Noonan syndrome with multiple lentigines (PTPN11 — Lentigines, ECG conduction defects, Ocular hypertelorism, Pulmonary stenosis, Abnormal genitalia, Retardation of growth, Deafness), Carney complex (LAMB/NAME — PRKAR1A; cardiac myxomas, endocrine tumours), Laugier–Hunziker (acquired oral and nail pigmentation, benign), Cowden/Bannayan–Riley–Ruvalcaba (penile lentigines — PTEN), centrofacial lentiginosis, partial unilateral lentiginosis, xeroderma pigmentosum"]),
 ("Histopathology of solar lentigo.", ["Elongated club/bud-shaped rete ridges with basal hyperpigmentation, increased (not nested, non-atypical) melanocytes, solar elastosis"]),
 ("Differential diagnosis.", ["Freckle, junctional naevus (nests on histology), lentigo maligna (irregular, enlarging, asymmetric follicular pigmentation on dermoscopy — biopsy), pigmented actinic keratosis, flat seborrhoeic keratosis, café-au-lait macule, pigmented BCC"]),
 ("What are the warning signs for lentigo maligna?", ["Asymmetry, irregular borders, variegation, enlargement on face of elderly; dermoscopy — asymmetric pigmented follicular openings, rhomboidal structures, annular-granular pattern, grey dots — needs biopsy"]),
 ("Management.", ["Photoprotection; topical hydroquinone, tretinoin, triple combination", "Cryotherapy, Q-switched (532 nm Nd:YAG, ruby, alexandrite) and picosecond lasers, IPL, chemical peels", "Evaluate syndromic lentiginosis (cardiac, GI, endocrine) when multiple/mucosal from childhood"]),
 ],
 spot=["Perioral and buccal lentigines + GI polyps — Peutz–Jeghers", "LEOPARD syndrome — PTPN11", "Enlarging irregular facial pigment in elderly — rule out lentigo maligna"]),

dict(case="Linear and whorled nevoid hypermelanosis", src=f"{PYQ}; {IA} (Mosaic pigmentary disorders)",
 qa=[
 ("What is linear and whorled nevoid hypermelanosis (LWNH)?", ["Sporadic mosaic disorder of pigmentation with streaks and whorls of macular hyperpigmentation following Blaschko's lines, appearing at birth or in the first weeks of life; progresses in first 1–2 years then stabilises", "Mosaic chromosomal abnormalities (trisomy 7, 18, X-chromosome mosaicism) in some"]),
 ("Clinical features.", ["Brown macules in linear streaks and whorls ('marble-cake' pattern) on trunk and limbs, sparing face, palms, soles, mucosa, eyes; no preceding inflammation, vesicles or verrucous stages", "Usually isolated, but may have associated anomalies (CNS — seizures, developmental delay; cardiac defects, skeletal asymmetry) — 'LWNH syndrome'"]),
 ("Histopathology.", ["Increased basal layer melanin, prominent melanocytes; no pigment incontinence (differentiates from incontinentia pigmenti stage 3)"]),
 ("Differential diagnosis.", ["Incontinentia pigmenti (X-linked dominant, girls; inflammatory vesicular → verrucous → hyperpigmented → atrophic stages; pigment incontinence; eye, teeth, CNS)", "Linear epidermal naevus (raised, verrucous), hypomelanosis of Ito (hypopigmented whorls — the 'negative' counterpart), Goltz syndrome (focal dermal hypoplasia), segmental pigmentation disorder, chimerism, X-linked reticulate pigmentary disorder"]),
 ("Management.", ["Reassurance; screen for systemic anomalies (development, neurology, cardiac, skeletal); genetic consultation/karyotype of skin fibroblasts if systemic features", "No effective treatment; camouflage; lasers rarely help"]),
 ],
 spot=["Swirls of brown pigment along Blaschko lines from infancy without preceding blisters — LWNH", "No pigment incontinence (vs IP)"]),

dict(case="Pityriasis alba", src=f"{PYQ}; {IA} (Hypopigmentation)",
 qa=[
 ("What is pityriasis alba (PA)?", ["Common benign condition of children and adolescents (3–16 y) with ill-defined, slightly scaly hypopigmented patches on the face (cheeks), sometimes neck, upper arms; low-grade eczematous dermatitis — minor criterion of atopic dermatitis", "More noticeable in darker skin and after summer (surrounding skin tans)"]),
 ("Clinical stages.", ["Initially mildly erythematous with slightly raised border → hypopigmented patch with fine branny scale → smooth hypopigmented patch", "Asymptomatic or mild itch; 1–4 cm, multiple; extensive PA on trunk (variant) in adults"]),
 ("Aetiology.", ["Atopy, xerosis, sun exposure (UV), frequent bathing/soaps, possibly Malassezia and low serum copper; post-inflammatory hypopigmentation from reduced melanosome transfer due to inflammation/oedema"]),
 ("Histopathology.", ["Non-specific mild spongiotic dermatitis, hyperkeratosis, parakeratosis, reduced melanin, normal or slightly reduced melanocytes"]),
 ("Differential diagnosis.", ["Pityriasis versicolor (KOH positive, upper trunk), vitiligo (chalk-white, sharp, Wood's bright), indeterminate leprosy (sensation, nerve), nevus depigmentosus (congenital stable), post-inflammatory hypopigmentation, seborrhoeic dermatitis, hypopigmented MF (persistent trunk patches in adults), progressive macular hypomelanosis, tinea faciei"]),
 ("Management.", ["Reassurance — self-limiting (months to years), repigments", "Emollients, gentle soap substitute, sunscreen to reduce contrast", "Mild topical steroid (hydrocortisone 1%) short course or calcineurin inhibitors (tacrolimus/pimecrolimus) for scaly/inflamed patches; calcitriol; excimer laser for persistent extensive PA"]),
 ],
 spot=["Ill-defined scaly hypopigmented cheek patches in atopic child — pityriasis alba", "Check sensation to exclude leprosy"]),

dict(case="Reticulate acropigmentation of Kitamura", src=f"{PYQ}; {IA} (Reticulate pigmentary disorders)",
 qa=[
 ("What is reticulate acropigmentation of Kitamura (RAPK)?", ["Rare autosomal dominant disorder (ADAM10 loss-of-function) of slightly depressed, angulated, reticulate brown freckle-like macules on the dorsa of hands and feet, starting in childhood/adolescence and slowly spreading proximally; worse with sun exposure", "Palmar and plantar pits (breaks in dermatoglyphics) — characteristic"]),
 ("Histopathology.", ["Epidermal atrophy with thin elongated rete ridges, increased basal pigmentation and melanocytes at the tips of rete — atrophic lentigo-like pattern"]),
 ("Differential diagnosis.", ["Dyschromatosis symmetrica hereditaria (hypo + hyperpigmented mottling on dorsa, Japanese — ADAR1)", "Dowling–Degos disease (flexural; overlap cases exist)", "Acropigmentation of Dohi, freckles, lentigines, Peutz–Jeghers, Naegeli–Franceschetti–Jadassohn, dermatopathia pigmentosa reticularis, acral pigmentation of B12 deficiency, Addison's"]),
 ("Enumerate reticulate pigmentary disorders.", RETIC),
 ("Treatment.", ["No definitive therapy; photoprotection; topical azelaic acid/hydroquinone or adapalene; Q-switched/Er:YAG laser (case reports); genetic counselling"]),
 ],
 spot=["Angulated reticulate pigmented macules on dorsa of hands with palmar pits — RAPK (ADAM10)"]),
]
