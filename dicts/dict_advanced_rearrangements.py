# ==========================================
# ADVANCED REARRANGEMENTS & PERICYCLIC ENGINE (EXHAUSTIVE GRADUATE LEVEL)
# ==========================================

# --- ADVANCED STEREOELECTRONIC POISONS & MATRICES ---
NO_ANTI_PROTON = ["[CX4H0]-[CX3](=O)-[CHX4]-[Cl,Br,I]"] # Lacking required anti-periplanar alpha'-protons
TERTIARY_ALPHA_OXIME = ["[C](=[NX2]-[OH])-[CX4H0](-[#6])(-[#6])-[#6*]"] # Quaternary/Tertiary alpha systems for fragmentation

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
ADVANCED_REARRANGEMENT_RULES = {

    # ==========================================
    # 1. BASE-PROMOTED SKELETAL & RING CONTRACTIONS
    # ==========================================

    "NaOH / H2O, 0°C (Favorskii Rearrangement - Cyclopropanone Mechanism)": {
        "rules": [
            # Acyclic and cyclic alpha-halo ketones undergoing base-mediated enolization, 
            # intramolecular nucleophilic attack (cyclopropanone intermediate), and hydroxide ring-opening 
            # directed toward the more stable carbanion / less substituted framework.
            "[C:1]-[CX3:2](=O)-[CHX4H1,CHX4H2:3]-[Cl,Br,I:4] >> [C:1]-[CH1:3]-[CX3:2](=O)[OH]"
        ],
        "poisons": NO_ANTI_PROTON,
        "poison_message": "Favorskii rearrangement failure: The substrate lacks an enolizable proton on the carbon opposite (alpha') to the halogen atom, preventing the mandatory base-mediated intramolecular displacement."
    },

    "KOH / Thermal Fusion, then H3O+ (Benzilic Acid Rearrangement)": {
        "rules": [
            # 1,2-Diketone skeletal contraction via nucleophilic hydroxide addition 
            # followed by concerted 1,2-aryl or alkyl shift driven by migratory aptitude (Aryl > Alkyl).
            "[c,C:1]-[CX3:2](=O)-[CX3:3](=O)-[c,C:4] >> [c:1]-[CX3:2](-[OH])(-[c,C:4])-[CX3:3](=O)[OH]"
        ]
    },

    "Sodium Ethoxide / EtOH (Wolff Rearrangement of Alpha-Diazoketones)": {
        "rules": [
            # Silver- or thermal/photochemically induced loss of nitrogen gas yielding an alpha-ketocarbene,
            # which undergoes a concerted migratory rearrangement into a stable ketene species.
            "[#6:1]-[CX3](=O)-[CX2]=[N+]=[N-] >> [#6:1]-CH2-C(=O)OCC"
        ]
    },

    # ==========================================
    # 2. PERICYCLIC [3,3]-SIGMATROPIC SHIFTS
    # ==========================================

    "Thermal, 200°C (Aliphatic Claisen Rearrangement)": {
        "rules": [
            # Concerted, pericyclic [3,3]-sigmatropic shift of allyl vinyl ethers proceeding 
            # through an ordered, chair-like transition state to yield gamma,delta-unsaturated carbonyl compounds.
            "[OX2:1](-[C:2]=[C:3]-[#6])-[CH2:4]-[CH:5]=[CH2:6] >> [OX2:1]=[C:2]-[C:3]-[CH2:6]-[CH:5]=[CH2:4]"
        ]
    },
    
    "Thermal, 250°C (Aromatic / O-Aryl Claisen Rearrangement)": {
        "rules": [
            # Thermal rearrangement of allyl aryl ethers yielding ortho-allyl phenols 
            # via a transient cyclohexadienone intermediate that tautomerizes back to aromaticity.
            "[c:1]1[cH][cH][cH][cH][c]1-[O]-[CH2]-[CH:2]=[CH2:3] >> [c:1]1[cH][cH][cH][c](-[CH2]-[CH:2]=[CH2:3])[c]1-[OH]"
        ]
    },

    "Thermal, 300°C (Cope Rearrangement of 1,5-Dienes)": {
        "rules": [
            # Thermal [3,3]-sigmatropic isomerization of 1,5-diene frameworks proceeding via a boat or chair transition state.
            "[C:1]=[C:2]-[CH2:3]-[CH2:4]-[C:5]=[C:6] >> [CH2:1]=[CH:2]-[CH2:3]-[CH2:4]-[CH:5]=[CH2:6]"
        ]
    },

    "Cope Catalyst / Room Temp (Oxy-Cope Rearrangement)": {
        "rules": [
            # Base-promoted rearrangement of 1,5-diene-3-ols driven thermodynamically 
            # by irreversible tautomerization of the resulting enol product into a stable beta,gamma-unsaturated carbonyl.
            "[C:1]=[C:2]-[CH2:3]-[CH(OH)]-[C:5]=[C:6] >> [CH2:1]=[CH:2]-[CH2:3]-CH2-C(=O)-[#6]"
        ]
    },

    # ==========================================
    # 3. NITROGEN ACID-CATALYZED REARRANGEMENTS & FRAGMENTATIONS
    # ==========================================

    "H2SO4 / Thermal Conditions (Standard Beckmann Rearrangement)": {
        "rules": [
            # Acid-catalyzed conversion of oximes into N-substituted amides 
            # characterized by the strict anti-periplanar migration of the group trans to the hydroxyl leaving group.
            "[C:1](=[NX2:2]-[OH])-[CH2:3]-[#6] >> [C:1](=O)-[NH1:2]-[CH2:3]-[#6]"
        ]
    },

    "H2SO4 / Thermal Conditions (Beckmann Fragmentation Pathway)": {
        "rules": [
            # Stereoelectronic cleavage occurring when the alpha-carbon can stabilize an open carbocation 
            # (tertiary or quaternary center), bypassing amide formation to yield a nitrile and a trapped carbocation.
            "[C:1](=[NX2:2]-[OH])-[C:3](-[CH3])(-[CH3])(-[CH3]) >> [C:1]#[N:2].[C:3]-[OH]"
        ],
        "poisons": ["[C](=[N]-[OH])-[CH2H2]-[#6]"], 
        "poison_message": "Beckmann Fragmentation failure: Requires a stable tertiary or quaternary alpha-carbocation center. Unbranched oximes undergo standard Beckmann rearrangement to form amides."
    },

    "HN3 / H2SO4 (Schmidt Reaction on Ketones and Carboxylic Acids)": {
        "rules": [
            # Acid-mediated hydrazoic acid insertion into carbonyl frameworks, 
            # yielding amides from ketones or primary amines (via isocyanate intermediates) from carboxylic acids.
            "[#6:1]-[CX3:2](=O)-[#6,H:3] >> [#6:1]-[CX3:2](=O)-[NX3H1]-[#6,H:3]",
            "[#6:1]-[CX3:2](=O)-[OH] >> [#6:1]-[NX3H2]"
        ]
    },

    "HCl / Heat (Curtius / Lossen Rearrangement Sequence via Isocyanates)": {
        "rules": [
            # Thermal or chemical loss of nitrogen/leaving groups from acyl azides or hydroxamates 
            # to generate electrophilic isocyanate intermediates, trapping with water to yield primary amines.
            "[#6:1]-C(=O)-N=[N+]=[N-] >> [#6:1]-[NX3H2]+O=C=O"
        ]
    }
}