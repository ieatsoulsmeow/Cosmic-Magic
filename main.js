document.addEventListener("DOMContentLoaded", () => {
    const themeToggle = document.getElementById("themeToggle");
    const darkModeIcon = document.getElementById("themeToggle").firstElementChild;
    const body = document.body;

    //Loads theme
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme) {
        toggleDarkMode(body, darkModeIcon)
    }

    //Toggles theme
    themeToggle.addEventListener("click", () => {
        toggleDarkMode(body, darkModeIcon)
    });
});

function toggleDarkMode(body, darkModeIcon) {
    if (body.classList.contains("dark")) {
        body.classList.remove("dark");
        localStorage.setItem("theme", ""); //Save user preference
        darkModeIcon.src = "assets/icons/light-mode.svg";
    } else {
        body.classList.add("dark");
        localStorage.setItem("theme", "dark"); //Save user preference
        darkModeIcon.src = "assets/icons/dark-mode.svg";
    }
}