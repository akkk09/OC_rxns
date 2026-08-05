# ==========================================
# HETEROCYCLES ENGINE (EAS, NAS, & ACID TRAPS)
# ==========================================

# --- HETEROCYCLE RECOGNITION (POISONS & SELECTORS) ---
# Pyrrole ([nH]) and Furan ([o]) are extremely sensitive to strong mineral acids.
ACID_SENSITIVE = ["[nH]1[c,cH][c,cH][c,cH][c,cH]1", "[o]1[c,cH][c,cH][c,cH][c,cH]1"]

# Pyridine ([n]) lone pair complexes with Lewis acids, halting Friedel-Crafts.
PYRIDINE_RING = ["[n]1[c,cH][c,cH][c,cH][c,cH][c,cH]1"]

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
HETEROCYCLE_RULES = {

    # --- 1. MILD EAS (FOR 5-MEMBERED RINGS) ---
    "HNO3 / Ac2O, 0°C (Mild Nitration)": {
        "rules": [
            # Alpha (C2) Nitration for Pyrrole, Furan, and Thiophene
            "[nH,o,s:1]1[cH1:2][cH1:3][cH1:4][cH1:5]1 >> [nH,o,s:1]1[c:2](-[N+](=O)[O-])[cH1:3][cH1:4][cH1:5]1"
        ],
        "poisons": PYRIDINE_RING,
        "poison_message": "Pyridine is highly deactivated (pi-deficient). It will not undergo nitration under mild conditions; it requires drastically harsh conditions (KNO3 / fuming H2SO4 at 300°C)."
    },
    
    "SO3 / Pyridine, Heat (Mild Sulfonation)": {
        "rules": [
            # Alpha (C2) Sulfonation 
            "[nH,o,s:1]1[cH1:2][cH1:3][cH1:4][cH1:5]1 >> [nH,o,s:1]1[c:2](-[S](=O)(=O)[OH])[cH1:3][cH1:4][cH1:5]1"
        ]
    },

    "POCl3 / DMF (Vilsmeier-Haack Formylation)": {
        "rules": [
            # Specifically formylates highly activated pi-excessive rings at the C2 position
            "[nH,o,s:1]1[cH1:2][cH1:3][cH1:4][cH1:5]1 >> [nH,o,s:1]1[c:2](-[C](=O)[H])[cH1:3][cH1:4][cH1:5]1"
        ],
        "poisons": PYRIDINE_RING,
        "poison_message": "The Vilsmeier-Haack reagent is not a strong enough electrophile to attack a deactivated pyridine ring."
    },

    # --- 2. HARSH EAS (THE ACID TRAPS) ---
    "Conc. HNO3 / Conc. H2SO4 (Standard Nitration)": {
        "rules": [
            # Pyridine undergoes Meta (C3) Nitration only under extreme heat/acid
            "[n:1]1[cH1:2][cH1:3][cH1:4][cH1:5][cH1:6]1 >> [n:1]1[cH1:2][c:3](-[N+](=O)[O-])[cH1:4][cH1:5][cH1:6]1"
        ],
        "poisons": ACID_SENSITIVE,
        "poison_message": "Pyrrole and Furan are highly acid-sensitive! The use of strong mineral acids like H2SO4 will protonate the ring, destroy aromaticity, and cause the molecule to violently polymerize into a black tar."
    },

    "CH3Cl / AlCl3 (Friedel-Crafts Alkylation)": {
        "rules": [
            # Thiophene is the only 5-membered ring stable enough to sometimes survive this, 
            # but usually, we just map it for general activated systems.
            "[s:1]1[cH1:2][cH1:3][cH1:4][cH1:5]1 >> [s:1]1[c:2](-[CH3])[cH1:3][cH1:4][cH1:5]1"
        ],
        "poisons": ACID_SENSITIVE + PYRIDINE_RING,
        "poison_message": "Friedel-Crafts fails! Pyrrole and Furan will polymerize in the presence of Lewis acids. Pyridine's basic nitrogen lone pair will complex with the AlCl3 catalyst, completely deactivating the ring."
    },

    # --- 3. NUCLEOPHILIC AROMATIC SUBSTITUTION (NAS) ---
    "NaNH2 / Liquid NH3, Heat (Chichibabin Reaction)": {
        "rules": [
            # Pyridine undergoes NAS at the Alpha (C2) position due to the electronegativity of Nitrogen
            # stabilizing the anionic Meisenheimer intermediate.
            "[n:1]1[cH1:2][cH1:3][cH1:4][cH1:5][cH1:6]1 >> [n:1]1[c:2](-[NH2])[cH1:3][cH1:4][cH1:5][cH1:6]1"
        ],
        "poisons": ["[nH]1[c,cH][c,cH][c,cH][c,cH]1"],
        "poison_message": "Pyrrole is strongly acidic at the N-H bond! NaNH2 acts as a powerful base here, ripping off the N-H proton to form a Pyrrole anion rather than attacking the carbon ring."
    }
}