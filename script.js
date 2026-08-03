let ketcherInstance = null;

// 1. Wait for Ketcher to initialize inside the iframe
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

// 2. Fetch loaded rules to populate the datalist
async function loadReagents() {
    try {
        const response = await fetch('/reagents');
        const reagents = await response.json();
        
        const datalist = document.getElementById('reagent-list');
        datalist.innerHTML = ''; 
        
        reagents.forEach(r => {
            const opt = document.createElement('option');
            opt.value = r;
            datalist.appendChild(opt);
        });
    } catch (error) {
        console.error("Failed to load reagents.", error);
    }
}
loadReagents();

// 3. Process the reaction (Now with Chain Support!)
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

        // Split by "->" to allow for multi-step synthesis chaining
        const sequence = rawInput.split('->').map(r => r.trim()).filter(r => r);

        for (let i = 0; i < sequence.length; i++) {
            const currentReagent = sequence[i];

            const response = await fetch('/predict', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ smiles: currentSmiles, reagent: currentReagent })
            });

            const data = await response.json();

            if (data.product_smiles) {
                currentSmiles = data.product_smiles;
                // Visually update the canvas at each step in the chain
                await ketcherInstance.setMolecule(currentSmiles);
            } else {
                alert(`Chain broke at Step ${i + 1} (${currentReagent}): ${data.message}`);
                return; // Stop the chain if a reaction fails
            }
        }

    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred. Make sure your Python server is running.");
    }
}