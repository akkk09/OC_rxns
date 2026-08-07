export const AppState = {
    ketcherInstance: null,
    customDictionary: null,
    reagentDatabase: {},
    sortedReagents: []
};

const API_BASE_URL = 'https://oc-rxns.onrender.com'; 

export async function fetchReagents() {
    try {
        const response = await fetch(`${API_BASE_URL}/reagents`);
        AppState.reagentDatabase = await response.json();
    } catch (error) {
        console.error("Failed to fetch reagents from server.", error);
    }
}

export async function executePrediction(payload) {
    const response = await fetch(`${API_BASE_URL}/predict`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });
    return await response.json();
}