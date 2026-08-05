# ==========================================
# PROTECTING GROUPS ENGINE (MASKING & DEPROTECTION)
# ==========================================

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
PROTECTING_GROUP_RULES = {

    # --- 1. AMINE PROTECTION (THE ANILINE SAVIOR) ---
    "(CH3CO)2O / Pyridine (Acetylation)": {
        "rules": [
            # Converts 1-degree aromatic and aliphatic amines to Acetamides
            # The nitrogen lone pair is now delocalized into the carbonyl, dropping its basicity!
            "[c,CX4:1]-[NX3H2:2] >> [c,C:1]-[NH1:2]-[C](=O)-[CH3]",
            
            # Converts 2-degree amines to N-substituted Acetamides
            "[#6:1]-[NX3H1:2]-[#6:3] >> [#6:1]-[N:2](-[#6:3])-[C](=O)-[CH3]"
        ]
    },
    
    # --- 2. ALCOHOL PROTECTION (SILYL ETHERS) ---
    "TMSCl / Triethylamine (TMS Protection)": {
        "rules": [
            # Caps a primary, secondary, or tertiary alcohol with a Trimethylsilyl group.
            # This completely removes the acidic proton, rendering the molecule safe for Grignards.
            "[#6,c:1]-[OX2H1:2] >> [#6,c:1]-[O:2]-[Si](-[CH3])(-[CH3])-[CH3]"
        ]
    },
    
    # --- 3. CARBONYL PROTECTION (ACETALS/KETALS) ---
    # (Cross-referenced from Aldehyde/Ketone module for synthetic completeness)
    "Ethylene Glycol / H+ (Dean-Stark Trap)": {
        "rules": [
            # Wraps the carbonyl into a stable 5-membered 1,3-dioxolane ring.
            # Safe against nucleophiles and bases (LiAlH4, Grignards, NaOH).
            "[CX3:1]=O >> [C:1]1-[O]-[CH2]-[CH2]-[O]-1"
        ]
    },

    # --- DEPROTECTION (THE UNLOCK CODES) ---
    
    # Universal Acidic Hydrolysis (Unmasks Amines and Carbonyls)
    "H3O+ / Heat (Global Deprotection)": {
        "rules": [
            # 1. Cleave Amide back to Amine (Reverses Acetylation)
            "[c,CX4:1]-[NH1:2]-[C](=O)-[CH3] >> [c,C:1]-[NX3H2:2]",
            "[#6:1]-[N:2](-[#6:3])-[C](=O)-[CH3] >> [#6:1]-[NX3H1:2]-[#6:3]",
            
            # 2. Cleave Acetal back to Carbonyl
            "[C:1]1-[O]-[CH2]-[CH2]-[O]-1 >> [C:1]=O",
            
            # 3. Cleave TMS back to Alcohol
            "[#6,c:1]-[O:2]-[Si](-[CH3])(-[CH3])-[CH3] >> [#6,c:1]-[OX2H1:2]"
        ]
    },
    
    # Orthogonal Fluoride Cleavage (Strictly for Silyl Ethers)
    "TBAF / THF (Selective TMS Deprotection)": {
        "rules": [
            # Tetra-n-butylammonium fluoride (TBAF) supplies F- ions.
            # Silicon has a massive affinity for Fluorine (due to empty d-orbitals).
            # This selectively snaps off the TMS group while leaving Acetals and Amides completely untouched!
            "[#6,c:1]-[O:2]-[Si](-[CH3])(-[CH3])-[CH3] >> [#6,c:1]-[OX2H1:2]"
        ],
        "poisons": ["[CX3]=O"], # Standard warning, though mathematically unnecessary if rules are exact
        "poison_message": "TBAF is highly selective for Si-O bonds. It will safely deprotect your alcohol without harming other sensitive groups!"
    }
}