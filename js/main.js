import { AppState, fetchReagents, executePrediction } from './api.js';
import { initUI, updateDropdownData, getActiveModules, hideDropdown } from './ui.js';

function waitForKetcher() {
    const iframe = document.getElementById('ketcher-frame');
    if (iframe.contentWindow && iframe.contentWindow.ketcher) {
        AppState.ketcherInstance = iframe.contentWindow.ketcher;
        console.log("Ketcher successfully connected!");
    } else {
        setTimeout(waitForKetcher, 500);
    }
}

async function initApp() {
    document.getElementById('ketcher-frame').addEventListener('load', waitForKetcher);
    initUI();
    await fetchReagents();
    updateDropdownData();
}

document.addEventListener('DOMContentLoaded', initApp);

document.getElementById('predictBtn').addEventListener('click', async () => {
    if (!AppState.ketcherInstance) {
        alert("Ketcher is still loading. Please wait.");
        return;
    }

    try {
        let currentSmiles = await AppState.ketcherInstance.getSmiles();
        if (!currentSmiles) {
            alert("Please draw a molecule first!");
            return;
        }

        const searchInput = document.getElementById('reagent');
        if (!searchInput.value) {
            alert("Please select a reagent!");
            return;
        }

        hideDropdown();
        const sequence = searchInput.value.split('->').map(r => r.trim()).filter(r => r);
        const activeModules = getActiveModules();

        for (let i = 0; i < sequence.length; i++) {
            const currentReagent = sequence[i];

            const data = await executePrediction({ 
                smiles: currentSmiles, 
                reagent: currentReagent,
                active_modules: activeModules,
                custom_dictionary: AppState.customDictionary 
            });

            if (data.product_smiles) {
                currentSmiles = data.product_smiles;
                await AppState.ketcherInstance.setMolecule(currentSmiles);
            } else {
                alert(`Chain broke at Step ${i + 1} (${currentReagent}): ${data.message}`);
                return;
            }
        }
    } catch (error) {
        console.error("Error:", error);
        alert("Server error. Make sure Python is running.");
    }
});