# ==========================================
# ALCOHOLS, PHENOLS, & ETHERS ENGINE
# ==========================================

# --- ALCOHOL POISONS ---
PRIMARY_ALCOHOLS = ["[CX4H2,CX4H3]-[OH]"]
PHENOLS_ONLY = ["[CX4]-[OH]"] # Prevents aliphatic alcohols from doing phenol-specific reactions

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
ALCOHOL_PHENOL_RULES = {

    # --- QUALITATIVE ALCOHOL TESTS ---
    "ZnCl2 / conc. HCl (Lucas Reagent)": {
        "rules": [
            # Tertiary Alcohols -> Immediate turbidity (Fast SN1)
            "[CX4H0:1]-[OH] >> [C:1]-[Cl]",
            
            # Secondary Alcohols -> Turbidity after 5 minutes (Slow SN1)
            "[CX4H1:1]-[OH] >> [C:1]-[Cl]"
        ],
        "poisons": PRIMARY_ALCOHOLS + ["[c]-[OH]"],
        "poison_message": "The Lucas test relies on an SN1 mechanism. Primary alcohols and phenols cannot form stable carbocations and will not produce turbidity (alkyl chlorides) at room temperature!"
    },

    # --- DEHYDRATION (ELIMINATION) ---
    "Conc. H2SO4 / 170°C (Dehydration)": {
        "rules": [
            # E1 Beta-Elimination (Produces a mixture of alkenes based on adjacent hydrogens)
            # RDKit will natively map all adjacent beta-hydrogens to show Saytzeff / Hofmann products.
            "[CH3,CH2,CH1:1]-[CX4:2]-[OH] >> [C:1]=[C:2]"
        ],
        "poisons": ["[c]-[OH]"],
        "poison_message": "Phenols do not undergo dehydration. The C-O bond is too strong due to resonance, and the aromatic ring prevents elimination."
    },

    # --- PHENOL-SPECIFIC REACTIONS (NAME REACTIONS) ---
    "CHCl3 / aq. NaOH (Reimer-Tiemann Reaction)": {
        "rules": [
            # Forms Salicylaldehyde (Ortho-formylation)
            # Targets the ortho position explicitly
            "[c:1](-[OH])[cH1:2] >> [c:1](-[OH])[c:2]-[C](=O)[H]"
        ],
        "poisons": PHENOLS_ONLY,
        "poison_message": "The Reimer-Tiemann reaction strictly requires a phenol to generate the highly reactive phenoxide ion, which then attacks the electrophilic dichlorocarbene intermediate."
    },
    "CO2 / NaOH, 125°C, High Pressure (Kolbe-Schmitt Reaction)": {
        "rules": [
            # Forms Salicylic Acid (Ortho-carboxylation)
            "[c:1](-[OH])[cH1:2] >> [c:1](-[OH])[c:2]-[C](=O)[OH]"
        ],
        "poisons": PHENOLS_ONLY,
        "poison_message": "The Kolbe-Schmitt reaction requires a phenoxide ion to undergo electrophilic aromatic substitution with CO2."
    },

    # --- ETHER CLEAVAGE (THE JEE TRAP) ---
    "Cold HI (1 Equivalent)": {
        "rules": [
            # 1. Alkyl-Aryl Ethers (Anisole derivatives)
            # The sp2 Aryl-O bond NEVER breaks. Oxygen strictly stays with the ring.
            "[c:1]-[O:2]-[CX4:3] >> [c:1]-[OH:2].[C:3]-[I]",
            
            # 2. Dialkyl Ethers (Assuming SN2 for primary/secondary, Iodine attacks less substituted)
            # RDKit splits the ether into an alcohol and an alkyl iodide.
            "[CX4:1]-[O:2]-[CX4:3] >> [C:1]-[OH:2].[C:3]-[I]"
        ]
    },
    "Excess HI / Heat": {
        "rules": [
            # 1. Alkyl-Aryl Ethers
            # Even with excess heat and acid, the Aryl-O bond is untouchable!
            "[c:1]-[O:2]-[CX4:3] >> [c:1]-[OH:2].[C:3]-[I]",
            
            # 2. Dialkyl Ethers
            # Both sides are cleaved to form two equivalents of alkyl iodides.
            "[CX4:1]-[O]-[CX4:2] >> [C:1]-[I].[C:2]-[I]"
        ]
    }
}