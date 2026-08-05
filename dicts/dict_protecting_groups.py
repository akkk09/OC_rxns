# ==========================================
# PROTECTING GROUPS ENGINE (MASKING & DEPROTECTION - OLYMPIAD LEVEL)
# ==========================================

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
PROTECTING_GROUP_RULES = {

    # ==========================================
    # 1. AMINE PROTECTION (ANILINE & ALIPHATIC MASKING)
    # ==========================================

    "(CH3CO)2O / Pyridine (Amine Acetylation via Nucleophilic Acyl Substitution)": {
        "rules": [
            # Converts primary aromatic and aliphatic amines to acetamides.
            # The nitrogen lone pair is delocalized into the carbonyl pi system, drastically lowering basicity and nucleophilicity.
            "[c,CX4:1]-[NX3H2:2] >> [c,C:1]-[NH1:2]-[C](=O)-[CH3]",
            
            # Converts secondary amines to N-substituted acetamides
            "[#6:1]-[NX3H1:2]-[#6:3] >> [#6:1]-[N:2](-[#6:3])-[C](=O)-[CH3]"
        ]
    },
    
    # ==========================================
    # 2. ALCOHOL PROTECTION (SILYL ETHER MASKING)
    # ==========================================

    "TMSCl / Triethylamine (Trimethylsilyl Alcohol Protection)": {
        "rules": [
            # Caps primary, secondary, or tertiary alcohols with a trimethylsilyl group.
            # Completely removes the acidic proton, rendering the substrate safe for aggressive organometallic reagents.
            "[#6,c:1]-[OX2H1:2] >> [#6,c:1]-[O:2]-[Si](-[CH3])(-[CH3])-[CH3]"
        ]
    },
    
    # ==========================================
    # 3. CARBONYL PROTECTION (ACETAL / KETAL MASKING)
    # ==========================================

    "Ethylene Glycol / Catalytic Acid, Dean-Stark Trap (Cyclic Acetal / Ketal Synthesis)": {
        "rules": [
            # Converts aldehydes and ketones into stable five-membered 1,3-dioxolane rings.
            # Renders the carbonyl completely inert against strong nucleophiles and bases (LiAlH4, Grignards, NaOH).
            "[CX3:1]=O >> [C:1]1-[O]-[CH2]-[CH2]-[O]-1"
        ]
    },

    # ==========================================
    # 4. DEPROTECTION PROTOCOLS (ORTHOGONAL UNLOCKING)
    # ==========================================
    
    "Aqueous H3O+ / Heat (Global Acidic Deprotection)": {
        "rules": [
            # 1. Cleave acetamides back to primary/secondary amines (reverses acetylation)
            "[c,CX4:1]-[NH1:2]-[C](=O)-[CH3] >> [c,C:1]-[NX3H2:2]",
            "[#6:1]-[N:2](-[#6:3])-[C](=O)-[CH3] >> [#6:1]-[NX3H1:2]-[#6:3]",
            
            # 2. Cleave cyclic acetals/ketals back to parent carbonyls
            "[C:1]1-[O]-[CH2]-[CH2]-[O]-1 >> [C:1]=O",
            
            # 3. Cleave TMS silyl ethers back to free hydroxyl alcohols
            "[#6,c:1]-[O:2]-[Si](-[CH3])(-[CH3])-[CH3] >> [#6,c:1]-[OX2H1:2]"
        ]
    },
    
    "TBAF / THF (Orthogonal Fluoride-Induced Selective TMS Cleavage)": {
        "rules": [
            # Tetra-n-butylammonium fluoride supplies F- ions. 
            # The extreme silicon-fluorine bond affinity (driven by vacant d-orbitals) selectively snaps off the TMS group 
            # while leaving acetals, ketals, and amides completely intact!
            "[#6,c:1]-[O:2]-[Si](-[CH3])(-[CH3])-[CH3] >> [#6,c:1]-[OX2H1:2]"
        ],
        "poisons": ["[CX3]=O"], 
        "poison_message": "TBAF is highly chemoselective for Si-O bonds. It cleanly unmasks your silyl ether without disturbing other sensitive functional groups."
    }
}