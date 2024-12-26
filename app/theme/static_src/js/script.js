// script.js

// Function to toggle navbar
function toggleNavbar(action) {
  const navbar = document.getElementById("navbar");
  const hamburgerIcon = document.getElementById("hamburger-icon");
  const closeIcon = document.getElementById("close-icon");

  if (navbar) {
    if (action === "open") {
      navbar.classList.remove("hidden"); // Show navbar
      hamburgerIcon.classList.add("hidden"); // Hide hamburger
      closeIcon.classList.remove("hidden"); // Show close button
    } else if (action === "close") {
      navbar.classList.add("hidden"); // Hide navbar
      hamburgerIcon.classList.remove("hidden"); // Show hamburger
      closeIcon.classList.add("hidden"); // Hide close button
    }
  } else {
    console.error("Navbar element not found");
  }
}

// Function to toggle dropdowns on hover
function toggleDropdown(dropdownId, show) {
  const dropdown = document.getElementById(dropdownId);
  if (dropdown) {
    dropdown.classList.toggle("hidden", !show);
  } else {
    console.error(`Dropdown element with ID ${dropdownId} not found`);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  // Services dropdown
  const servicesLink = document.getElementById("servicesLink");
  if (servicesLink) {
    servicesLink.addEventListener("mouseenter", () =>
      toggleDropdown("servicesLink", true)
    );
    servicesLink.addEventListener("mouseleave", () =>
      toggleDropdown("servicesLink", false)
    );
  } else {
    console.error("Element with ID 'servicesLink' not found");
  }

  // About dropdown
  const aboutLink = document.getElementById("aboutLink");
  if (aboutLink) {
    aboutLink.addEventListener("mouseenter", () =>
      toggleDropdown("aboutLink", true)
    );
    aboutLink.addEventListener("mouseleave", () =>
      toggleDropdown("aboutLink", false)
    );
  } else {
    console.error("Element with ID 'aboutLink' not found");
  }

  // Join dropdown
  const joinLink = document.getElementById("joinLink");
  if (joinLink) {
    joinLink.addEventListener("mouseenter", () =>
      toggleDropdown("joinLink", true)
    );
    joinLink.addEventListener("mouseleave", () =>
      toggleDropdown("joinLink", false)
    );
  } else {
    console.error("Element with ID 'joinLink' not found");
  }

  // Contact dropdown
  const contactLink = document.getElementById("contactLink");
  if (contactLink) {
    contactLink.addEventListener("mouseenter", () =>
      toggleDropdown("contactLink", true)
    );
    contactLink.addEventListener("mouseleave", () =>
      toggleDropdown("contactLink", false)
    );
  } else {
    console.error("Element with ID 'contactLink' not found");
  }
});
