document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    const signupForm = document.getElementById('signupForm');
    const showSignup = document.getElementById('showSignup');
    const showLogin = document.getElementById('showLogin');
    const backgroundAnimation = document.getElementById('backgroundAnimation');

    // Initially show login form
    loginForm.classList.add('active');
    backgroundAnimation.style.background = "radial-gradient(circle, #ff7eb3, #6a82fb)";

    // Show Signup form and hide Login form when "Sign Up" is clicked
    showSignup.addEventListener('click', function() {
        loginForm.classList.remove('active');
        signupForm.classList.add('active');
        backgroundAnimation.style.background = "radial-gradient(circle, #ff7eb3, #6a82fb)";
        backgroundAnimation.style.animation = "rotateBackground 10s infinite linear";
    });

    // Show Login form and hide Signup form when "Login" is clicked
    showLogin.addEventListener('click', function() {
        signupForm.classList.remove('active');
        loginForm.classList.add('active');
        backgroundAnimation.style.background = "radial-gradient(circle, #ff7eb3, #6a82fb)";
        backgroundAnimation.style.animation = "rotateBackground 10s infinite linear";
    });

    // Handle "Forgot Password" functionality
    document.querySelector('.forgot-password').addEventListener('click', function() {
        alert("Password recovery feature coming soon!");
    });
});
