let hamburger_button = document.querySelector(".hamburger-button");

hamburger_button.addEventListener('click', () => {
    let navAnchorElements = document.querySelectorAll("nav > a");

    navAnchorElements.forEach((navAnchor) => {
        if (!navAnchor.style.display) {
            navAnchor.style.display = "block";
        }
        else if (navAnchor.style.display == "none") {
            navAnchor.style.display = "block";
        } else {
            navAnchor.style.display = "none";
        }
    });
})