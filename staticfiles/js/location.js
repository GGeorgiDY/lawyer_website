// document.addEventListener('DOMContentLoaded', function () {
//     const form = document.querySelector('form');
//
//     form.addEventListener('submit', function (event) {
//         let isValid = true;
//
//         // Check the name field
//         const name = document.getElementById('name');
//         if (name.value.trim() === '') {
//             isValid = false;
//             alert('Name is required.');
//         }
//
//         // Check the email field
//         const email = document.getElementById('email');
//         const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
//         if (!emailPattern.test(email.value.trim())) {
//             isValid = false;
//             alert('Please enter a valid email address.');
//         }
//
//         // Check the message field
//         const message = document.getElementById('message');
//         if (message.value.trim() === '') {
//             isValid = false;
//             alert('Message is required.');
//         }
//
//         // Prevent form submission if validation fails
//         if (!isValid) {
//             event.preventDefault();
//         }
//     });
// });
