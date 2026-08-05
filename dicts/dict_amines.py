# ==========================================
# AMINES & DIAZONIUM ENGINE (TESTS & COUPLING)
# ==========================================

# --- SECONDARY & TERTIARY AMINE POISONS ---
# Used to block 1-degree specific tests (like Carbylamine)
SECONDARY_AMINE = ["[NX3H1](-[#6])-[#6]", "[nx3H1]"] # Aliphatic and aromatic 2-degree
TERTIARY_AMINE = ["[NX3H0](-[#6])(-[#6])-[#6]", "[nx3H0]"]

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
AMINE_RULES = {

    # --- QUALITATIVE TESTS (DEGREE IDENTIFICATION) ---
    "CHCl3 / KOH, Heat (Carbylamine Test)": {
        "rules": [
            # 1-degree Aliphatic OR Aromatic Amine -> Isocyanide (Foul smell)
            # The nitrogen formally becomes positive, carbon becomes negative.
            "[CX4,c:1]-[NX3H2:2] >> [C:1]-[N+:2]#[C-]"
        ],
        "poisons": SECONDARY_AMINE + TERTIARY_AMINE,
        "poison_message": "The Carbylamine (Isocyanide) test is strictly positive for 1° amines. Secondary and tertiary amines do not have the required two protons to eliminate, and thus do not react."
    },
    
    # --- NITROUS ACID (THE BIFURCATION POINT) ---
    "NaNO2 / HCl, 0-5°C (Nitrous Acid)": {
        "rules": [
            # 1. Aromatic 1-degree -> Diazonium Salt (Stable at cold temps due to resonance)
            "[c:1]-[NX3H2] >> [c:1]-[N+]#[N]",
            
            # 2. Aliphatic 1-degree -> Alcohol (Diazonium is highly unstable, immediately hydrolyzes)
            "[CX4:1]-[NX3H2] >> [C:1]-[OH]",
            
            # 3. Secondary Amines -> N-Nitrosamine (Yellow oily liquid)
            "[#6:1]-[NX3H1:2]-[#6:3] >> [#6:1]-[N:2](-[#6:3])-[N]=O"
        ],
        "poisons": TERTIARY_AMINE,
        "poison_message": "Tertiary aliphatic amines dissolve to form soluble nitrite salts but do not yield a distinct neutral organic product. Tertiary aromatic amines undergo electrophilic aromatic substitution at the para position."
    },

    # --- DIAZONIUM HUB (AROMATIC TRANSFORMATIONS) ---
    # These reactions strictly require a pre-formed diazonium group on an aromatic ring.
    "CuCl / HCl (Sandmeyer Reaction)": {
        "rules": [
            "[c:1]-[N+]#[N] >> [c:1]-[Cl]"
        ],
        "poisons": ["[CX4]-[N+]#[N]"],
        "poison_message": "Aliphatic diazonium salts are too unstable to be isolated for a Sandmeyer reaction; they instantly degrade into carbocations."
    },
    "CuCN / KCN (Sandmeyer Cyanation)": {
        "rules": [
            "[c:1]-[N+]#[N] >> [c:1]-C#N"
        ]
    },
    "KI / Warm (Iodination)": {
        "rules": [
            # Cu is not required for Iodine
            "[c:1]-[N+]#[N] >> [c:1]-[I]"
        ]
    },
    "HBF4, Heat (Balz-Schiemann Reaction)": {
        "rules": [
            # Fluorination via thermal decomposition of the tetrafluoroborate salt
            "[c:1]-[N+]#[N] >> [c:1]-[F]"
        ]
    },
    "Warm H2O (Hydrolysis)": {
        "rules": [
            # Direct conversion to Phenol
            "[c:1]-[N+]#[N] >> [c:1]-[OH]"
        ]
    },
    
    # --- DIAZONIUM DEAMINATION (THE "ERASER") ---
    "H3PO2 / H2O or EtOH (Deamination)": {
        "rules": [
            # Completely removes the Diazonium group, replacing it with Hydrogen.
            # RDKit's valency engine will automatically restore the aromatic C-H bond.
            "[c:1]-[N+]#[N] >> [c:1]"
        ]
    }
}