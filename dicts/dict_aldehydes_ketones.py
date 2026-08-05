# ==========================================
# ALDEHYDE & KETONE ENGINE (ADDITION & CONDENSATION)
# ==========================================

# --- THE ALPHA-HYDROGEN TRAPS ---
# Matches an sp3 hybridized carbon bonded to a carbonyl that contains at least 1 hydrogen.
# Crucial for deciding between Aldol and Cannizzaro.
HAS_ALPHA_H = ["[CX4H1,CX4H2,CX4H3]-[CX3]=O"]

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
ALDEHYDE_KETONE_RULES = {

    # --- NUCLEOPHILIC ADDITION ---
    "HCN / KCN (Cyanohydrin Formation)": {
        "rules": [
            # Carbonyl oxygen becomes a hydroxyl, cyanide attaches to the carbonyl carbon
            "[CX3:1]=O >> [C:1](-[OH])-[C]#N"
        ]
    },
    
    # --- ACETAL / KETAL PROTECTION ---
    "Ethylene Glycol / H+ (Dean-Stark Trap)": {
        "rules": [
            # The '1' notation in SMARTS signifies a ring closure. 
            # This wraps the carbonyl into a 5-membered 1,3-dioxolane ring!
            "[CX3:1]=O >> [C:1]1-[O]-[CH2]-[CH2]-[O]-1"
        ]
    },
    "H3O+ / Heat (Deprotection)": {
        "rules": [
            # Cleaves the 1,3-dioxolane ring back into a carbonyl
            "[C:1]1-[O]-[CH2]-[CH2]-[O]-1 >> [C:1]=O"
        ]
    },

    # --- CONDENSATION REACTIONS ---
    "Dilute NaOH / Heat (Aldol Condensation)": {
        "rules": [
            # Simplified Bimolecular Dehydration (Cross/Self Aldol)
            # RDKit connects the alpha-carbon of one molecule to the carbonyl of the other,
            # eliminating water to form the alpha,beta-unsaturated system.
            "[CX4H2,CX4H3:1]-[CX3:2]=O.[CX3:3]=O >> [C:3]=[C:1]-[C:2]=O"
        ],
        "poisons": [
            # We want to warn the user if they try to run this on something lacking alpha-H's
            "[CX3H1](=O)-[C](-[#6])(-[#6])-[#6]", # Tertiary alpha-carbon
            "[c]-[CX3H1]=O"                      # Benzaldehyde derivative
        ],
        "poison_message": "Aldol condensation requires at least one alpha-hydrogen. Molecules like benzaldehyde or formaldehyde will not undergo this reaction under standard conditions!"
    },
    
    "Conc. KOH / Heat (Cannizzaro Reaction)": {
        "rules": [
            # Bimolecular Disproportionation (Oxidation & Reduction simultaneously)
            # Two aldehydes react: one becomes an alcohol, the other a carboxylate salt.
            "[CX3H1:1]=O.[CX3H1:2]=O >> [C:1]-[OH].[O-]-[C:2]=O"
        ],
        "poisons": HAS_ALPHA_H,
        "poison_message": "Molecules with alpha-hydrogens will undergo Aldol condensation in the presence of strong base. The Cannizzaro reaction is strictly for aldehydes lacking alpha-hydrogens!"
    },

    # --- THE HALOFORM CLEAVAGE ---
    "I2 / NaOH or NaOI (Iodoform Test)": {
        "rules": [
            # Cleaves a Methyl Ketone into a Carboxylate Salt and Iodoform (CHI3)
            # The dot (.) splits the products. C:1 is the methyl group turning into Iodoform.
            "[CH3:1]-[C:2](=O)-[#6,#1:3] >> [O-]-[C:2](=O)-[#6,#1:3].[C:1](I)(I)I"
        ],
        "poisons": ["[CH2]-[CX3]=O", "[CH1]-[CX3]=O", "[CH0]-[CX3]=O"], # Standard ketones lacking a terminal methyl
        "poison_message": "The Haloform reaction strictly requires a Methyl Ketone (or a methyl carbinol that can be oxidized into one). Other ketones will not cleave!"
    },

    # --- AMMONIA DERIVATIVES (IMINE CHEMISTRY) ---
    "NH2-OH / H+ (Hydroxylamine)": {
        "rules": [
            # Forms an Oxime (Water is eliminated)
            "[CX3:1]=O >> [C:1]=[N]-[OH]"
        ]
    },
    "NH2-NH-Ph / H+ (Phenylhydrazine)": {
        "rules": [
            # Forms a Phenylhydrazone
            "[CX3:1]=O >> [C:1]=[N]-[NH]-[c]1[cH][cH][cH][cH][cH]1"
        ]
    }
}