# ==========================================
# HETEROCYCLES ENGINE (EXHAUSTIVE OLYMPIAD & GRADUATE LEVEL)
# ==========================================

# --- HETEROCYCLE RECOGNITION (POISONS & SELECTORS) ---
# Pyrrole ([nH]) and Furan ([o]) are extremely sensitive to strong mineral acids, causing rapid polymerization.
ACID_SENSITIVE = ["[nH]1[c,cH][c,cH][c,cH][c,cH]1", "[o]1[c,cH][c,cH][c,cH][c,cH]1"]

# Pyridine ([n]) lone pair complexes with strong Lewis acids, shutting down Friedel-Crafts alkylation/acylation.
PYRIDINE_RING = ["[n]1[c,cH][c,cH][c,cH][c,cH][c,cH]1"]

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
HETEROCYCLE_RULES = {

    # ==========================================
    # 1. MILD ELECTROPHILIC AROMATIC SUBSTITUTION (5-MEMBERED PI-EXCESSIVE RINGS)
    # ==========================================

    "HNO3 / Ac2O, 0°C (Mild Regioselective C2 Nitration)": {
        "rules": [
            # Alpha (C2) Nitration for Pyrrole, Furan, and Thiophene via activated electrophilic pathways
            "[nH,o,s:1]1[cH1:2][cH1:3][cH1:4][cH1:5]1 >> [nH,o,s:1]1[c:2](-[N+](=O)[O-])[cH1:3][cH1:4][cH1:5]1"
        ],
        "poisons": PYRIDINE_RING,
        "poison_message": "Pyridine is highly deactivated and pi-deficient. It will not undergo nitration under mild conditions; it requires drastically harsh conditions (KNO3 / fuming H2SO4 at high temperatures)."
    },
    
    "SO3 / Pyridine, Heat (Mild Regioselective C2 Sulfonation)": {
        "rules": [
            # Alpha (C2) Sulfonation of pi-excessive five-membered heterocycles
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

    # ==========================================
    # 2. HARSH EAS & THE ACID DESTRUCTION TRAPS
    # ==========================================

    "Conc. HNO3 / Conc. H2SO4, Heat (Pyridine C3 Nitration)": {
        "rules": [
            # Pyridine undergoes Meta (C3) Nitration only under extreme thermal and acidic conditions
            "[n:1]1[cH1:2][cH1:3][cH1:4][cH1:5][cH1:6]1 >> [n:1]1[cH1:2][c:3](-[N+](=O)[O-])[cH1:4][cH1:5][cH1:6]1"
        ],
        "poisons": ACID_SENSITIVE,
        "poison_message": "Pyrrole and Furan are highly acid-sensitive! The use of strong mineral acids like H2SO4 will protonate the ring, destroy aromaticity, and cause the molecule to violently polymerize into an insoluble black tar."
    },

    "CH3Cl / Anhydrous AlCl3 (Friedel-Crafts Alkylation Attempt)": {
        "rules": [
            # Thiophene is the only 5-membered ring robust enough to survive under modified conditions
            "[s:1]1[cH1:2][cH1:3][cH1:4][cH1:5]1 >> [s:1]1[c:2](-[CH3])[cH1:3][cH1:4][cH1:5]1"
        ],
        "poisons": ACID_SENSITIVE + PYRIDINE_RING,
        "poison_message": "Friedel-Crafts failure! Pyrrole and Furan polymerize instantly in the presence of Lewis acids. Pyridine's basic nitrogen lone pair complexes with the AlCl3 catalyst, permanently deactivating the ring."
    },

    # ==========================================
    # 3. NUCLEOPHILIC AROMATIC SUBSTITUTION (NAS) & BASE PATHWAYS
    # ==========================================

    "NaNH2 / Liquid NH3, Heat (Chichibabin Amination of Pyridine)": {
        "rules": [
            # Pyridine undergoes NAS at the Alpha (C2) position due to nitrogen electronegativity 
            # stabilizing the anionic Meisenheimer intermediate.
            "[n:1]1[cH1:2][cH1:3][cH1:4][cH1:5][cH1:6]1 >> [n:1]1[c:2](-[NH2])[cH1:3][cH1:4][cH1:5][cH1:6]1"
        ],
        "poisons": ["[nH]1[c,cH][c,cH][c,cH][c,cH]1"],
        "poison_message": "Pyrrole is strongly acidic at the N-H bond! NaNH2 acts as a powerful Brønsted base here, ripping off the N-H proton to form a pyrrolyl anion rather than attacking the carbon ring."
    }
}