let ketcherInstance = null;
let customDictionary = null; 
let reagentDatabase = {}; 
let sortedReagents = []; // Stores the sorted flat list for the custom dropdown

function waitForKetcher() {
    const iframe = document.getElementById('ketcher-frame');
    if (iframe.contentWindow && iframe.contentWindow.ketcher) {
        ketcherInstance = iframe.contentWindow.ketcher;
        console.log("Ketcher successfully connected!");
    } else {
        setTimeout(waitForKetcher, 500);
    }
}
document.getElementById('ketcher-frame').addEventListener('load', waitForKetcher);

async function loadReagents() {
    try {
        const response = await fetch('/reagents');
        reagentDatabase = await response.json();
        updateDropdownData();
    } catch (error) {
        console.error("Failed to load reagents.", error);
    }
}
loadReagents();

function getActiveModules() {
    const checkboxes = document.querySelectorAll('#defaultDicts input[type="checkbox"]:checked');
    return Array.from(checkboxes).map(cb => cb.value);
}

// Gathers active reagents into an array for the custom dropdown
function updateDropdownData() {
    const activeModules = getActiveModules();
    let activeReagents = new Set();
    
    activeModules.forEach(mod => {
        if (reagentDatabase[mod]) {
            reagentDatabase[mod].forEach(r => activeReagents.add(r));
        }
    });
    
    if (customDictionary) {
        Object.keys(customDictionary).forEach(r => activeReagents.add(r));
    }
    
    sortedReagents = Array.from(activeReagents).sort();
}

// --- Custom Autocomplete UI Logic ---
const searchInput = document.getElementById('reagent');
const dropdown = document.getElementById('custom-dropdown');

function renderDropdown(filterText = '') {
    dropdown.innerHTML = '';
    const query = filterText.toLowerCase().trim();

    const filtered = sortedReagents.filter(r => r.toLowerCase().includes(query));

    if (filtered.length === 0) {
        dropdown.style.display = 'none';
        return;
    }

    filtered.forEach(r => {
        const div = document.createElement('div');
        div.className = 'dropdown-item';
        div.textContent = r;
        
        // Handle clicking a suggestion
        div.onclick = () => {
            // Allows users to chain reagents smoothly (e.g. "Step1 -> Step2")
            const parts = searchInput.value.split('->');
            parts.pop(); // Remove the incomplete part they were typing
            parts.push(' ' + r); // Append the completed selected reagent
            
            // Format cleanly back into the input box
            searchInput.value = parts.map(p => p.trim()).join(' -> ');
            dropdown.style.display = 'none';
            searchInput.focus();
        };
        dropdown.appendChild(div);
    });
    
    dropdown.style.display = 'block';
}

// Listen to typing to filter dropdown based on current chain segment
searchInput.addEventListener('input', (e) => {
    const parts = e.target.value.split('->');
    const currentQuery = parts[parts.length - 1]; // Filter using only the current step
    renderDropdown(currentQuery);
});

// Show dropdown on click/focus
searchInput.addEventListener('focus', () => {
    const parts = searchInput.value.split('->');
    const currentQuery = parts[parts.length - 1];
    renderDropdown(currentQuery);
});

// Hide dropdown when clicking outside of it
document.addEventListener('click', (e) => {
    if (!e.target.closest('.autocomplete-wrapper')) {
        dropdown.style.display = 'none';
    }
});


// --- Modal UI Controls ---
const dictModal = document.getElementById('dictModal');
const builderModal = document.getElementById('builderModal');

document.getElementById('settingsBtn').onclick = () => dictModal.style.display = 'flex';
document.getElementById('closeModal').onclick = () => dictModal.style.display = 'none';

document.getElementById('builderBtn').onclick = () => builderModal.style.display = 'flex';
document.getElementById('closeBuilderModal').onclick = () => builderModal.style.display = 'none';

window.onclick = (e) => { 
    if (e.target === dictModal) dictModal.style.display = 'none'; 
    if (e.target === builderModal) builderModal.style.display = 'none';
};

// Listen for checkbox toggles
document.querySelectorAll('#defaultDicts input[type="checkbox"]').forEach(cb => {
    cb.addEventListener('change', updateDropdownData);
});

// JSON File Upload Handler
document.getElementById('customDictUpload').addEventListener('change', function(event) {
    const file = event.target.files[0];
    const status = document.getElementById('uploadStatus');
    if (!file) {
        status.innerText = "";
        updateDropdownData(); 
        return;
    }

    const reader = new FileReader();
    reader.onload = function(e) {
        try {
            const uploadedDict = JSON.parse(e.target.result);
            if (!customDictionary) customDictionary = {};
            Object.assign(customDictionary, uploadedDict);
            
            status.innerText = "✅ Custom dictionary loaded dynamically!";
            status.className = "upload-status upload-success";
            updateDropdownData(); 
        } catch (error) {
            status.innerText = "❌ Invalid JSON format.";
            status.className = "upload-status upload-error";
        }
    };
    reader.readAsText(file);
});


// --- Reagent Builder Submission Handler ---
document.getElementById('reagentForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const name = document.getElementById('rbName').value.trim();
    const rule = document.getElementById('rbRule').value.trim();
    const poison = document.getElementById('rbPoison').value.trim();
    const poisonMsg = document.getElementById('rbPoisonMsg').value.trim();

    const newReagent = {
        "rules": [rule]
    };

    if (poison) {
        newReagent["poisons"] = [poison];
        newReagent["poison_message"] = poisonMsg || `Reaction poisoned by structural mismatch.`;
    }

    if (!customDictionary) customDictionary = {};
    customDictionary[name] = newReagent;

    updateDropdownData(); // Make available immediately

    const status = document.getElementById('builderStatus');
    status.innerText = "✅ Reagent successfully injected!";
    status.className = "upload-status upload-success";

    setTimeout(() => {
        status.innerText = "";
        document.getElementById('reagentForm').reset();
        builderModal.style.display = 'none';
    }, 1200);
});

// --- Simulation Execution Logic ---
async function runReaction() {
    if (!ketcherInstance && document.getElementById('ketcher-frame').contentWindow.ketcher) {
        ketcherInstance = document.getElementById('ketcher-frame').contentWindow.ketcher;
    }

    if (!ketcherInstance) {
        alert("Ketcher is still starting up. Please wait a second.");
        return;
    }

    try {
        let currentSmiles = await ketcherInstance.getSmiles();
        if (!currentSmiles) {
            alert("Please draw a molecule first!");
            return;
        }

        const rawInput = document.getElementById('reagent').value;
        if (!rawInput) {
            alert("Please select or type a reagent!");
            return;
        }

        dropdown.style.display = 'none'; // Ensure UI is clean on run

        const sequence = rawInput.split('->').map(r => r.trim()).filter(r => r);
        const activeModules = getActiveModules();

        for (let i = 0; i < sequence.length; i++) {
            const currentReagent = sequence[i];

            const response = await fetch('/predict', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 
                    smiles: currentSmiles, 
                    reagent: currentReagent,
                    active_modules: activeModules,
                    custom_dictionary: customDictionary 
                })
            });

            const data = await response.json();

            if (data.product_smiles) {
                currentSmiles = data.product_smiles;
                await ketcherInstance.setMolecule(currentSmiles);
            } else {
                alert(`Chain broke at Step ${i + 1} (${currentReagent}): ${data.message}`);
                return;
            }
        }
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred. Make sure your Python server is running.");
    }
}