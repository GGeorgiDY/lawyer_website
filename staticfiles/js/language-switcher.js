let currentLanguage = localStorage.getItem('selectedLanguage') || 'en'; // Get language from localStorage or default to 'en'
let translations = {}; // This will hold the loaded translations

// Function to update text content based on selected language
function updateLanguage(lang) {
    console.log("Updating language to:", lang);  // Debugging

    if (translations[lang]) {
        document.getElementById('home-link').textContent = translations[lang].home;
        document.getElementById('about-link').textContent = translations[lang].about;
        document.getElementById('news-link').textContent = translations[lang].news;
        document.getElementById('location-link').textContent = translations[lang].location;

        const profileLink = document.getElementById('profile-link');
        const logoutLink = document.getElementById('logout-link');
        const loginLink = document.getElementById('login-link');
        const registerLink = document.getElementById('register-link');

        if (profileLink) profileLink.textContent = translations[lang].profile;
        if (logoutLink) logoutLink.textContent = translations[lang].logout;
        if (loginLink) loginLink.textContent = translations[lang].login;
        if (registerLink) registerLink.textContent = translations[lang].register;

        console.log("Language updated successfully");  // Debugging
    } else {
        console.error(`Translations for language '${lang}' not found.`);
    }
}

// Function to toggle language and update localStorage
function toggleLanguage() {
    currentLanguage = currentLanguage === 'en' ? 'bg' : 'en';
    localStorage.setItem('selectedLanguage', currentLanguage);
    document.getElementById('language-switcher').textContent = currentLanguage === 'en' ? 'BG' : 'EN';
    updateLanguage(currentLanguage);
}

// Function to load translations from Django view
function loadTranslations() {
    fetch('/translations/')
        .then(response => {
            console.log("Fetch response status:", response.status);  // Log status code
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log("Fetched translations data:", data);  // Log the fetched data
            translations = data;
            updateLanguage(currentLanguage);
        })
        .catch(error => console.error('Error fetching translations:', error));
}


// Initialize page on load
document.addEventListener('DOMContentLoaded', function() {
    loadTranslations(); // Load translations from the Django view

    // Set the button text based on the current language
    document.getElementById('language-switcher').textContent = currentLanguage === 'en' ? 'BG' : 'EN';
});

// Add event listener to the language switcher button
document.getElementById('language-switcher').addEventListener('click', toggleLanguage);
