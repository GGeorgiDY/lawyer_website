let currentLanguage = localStorage.getItem('selectedLanguage') || 'en'; // Get language from localStorage or default to 'en'
let translations = {}; // This will hold the loaded translations

// Function to update text content based on selected language
function updateLanguage(lang) {
    console.log("Updating language to:", lang);

    if (translations[lang]) {
        // Your existing code to update the page content based on language
    } else {
        console.error(`Translations for language '${lang}' not found.`);
    }

    if (translations[lang]) {
        // Update menu links
        document.getElementById('home-link').textContent = translations[lang].home;
        document.getElementById('about-link').textContent = translations[lang].about;
        document.getElementById('news-link').textContent = translations[lang].news;
        document.getElementById('location-link').textContent = translations[lang].location;

        // Update login/logout links if they exist
        const profileLink = document.getElementById('profile-link');
        const logoutLink = document.getElementById('logout-link');
        const loginLink = document.getElementById('login-link');
        const registerLink = document.getElementById('register-link');

        if (profileLink) profileLink.textContent = translations[lang].profile;
        if (logoutLink) logoutLink.textContent = translations[lang].logout;
        if (loginLink) loginLink.textContent = translations[lang].login;
        if (registerLink) registerLink.textContent = translations[lang].register;

        // Update static text on the homepage if the elements exist
        if (document.getElementById('welcome-message')) {
            document.getElementById('welcome-message').textContent = translations[lang].welcome_message;
        }
        if (document.getElementById('services-description')) {
            document.getElementById('services-description').textContent = translations[lang].services_description;
        }
        if (document.getElementById('learn-more-button')) {
            document.getElementById('learn-more-button').textContent = translations[lang].learn_more;
        }
        if (document.getElementById('our-lawyers-title')) {
            document.getElementById('our-lawyers-title').textContent = translations[lang].our_lawyers;
        }
        if (document.getElementById('our-lawyers-description')) {
            document.getElementById('our-lawyers-description').textContent = translations[lang].our_lawyers_description;
        }
        if (document.getElementById('view-lawyers-button')) {
            document.getElementById('view-lawyers-button').textContent = translations[lang].view_lawyers;
        }
        if (document.getElementById('our-services-title')) {
            document.getElementById('our-services-title').textContent = translations[lang].our_services;
        }
        if (document.getElementById('our-services-description')) {
            document.getElementById('our-services-description').textContent = translations[lang].our_services_description;
        }
        if (document.getElementById('view-services-button')) {
            document.getElementById('view-services-button').textContent = translations[lang].view_services;
        }
        if (document.getElementById('news-insights-title')) {
            document.getElementById('news-insights-title').textContent = translations[lang].news_insights;
        }
        if (document.getElementById('news-insights-description')) {
            document.getElementById('news-insights-description').textContent = translations[lang].news_insights_description;
        }
        if (document.getElementById('read-news-button')) {
            document.getElementById('read-news-button').textContent = translations[lang].read_news;
        }


        // location webpage
        if (document.getElementById('location_for_direct_contacts')) {
            document.getElementById('location_for_direct_contacts').textContent = translations[lang].location_for_direct_contacts;
        }
        if (document.getElementById('location_address')) {
            document.getElementById('location_address').textContent = translations[lang].location_address;
        }
        if (document.getElementById('location_working_time')) {
            document.getElementById('location_working_time').textContent = translations[lang].location_working_time;
        }
        if (document.getElementById('read-news-button')) {
            document.getElementById('read-news-button').textContent = translations[lang].read_news;
        }

        console.log("Language updated successfully");
    } else {
        console.error(`Translations for language '${lang}' not found.`);
    }
}

// // Function to toggle language and update localStorage
// function toggleLanguage() {
//     currentLanguage = currentLanguage === 'en' ? 'bg' : 'en';
//     localStorage.setItem('selectedLanguage', currentLanguage);
//     document.getElementById('language-switcher').textContent = currentLanguage === 'en' ? 'BG' : 'EN';
//     updateLanguage(currentLanguage);
// }
//
// // Function to load translations from Django view
// function loadTranslations() {
//     fetch('/translations/')
//         .then(response => {
//             console.log("Fetch response status:", response.status);  // Log status code
//             if (!response.ok) {
//                 throw new Error('Network response was not ok');
//             }
//             return response.json();
//         })
//         .then(data => {
//             console.log("Fetched translations data:", data);  // Log the fetched data
//             translations = data;
//             updateLanguage(currentLanguage);
//         })
//         .catch(error => console.error('Error fetching translations:', error));
// }
//
// // Initialize page on load
// document.addEventListener('DOMContentLoaded', function() {
//     loadTranslations(); // Load translations from the Django view
//
//     // Set the button text based on the current language
//     document.getElementById('language-switcher').textContent = currentLanguage === 'en' ? 'BG' : 'EN';
// });
//
// // Add event listener to the language switcher button
// document.getElementById('language-switcher').addEventListener('click', toggleLanguage);





// Function to toggle language and update localStorage
function switchLanguage(lang) {
    currentLanguage = lang;
    localStorage.setItem('selectedLanguage', currentLanguage);
    updateLanguage(currentLanguage);

    // Toggle the visibility of the flags
    if (currentLanguage === 'en') {
        document.getElementById('flag-en').style.display = 'block';
        document.getElementById('flag-bg').style.display = 'none';
    } else {
        document.getElementById('flag-en').style.display = 'none';
        document.getElementById('flag-bg').style.display = 'block';
    }
}

// Function to load translations from Django view
function loadTranslations() {
    fetch('/translations/')
        .then(response => response.json())
        .then(data => {
            translations = data;
            updateLanguage(currentLanguage);
            // Set the correct initial flag visibility based on the stored language
            switchLanguage(currentLanguage);
        })
        .catch(error => console.error('Error fetching translations:', error));
}

// Initialize page on load
document.addEventListener('DOMContentLoaded', function() {
    loadTranslations();

    // Add click event listeners to the flag images
    document.getElementById('flag-en').addEventListener('click', function() {
        switchLanguage('bg'); // Switch to Bulgarian
    });

    document.getElementById('flag-bg').addEventListener('click', function() {
        switchLanguage('en'); // Switch to English
    });
});