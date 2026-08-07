import { AppState } from './api.js';

export function getActiveModules() {
    const checkboxes = document.querySelectorAll('#defaultDicts input[type="checkbox"]:checked');
    return Array.from(checkboxes).map(cb => cb.value);
}

export function updateDropdownData() {
    const activeModules = getActiveModules();
    let activeReagents = new Set();
    
    activeModules.forEach(mod => {
        if (AppState.reagentDatabase[mod]) {
            AppState.reagentDatabase[mod].forEach(r => activeReagents.add(r));
        }
    });
    
    if (AppState.customDictionary) {
        Object.keys(AppState.customDictionary).forEach(r => activeReagents.add(r));
    }
    
    AppState.sortedReagents = Array.from(activeReagents).sort();
}

const searchInput = document.getElementById('reagent');
const dropdown = document.getElementById('custom-dropdown');

document.getElementById('themeBtn').addEventListener('click', () => {
    const ketcherFrame = document.getElementById('ketcher-frame');
    ketcherFrame.classList.toggle('ketcher-dark');
});

function debounce(func, wait) {
    let timeout;
    return function(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), wait);
    };
}

export function renderDropdown(filterText = '') {
    dropdown.innerHTML = '';
    const query = filterText.toLowerCase().trim();
    const filtered = AppState.sortedReagents.filter(r => r.toLowerCase().includes(query));

    if (filtered.length === 0) {
        dropdown.style.display = 'none';
        return;
    }


    const fragment = document.createDocumentFragment();
    filtered.forEach(r => {
        const div = document.createElement('div');
        div.className = 'dropdown-item';
        div.textContent = r;
        
        div.onclick = () => {
            const parts = searchInput.value.split('->');
            parts.pop(); 
            parts.push(' ' + r); 
            searchInput.value = parts.map(p => p.trim()).join(' -> ');
            dropdown.style.display = 'none';
            searchInput.focus();
        };
        fragment.appendChild(div);
    });
    
    dropdown.appendChild(fragment);
    dropdown.style.display = 'block';
}

export function hideDropdown() {
    dropdown.style.display = 'none';
}

const debouncedSearchHandler = debounce((e) => {
    const parts = e.target.value.split('->');
    renderDropdown(parts[parts.length - 1]);
}, 150);


export function initUI() {
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

    document.addEventListener('click', (e) => {
        if (!e.target.closest('.autocomplete-wrapper')) hideDropdown();
    });

    searchInput.addEventListener('input', debouncedSearchHandler);

    searchInput.addEventListener('focus', () => {
        const parts = searchInput.value.split('->');
        renderDropdown(parts[parts.length - 1]);
    });

    document.querySelectorAll('#defaultDicts input[type="checkbox"]').forEach(cb => {
        cb.addEventListener('change', updateDropdownData);
    });

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
                if (!AppState.customDictionary) AppState.customDictionary = {};
                Object.assign(AppState.customDictionary, uploadedDict);
                status.innerText = "✅ Custom dictionary loaded!";
                status.className = "upload-status upload-success";
                updateDropdownData(); 
            } catch (error) {
                status.innerText = "❌ Invalid JSON.";
                status.className = "upload-status upload-error";
            }
        };
        reader.readAsText(file);
    });

    document.getElementById('reagentForm').addEventListener('submit', function(e) {
        e.preventDefault();
        const name = document.getElementById('rbName').value.trim();
        const rule = document.getElementById('rbRule').value.trim();
        const poison = document.getElementById('rbPoison').value.trim();
        const poisonMsg = document.getElementById('rbPoisonMsg').value.trim();

        const newReagent = { "rules": [rule] };
        if (poison) {
            newReagent["poisons"] = [poison];
            newReagent["poison_message"] = poisonMsg || `Reaction poisoned by structural mismatch.`;
        }

        if (!AppState.customDictionary) AppState.customDictionary = {};
        AppState.customDictionary[name] = newReagent;

        updateDropdownData(); 

        const status = document.getElementById('builderStatus');
        status.innerText = "✅ Reagent injected!";
        status.className = "upload-status upload-success";

        setTimeout(() => {
            status.innerText = "";
            document.getElementById('reagentForm').reset();
            builderModal.style.display = 'none';
        }, 1200);
    });
}