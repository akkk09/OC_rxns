PROTECTING_GROUPS_RULES = {
    # 1. Ketone/Aldehyde Protection (Acetal Formation)
    # Uses Ethylene Glycol to form a cyclic acetal, protecting it from nucleophiles/reducers.
    "Ethylene Glycol / pTsOH (Protect Carbonyl)": [
        "[#6:1]-[C:2](=O)-[#6,H:3] >> [#6:1]-[C:2]1(-[O]-[CH2]-[CH2]-[O]1)-[#6,H:3]"
    ],

    # 2. Acetal Deprotection
    # Removes the cyclic acetal to restore the ketone/aldehyde.
    "H3O+ / Heat (Deprotect Acetal)": [
        "[#6:1]-[C:2]1(-[O]-[CH2]-[CH2]-[O]1)-[#6,H:3] >> [#6:1]-[C:2](=O)-[#6,H:3]"
    ],

    # 3. Amine Protection (Boc Protection)
    # Masks a primary amine with a bulky tert-butoxycarbonyl (Boc) group.
    "Boc2O / Et3N (Protect Amine)": [
        "[#6:1]-[NH2:2] >> [#6:1]-[NH:2]-[C](=O)-[O]-[C](C)(C)C"
    ],

    # 4. Amine Deprotection
    # Removes the Boc group using strong acid.
    "TFA / CH2Cl2 (Deprotect Amine)": [
        "[#6:1]-[NH:2]-[C](=O)-[O]-[C](C)(C)C >> [#6:1]-[NH2:2]"
    ]
}