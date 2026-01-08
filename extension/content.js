// Variables to manage cooldown
let lastTriggerTime = 0;
const COOLDOWN_MS = 50

// Default settings cache
let settings = {
    enableExtension: true,
    hoverPattern: "single",
    clickPattern: "single",
    cursorPattern: "single"
};

// Initialize settings
chrome.storage.local.get(settings, (items) => {
    settings = items;
});

// Update settings when they change
chrome.storage.onChanged.addListener((changes) => {
    for (let key in changes) {
        if (settings.hasOwnProperty(key)) {
            settings[key] = changes[key].newValue;
        }
    }
});

// Function to trigger haptic feedback
function triggerHaptic(source, pattern) {
    // If pattern is "none", it means disabled
    if (!pattern || pattern === "none") return;

    const now = Date.now();

    // Check cooldown
    if (now - lastTriggerTime < COOLDOWN_MS) {
        return;
    }

    // Check if extension is enabled
    if (!settings.enableExtension) {
        return;
    }

    lastTriggerTime = now;
    // Always use Channel 1 for this simplified version
    const channel = 1;

    // Send message to background script
    chrome.runtime.sendMessage({
        type: "TRIGGER_HAPTIC",
        source: source,
        channel: channel,
        pattern: pattern
    });
}

// Variables variables
let lastInteractiveElement = null; // Track Hover Heuristic
let isPointerActive = false;       // Track Cursor Style

// Hover Event Listener
document.addEventListener('mouseover', (event) => {
    const target = event.target;

    // --- LOGIQUE 1 : HOVER PATTERN (Sémantique) ---
    if (settings.hoverPattern && settings.hoverPattern !== 'none') {
        const element = target.closest('a, button, [role="button"], input[type="submit"], input[type="button"], [onclick], [ng-click], .btn, .button, .clickable');

        if (element) {
            // Check doublon élément
            if (element !== lastInteractiveElement) {
                lastInteractiveElement = element;
                // Check disabled
                if (!element.hasAttribute('disabled') && !element.classList.contains('disabled')) {
                    triggerHaptic("HOVER", settings.hoverPattern);
                }
            }
        } else {
            // Si on ne survole plus rien de sémantique, on ne reset PAS forcément lastInteractiveElement
            // car mouseover peut bubbler. Mais si on arrive sur "rien", on reset.
            // Simplified: mouseout handles deep reset, but here if transition to non-element...
            // element is null.
            // On peut reset lastInteractiveElement s'il n'est pas un ancêtre de target ?
            // target.closest(...) is null means we represent not inside one.
            lastInteractiveElement = null;
        }
    }

    // --- LOGIQUE 2 : CURSOR PATTERN (Visuel) ---
    if (settings.cursorPattern && settings.cursorPattern !== 'none') {
        const style = window.getComputedStyle(target);
        const isPointer = (style.cursor === 'pointer');

        if (isPointer) {
            if (!isPointerActive) {
                isPointerActive = true;
                triggerHaptic("CURSOR", settings.cursorPattern);
            }
        } else {
            isPointerActive = false;
        }
    }
});

// Reset lastInteractiveElement quand la souris quitte la fenêtre ou le document
document.addEventListener('mouseout', (event) => {
    // Si on sort de l'élément interactif actuel
    if (lastInteractiveElement) {
        // Vérifier si we quitte vraiment l'élément suivi (pas juste vers un enfant)
        // Mais mouseout buble, donc event.target est l'élément quitté.
        // Si event.target est ou contient lastInteractiveElement...
        // Simplification: On reset que si on sort vers "rien" ou un autre élément non interactif.
        // La logique de mouseover gère le changement d'élément.
    }

    if (event.relatedTarget === null) {
        lastInteractiveElement = null;
    }
});

// Click Event Listener
document.addEventListener('click', (event) => {
    const target = event.target;

    // Ignore Inputs and Textareas
    if (target.tagName === 'INPUT' || target.tagName === 'TEXTAREA') {
        return;
    }

    triggerHaptic("CLICK", settings.clickPattern);
});

//console.log("[MX4] Content script loaded (Multi-Channel Version).");
