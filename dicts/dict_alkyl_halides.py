# ==========================================
# ALKYL HALIDE ENGINE (EXHAUSTIVE OLYMPIAD & GRADUATE LEVEL)
# ==========================================

# Standard Leaving Groups (excluding Fluorine due to high C-F bond dissociation energy)
LG = "[Cl,Br,I]"

# Chemically Inert Matrices (Resonance and hybridization stabilization blocks)
INERT_HALIDES = [
    f"[c]-{LG}",      # Aryl Halide (strong resonance stabilization and sp2 carbon character)
    f"[C]=[C]-{LG}"   # Vinyl Halide (partial double bond character via lone-pair overlap)
]

# Sterically Hindered or Bridgehead Systems (Bredt's Rule & Neopentyl Steric Walls)
BREDT_HALIDES = ["[CX4H0]1-[#6]-[#6]-[CX4H0]2-[#6]-[#6]-1-[#6]-2-[Cl,Br,I]"]
NEOPENTYL_SYSTEMS = ["[CX4](C)(C)(C)-CH2-[Cl,Br,I]"]

# Tertiary Halides (sterically blocked from concerted SN2; undergoes ionization SN1/E1 or base-promoted E2)
TERTIARY_HALIDE = [f"[CX4](-[*])(-[*])(-[*])-{LG}"]

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
ALKYL_HALIDE_RULES = {

    # ==========================================
    # 1. SOLVOLYSIS & IONIZATION PATHWAYS
    # ==========================================

    "Aqueous NaOH / Thermal Solvolysis (SN1 Substitution & E1 Elimination Competition)": {
        "rules": [
            # Tertiary and secondary substrates proceed via slow rate-determining carbocation ionization (SN1 alcohols + E1 alkenes)
            f"[CX4H0,CX4H1:1]-{LG} >> [C:1]-[OH]"
        ],
        "poisons": INERT_HALIDES + BREDT_HALIDES,
        "poison_message": "Hydrolysis failure: Aryl and vinyl halides are completely unreactive toward nucleophilic substitution due to electron-rich pi systems. Bridgehead halides cannot flatten to sp2 transition states required for stable carbocation generation (Bredt's rule)."
    },

    "AgNO3 / Aqueous Ethanol, Room Temp (Silver-Assisted SN1 Solvolysis via Halide Abstraction)": {
        "rules": [
            # Silver ion (Ag+) coordinates with the halide leaving group, precipitating insoluble AgX 
            # and forcing rapid carbocation formation even on secondary or reactive alkyl systems.
            f"[CX4:1]-{LG} >> [C:1]-[OH]"
        ],
        "poisons": INERT_HALIDES + BREDT_HALIDES,
        "poison_message": "Silver-assisted solvolysis failure: Inactive on un-ionizable aryl, vinyl, or bridgehead halide matrices."
    },

    # ==========================================
    # 2. CONCERTED ELIMINATION PATHWAYS (E2 STEREOELECTRONICS)
    # ==========================================

    "Alcoholic KOH / Elevated Temperature (Concerted E2 Bimolecular Elimination)": {
        "rules": [
            # Stereoelectronically controlled anti-periplanar elimination yielding Zaitsev-preferred stable internal alkenes
            f"[CH3,CH2,CH1:1]-[CX4:2]-{LG} >> [C:1]=[C:2]"
        ],
        "poisons": INERT_HALIDES + BREDT_HALIDES,
        "poison_message": "E2 Elimination failure: Requires strict anti-periplanar geometric alignment of a beta-hydrogen and the leaving group. Unreactive on aryl/vinyl matrices and bridgehead systems."
    },

    "Potassium tert-Butoxide / t-BuOH (Bulky Base-Promoted Hofmann Elimination)": {
        "rules": [
            # Sterically hindered strong base abstracting the most accessible, least hindered proton,
            # yielding the kinetic Hofmann-preferred alkene product.
            f"[CH3,CH2:1]-[CX4:2]-[CX4:3]-{LG} >> [C:1]=[C:2]-[C:3]"
        ],
        "poisons": INERT_HALIDES + BREDT_HALIDES,
        "poison_message": "Hofmann elimination failure: Incompatible with rigid or non-enolizable halogen frameworks lacking accessible beta-hydrogens."
    },

    # ==========================================
    # 3. AMBIDENT NUCLEOPHILES & HSAB THEORY
    # ==========================================

    "KCN / Aqueous Ethanol (Ionic Carbon Attack -> Nitriles via SN2)": {
        "rules": [
            # Ionic cyanide acting as an ambident nucleophile reacting via its softer carbon center 
            # to displace primary and secondary halides via concerted SN2 kinetics.
            f"[CX4H2,CX4H1:1]-{LG} >> [C:1]-C#N"
        ],
        "poisons": INERT_HALIDES + TERTIARY_HALIDE + BREDT_HALIDES + NEOPENTYL_SYSTEMS,
        "poison_message": "Nucleophilic substitution failure: Tertiary, neopentyl, and bridgehead systems experience prohibitive steric hindrance or ionization failure, defaulting to E2 elimination pathways under ionic conditions."
    },
    
    "AgCN / Ether (Covalent Nitrogen Attack -> Isonitriles / Carbylamines)": {
        "rules": [
            # Silver ion (Ag+) assistance pulls the leaving group via precipitation (AgX), 
            # shifting mechanism toward carbocationic character where the harder nitrogen lone pair attacks.
            f"[CX4:1]-{LG} >> [C:1]-[N+]#[C-]"
        ],
        "poisons": INERT_HALIDES + BREDT_HALIDES,
        "poison_message": "AgCN reaction failure: Inert on aryl/vinyl or bridgehead matrices where ionization is structurally forbidden."
    },

    "KNO2 / DMF (Ionic Oxygen Attack -> Alkyl Nitrites via SN2)": {
        "rules": [
            # Ambident nitrite ion reacting via the more electronegative oxygen center under standard SN2 conditions
            f"[CX4H2,CX4H1:1]-{LG} >> [C:1]-O-N=O"
        ],
        "poisons": INERT_HALIDES + TERTIARY_HALIDE,
        "poison_message": "Substitution failure: Sterically hindered tertiary alkyl halides fail to undergo SN2 displacement with nitrite salts."
    },
    
    "AgNO2 / Ether (Silver-Assisted Nitrogen Attack -> Nitroalkanes)": {
        "rules": [
            # Silver-assisted ionization yielding covalent nitroalkanes via nitrogen-bound addition pathways
            f"[CX4:1]-{LG} >> [C:1]-[N+](=O)[O-]"
        ],
        "poisons": INERT_HALIDES,
        "poison_message": "Silver-assisted substitution requires an accessible sp3 carbon center capable of coordination."
    },

    # ==========================================
    # 4. WILLIAMSON ETHER SYNTHESIS & ETHER CLEAVAGE
    # ==========================================

    "Sodium Alkoxide / Alcohol (SN2 Williamson Ether Synthesis vs. E2 Competition)": {
        "rules": [
            # Nucleophilic displacement of primary halides by alkoxide ions to generate unsymmetrical ethers
            f"[CX4H2:1]-{LG} >> [C:1]-[O]-[CH3]"
        ],
        "poisons": INERT_HALIDES + TERTIARY_HALIDE + BREDT_HALIDES,
        "poison_message": "Williamson Ether Synthesis failure: Strong alkoxide bases act predominantly as Brønsted bases with tertiary or hindered substrates, driving quantitative E2 elimination to alkenes instead of substitution."
    },

    # ==========================================
    # 5. HALOGEN EXCHANGE & KINETIC EQUILIBRIA
    # ==========================================

    "NaI / Anhydrous Acetone (Finkelstein Equilibrium via Halide Precipitation)": {
        "rules": [
            # Bimolecular halogen exchange driven forward by the physical precipitation 
            # of insoluble sodium chloride or sodium bromide in dry acetone solvent matrices.
            "[CX4H2,CX4H1:1]-[Cl,Br] >> [C:1]-[I]"
        ],
        "poisons": INERT_HALIDES + TERTIARY_HALIDE,
        "poison_message": "Finkelstein reaction failure: Incompatible with aryl, vinyl, or unreactive tertiary halide structures lacking clean SN2 transition state access."
    },
    
    "AgF or Hg2F2 / Solvent (Swarts Fluorination via Heavy Metal Abstraction)": {
        "rules": [
            # Heavy metal salt-assisted halogen exchange to synthesize unreactive alkyl fluorides
            f"[CX4:1]-{LG} >> [C:1]-[F]"
        ],
        "poisons": INERT_HALIDES,
        "poison_message": "Swarts reaction requires an activated sp3 carbon center capable of heavy metal-assisted halide abstraction."
    }
}