// Simulating data fetch for user profile
document.addEventListener("DOMContentLoaded", () => {
    // Get elements
    const userNameElement = document.getElementById("user-name");
    const siteNameElement = document.getElementById("site-name");
    const siteLinkElement = document.getElementById("site-link");
    const siteStatusElement = document.getElementById("site-status");

    // Simulate a user profile
    const userProfile = {
        name: "John Doe",
        websiteName: "YourSite",
        websiteLink: "www.yoursite.com",
        websiteStatus: "Deployed"
    };

    // Populate dashboard with user data
    userNameElement.textContent = userProfile.name;
    siteNameElement.textContent = userProfile.websiteName;
    siteLinkElement.href = `https://${userProfile.websiteLink}`;
    siteLinkElement.textContent = userProfile.websiteLink;
    siteStatusElement.textContent = userProfile.websiteStatus;

    // Add event listeners for buttons
    const manageSiteButton = document.getElementById("manage-site-btn");
    const updateProfileButton = document.getElementById("update-profile-btn");
    const logoutButton = document.getElementById("logout-btn");

    manageSiteButton.addEventListener("click", () => {
        alert("Managing your website...");
    });

    updateProfileButton.addEventListener("click", () => {
        alert("Update profile functionality...");
    });

    logoutButton.addEventListener("click", () => {
        alert("Logging out...");
    });
});
