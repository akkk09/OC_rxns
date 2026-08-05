# ==========================================
# ALKYL HALIDE ENGINE (SN1/SN2 vs E1/E2)
# ==========================================

# Standard Leaving Groups (excluding Fluorine, which is a poor LG)
LG = "[Cl,Br,I]"

# Inert Halides: Aryl and Vinyl halides do not undergo SN1/SN2 reactions
INERT_HALIDES = [
    f"[c]-{LG}",        # Aryl Halide
    f"[C]=[C]-{LG}"     # Vinyl Halide
]

# Tertiary Halide Poison for SN2: 3-degree carbons attached to LG
TERTIARY_HALIDE = [f"[CX4](-[*])(-[*])(-[*])-{LG}"]

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
ALKYL_HALIDE_RULES = {

    # --- HYDROLYSIS (SUBSTITUTION) ---
    "Aqueous KOH / NaOH": {
        "rules": [
            # General substitution (SN2 for 1/2 degree, SN1 for 3 degree)
            f"[CX4:1]-{LG} >> [C:1]-[OH]"
        ],
        "poisons": INERT_HALIDES,
        "poison_message": "Aryl and vinyl halides are inert to nucleophilic substitution due to partial double-bond character and sp2 hybridization."
    },
    
    # --- DEHYDROHALOGENATION (ELIMINATION) ---
    "Alcoholic KOH / Heat": {
        "rules": [
            # E2 Beta-Elimination (RDKit maps all adjacent beta-hydrogens to output alkene mixtures)
            f"[CH3,CH2,CH1:1]-[CX4:2]-{LG} >> [C:1]=[C:2]"
        ],
        # Aryl/Vinyl cannot do beta-elimination easily
        "poisons": INERT_HALIDES,
        "poison_message": "Standard E2 elimination fails on sp2 hybridized vinyl/aryl halides."
    },

    # --- AMBIDENT NUCLEOPHILES (THE JEE TRAP) ---
    # KCN is ionic -> attacks via Carbon -> Nitriles
    "KCN (Potassium Cyanide)": {
        "rules": [
            f"[CX4:1]-{LG} >> [C:1]-C#N"
        ],
        "poisons": INERT_HALIDES + TERTIARY_HALIDE,
        "poison_message": "If tertiary, steric hindrance prevents SN2, leading to E2 elimination. If aryl/vinyl, the bond is inert."
    },
    
    # AgCN is covalent -> Nitrogen lone pair attacks -> Isonitriles
    "AgCN (Silver Cyanide)": {
        "rules": [
            f"[CX4:1]-{LG} >> [C:1]-[N+]#[C-]"
        ],
        "poisons": INERT_HALIDES + TERTIARY_HALIDE,
        "poison_message": "If tertiary, steric hindrance prevents SN2. If aryl/vinyl, the bond is inert."
    },

    # KNO2 is ionic -> attacks via Oxygen -> Alkyl Nitrites
    "KNO2 (Potassium Nitrite)": {
        "rules": [
            f"[CX4:1]-{LG} >> [C:1]-O-N=O"
        ],
        "poisons": INERT_HALIDES,
        "poison_message": "Aryl and vinyl halides are inert to nucleophilic substitution."
    },
    
    # AgNO2 is covalent -> attacks via Nitrogen -> Nitroalkanes
    "AgNO2 (Silver Nitrite)": {
        "rules": [
            f"[CX4:1]-{LG} >> [C:1]-[N+](=O)[O-]"
        ],
        "poisons": INERT_HALIDES,
        "poison_message": "Aryl and vinyl halides are inert to nucleophilic substitution."
    },

    # --- WILLIAMSON ETHER SYNTHESIS ---
    "RONa (Sodium Alkoxide)": {
        "rules": [
            # Assuming a general methoxide/ethoxide attack for simulator simplicity
            f"[CX4:1]-{LG} >> [C:1]-[O]-[CH3]" 
        ],
        "poisons": INERT_HALIDES + TERTIARY_HALIDE,
        "poison_message": "Williamson Ether Synthesis fails with tertiary alkyl halides. The strongly basic alkoxide ion will trigger an E2 elimination to form an alkene instead!"
    },
    
    # --- FINKELSTEIN & SWARTS (HALOGEN EXCHANGE) ---
    "NaI / Dry Acetone (Finkelstein)": {
        "rules": [
            "[CX4:1]-[Cl,Br] >> [C:1]-[I]"
        ],
        "poisons": INERT_HALIDES,
        "poison_message": "Aryl/Vinyl halides do not undergo SN2 halogen exchange."
    },
    "AgF / Hg2F2 (Swarts Reaction)": {
        "rules": [
            "[CX4:1]-[Cl,Br,I] >> [C:1]-[F]"
        ],
        "poisons": INERT_HALIDES,
        "poison_message": "Aryl/Vinyl halides do not undergo SN2 halogen exchange."
    }
}