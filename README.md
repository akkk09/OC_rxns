```markdown
# 🧪 High School Level Chemistry Simulator


A private, rule-based organic chemistry simulator designed to execute advanced, high school level chemistry simulations. This engine is built on a modular architecture that strictly separates chemical logic (dictionaries) from the processing engine, allowing for complex synthetic route planning, reaction chaining, and edge-case handling.

## ✨ Key Features

* **Modular Reaction Dictionaries:** Chemistry rules are defined using SMARTS strings (`Reactant >> Product`) and grouped into categorized Python dictionaries (e.g., Oxidation, Reduction, Protecting Groups).
* **Smart Exception Handling:** The engine natively supports chemical "poisons" and negative lookaheads (Recursive SMARTS) to accurately simulate textbook exceptions (e.g., blocking Friedel-Crafts on deactivated rings).
* **Reaction Chaining:** Supports multi-step synthetic pathways directly from the UI, allowing for advanced workarounds like aniline protection/deprotection schemes.
* **Interactive Molecular UI:** Integrates the Ketcher interface via an iframe for intuitive, professional-grade molecule drawing and product visualization.
* **Strict Chemical Sanity:** Powered by RDKit, the backend strictly enforces chemical valence and structural laws, intelligently filtering out impossible reaction pathways.

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, Vanilla JavaScript, Ketcher (iframe)
* **Backend:** Python, Flask
* **Cheminformatics Engine:** RDKit
* **Deployment:** Render (Web Service)

## 📁 Project Architecture

```text
OC_rxns/
├── public/                 # Frontend static assets
│   ├── ketcher/            # Molecule drawing interface
│   ├── index.html          
│   ├── style.css           
│   └── script.js           # API communication & UI logic
├── api/                    # Backend architecture
│   ├── dicts/              # Modular SMARTS reaction rules
│   │   ├── dict_oxidation.py
│   │   ├── dict_reduction.py
│   │   └── dict_protecting_groups.py
│   └── index.py            # Flask + RDKit Processing Engine
├── requirements.txt        # Production dependencies
└── README.md

```

## 🚀 Local Development Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/akkk09/OC_rxns.git](https://github.com/akkk09/OC_rxns.git)
cd OC_rxns

```


2. **Create a virtual environment (Recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```


3. **Install the dependencies:**
```bash
pip install -r requirements.txt

```


4. **Run the local development server:**
```bash
python api/index.py

```


*(Ensure your Flask app is set to run on `app.run(debug=True)` for local testing).*

## ☁️ Production Deployment

This application is configured for deployment on Render.
**Crucial Deployment Note:** Ensure the environment variable `PYTHON_VERSION` is set to `3.11.9` in your Render dashboard to guarantee compatibility with RDKit's pre-compiled binaries.

## 🔒 License & Copyright

All Rights Reserved.
