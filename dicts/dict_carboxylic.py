# ==========================================
# CARBOXYLIC ACIDS & DERIVATIVES ENGINE
# ==========================================

# --- ALPHA-HYDROGEN & AMIDE POISONS ---
NO_ALPHA_H = ["[CX4H0]-[CX3](=O)[OH]", "[c]-[CX3](=O)[OH]"] # Tertiary or aromatic acids
SUBSTITUTED_AMIDES = ["[CX3](=O)-[NX3H1]", "[CX3](=O)-[NX3H0]"] # 2-degree and 3-degree amides

# ==========================================
# THE REAGENT DICTIONARY
# ==========================================
CARBOXYLIC_RULES = {

    # --- ACID DERIVATIVE SYNTHESIS ---
    "SOCl2 / Pyridine (Thionyl Chloride)": {
        "rules": [
            # Converts Carboxylic Acids to Acid Chlorides
            "[CX3:1](=O)[OH] >> [C:1](=O)[Cl]",
            
            # (Bonus: Also cleanly converts Alcohols to Alkyl Chlorides via SN2)
            "[CX4:1]-[OH] >> [C:1]-[Cl]"
        ]
    },
    "H+ / Heat (Fischer Esterification)": {
        "rules": [
            # Bimolecular condensation: Acid + Alcohol -> Ester + Water
            # RDKit links the carbonyl carbon directly to the alcohol's oxygen.
            "[CX3:1](=O)[OH].[CX4,c:2]-[OH] >> [C:1](=O)-[O]-[C,c:2]"
        ]
    },
    
    # --- DECARBOXYLATION (CHAIN STEP-DOWN) ---
    "NaOH / CaO, Heat (Soda-Lime Decarboxylation)": {
        "rules": [
            # Cleaves the entire carboxylate group, replacing it with a hydrogen
            # Works on both aliphatic and aromatic acids/salts
            "[#6,c:1]-[CX3](=O)[OH,O-] >> [#6,c:1]"
        ]
    },
    "Mild Heat (Beta-Keto Acid Decarboxylation)": {
        "rules": [
            # Strictly looks for a ketone at the beta position!
            # The CO2 is lost, and the alpha-carbon takes the hydrogen.
            "[CX3:1](=O)-[CX4:2]-[CX3](=O)[OH] >> [C:1](=O)-[C:2]"
        ],
        "poisons": ["[CX4]-[CX3](=O)[OH]", "[c]-[CX3](=O)[OH]"], 
        "poison_message": "Standard carboxylic acids do not decarboxylate under mild heat. This requires a beta-carbonyl group to facilitate a cyclic transition state, or harsh reagents like Soda-Lime."
    },

    # --- ALPHA-HALOGENATION ---
    "Br2 / Red Phosphorus (HVZ Reaction)": {
        "rules": [
            # Hell-Volhard-Zelinsky: Substitutes an alpha-hydrogen with Bromine
            "[CX4H1,CX4H2,CX4H3:1]-[CX3](=O)[OH:2] >> [C:1](-[Br])-[C](=O)[OH:2]"
        ],
        "poisons": NO_ALPHA_H,
        "poison_message": "The HVZ reaction strictly requires at least one alpha-hydrogen. Acids like Pivalic acid or Benzoic acid will not react!"
    },

    # --- AMIDE DEGRADATION (THE JEE FAVORITE) ---
    "Br2 / NaOH (Hoffmann Bromamide Degradation)": {
        "rules": [
            # Chain step-down: Primary Amide -> Primary Amine
            # Notice how the carbonyl carbon is intentionally left unmapped. 
            # RDKit deletes it and bonds the R-group directly to the Nitrogen!
            "[#6,c:1]-[CX3](=O)-[NX3H2:2] >> [#6,c:1]-[N:2]"
        ],
        "poisons": SUBSTITUTED_AMIDES,
        "poison_message": "Hoffmann Bromamide Degradation is strictly for primary (1°) amides. Secondary and tertiary amides lack the necessary protons to form the isocyanate intermediate."
    },

    # --- HYDROLYSIS (DERIVATIVES BACK TO ACIDS) ---
    "H3O+ / Heat (Derivative Hydrolysis)": {
        "rules": [
            # 1. Esters -> Acid (Alcohol fragment is cleaved via the dot '.')
            "[CX3:1](=O)-[OX2]-[CX4,c:2] >> [C:1](=O)[OH].[OH]-[C,c:2]",
            
            # 2. Amides -> Acid + Ammonium ion
            "[CX3:1](=O)-[NX3] >> [C:1](=O)[OH]",
            
            # 3. Acid Chlorides -> Acid
            "[CX3:1](=O)[Cl] >> [C:1](=O)[OH]",
            
            # 4. Acid Anhydrides -> Two Equivalents of Acid
            "[CX3:1](=O)-[O]-[CX3:2](=O) >> [C:1](=O)[OH].[C:2](=O)[OH]"
        ]
    }
}