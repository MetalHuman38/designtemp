// script.js

// Function to toggle the entire navbar on mobile
function toggleNavbar() {
  const navbar = document.getElementById("navbar");
  const hamburgerIcon =
    document.getElementById("hamburger-icon").firstElementChild;

  if (navbar) {
    navbar.classList.toggle("hidden");

    // Toggle the icon based on the navbar visibility
    if (navbar.classList.contains("hidden")) {
      hamburgerIcon.classList.remove("fa-x");
      hamburgerIcon.classList.add("fa-bars");
    } else {
      hamburgerIcon.classList.remove("fa-bars");
      hamburgerIcon.classList.add("fa-x");
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
