# ==========================================
# AMINES & NITROGEN COMPOUNDS ENGINE
# ==========================================

# --- NITROGEN TRAPS & POISONS ---
SECONDARY_TERTIARY_AMINES = ["[NX3H1]", "[NX3H0]"]
ARYL_HALIDES = ["[c]-[F,Cl,Br,I]"]

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
NITROGEN_RULES = {

    # --- 1. THE ISOCYANIDE TEST ---
    "CHCl3 / KOH, Heat (Carbylamine Reaction)": {
        "rules": [
            # Converts ONLY Primary Amines (Aliphatic and Aromatic) to Isocyanides
            # Note the formal charges: Nitrogen is +, Carbon is -
            "[#6,c:1]-[NX3H2:2] >> [#6,c:1]-[N+:2]#[C-]"
        ],
        "poisons": SECONDARY_TERTIARY_AMINES,
        "poison_message": "The Carbylamine test strictly requires a primary amine! Secondary and tertiary amines cannot provide the two protons necessary to form the triple bond of the foul-smelling isocyanide."
    },

    # --- 2. DIAZOTIZATION (THE GREAT BIFURCATION) ---
    "NaNO2 / HCl, 0-5°C (Diazotization)": {
        "rules": [
            # 1. Aromatic Primary Amines -> Stable Diazonium Salt
            # Resonance stabilizes the N2+ leaving group at low temperatures.
            "[c:1]-[NX3H2:2] >> [c:1]-[N+:2]#[N]",
            
            # 2. Aliphatic Primary Amines -> Alcohols
            # The aliphatic diazonium ion is highly unstable, instantly losing N2 gas
            # to form a carbocation, which is trapped by water.
            "[CX4:1]-[NX3H2:2] >> [C:1]-[OH]"
        ],
        "poisons": SECONDARY_TERTIARY_AMINES,
        "poison_message": "Secondary amines form a yellow oily N-nitrosamine. Tertiary amines simply undergo acid-base protonation or ring nitrosation. Only primary amines form the diazonium species!"
    },

    # --- 3. GABRIEL PHTHALIMIDE SYNTHESIS ---
    # (Macro: Phthalimide + KOH + R-X -> -> Primary Amine)
    "Gabriel Phthalimide Sequence (Macro)": {
        "rules": [
            # Strictly converts primary/secondary Alkyl Halides to Primary Amines
            "[CX4:1]-[Cl,Br,I] >> [C:1]-[NH2]"
        ],
        "poisons": ARYL_HALIDES + ["[CX4H0]-[Cl,Br,I]"], # Aryl halides and Tertiary halides
        "poison_message": "Gabriel Phthalimide Synthesis relies on an SN2 attack by the bulky phthalimide anion. Aryl halides cannot undergo SN2 due to sp2 partial double bond character, meaning you CANNOT synthesize Aniline this way! Tertiary halides will strictly undergo E2 elimination."
    },

    # --- 4. EXHAUSTIVE METHYLATION & ELIMINATION ---
    "CH3I (Excess) / Ag2O, Heat (Hofmann Elimination)": {
        "rules": [
            # E2 Beta-Elimination yielding the LEAST substituted alkene (Anti-Saytzeff / Hofmann Rule)
            # The bulky quaternary ammonium leaving group dictates the stereochemistry.
            "[CH3,CH2,CH1:1]-[CX4:2]-[NX3,NX4+] >> [C:1]=[C:2]"
        ]
    },

    # --- 5. REDUCTION OF NITRO COMPOUNDS ---
    "Sn / HCl or Fe / HCl (Acidic Reduction)": {
        "rules": [
            # The industrial and laboratory standard for converting Nitro to Amine
            "[#6,c:1]-[N+](=O)[O-] >> [#6,c:1]-[NH2]"
        ]
    },
    
    # --- 6. SANDMEYER / GATTERMANN REACTIONS ---
    "CuCl / HCl (Sandmeyer Reaction)": {
        "rules": [
            # Replaces the aromatic diazonium group with a Chloride via radical mechanism
            "[c:1]-[N+]#[N] >> [c:1]-[Cl]"
        ],
        "poisons": ["[CX4]-[N+]#[N]"],
        "poison_message": "Aliphatic diazonium salts decompose instantly. The Sandmeyer reaction requires the transient stability of an AROMATIC diazonium salt."
    }
}