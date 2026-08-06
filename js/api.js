export const AppState = {
    ketcherInstance: null,
    customDictionary: null,
    reagentDatabase: {},
    sortedReagents: []
};

// Change this to your live Render URL once deployed (e.g., 'https://rxn-api.onrender.com')
// If running everything on the same server, you can change this back to an empty string ''.
const API_BASE_URL = 'http://localhost:8000'; 

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