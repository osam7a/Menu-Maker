document.addEventListener("DOMContentLoaded", () => {
    console.log("Scrollspy module loading..");

    const sections = document.querySelectorAll("section");
    const buttons = document.querySelectorAll("[data-target]");
    const stickyNav = document.getElementById("sticky-nav");
    let ticking = false;

    function updateScroll() {
        let current = "";
        const scrollY = window.scrollY + 150; // Adjust to account for the offset

        sections.forEach((section, index) => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const nextSectionTop =
                index < sections.length - 1
                    ? sections[index + 1].offsetTop
                    : document.body.scrollHeight;

            if (scrollY >= sectionTop && scrollY < nextSectionTop) {
                current = section.getAttribute("id");
            }
        });

        // Handle last section detection
        const lastSection = sections[sections.length - 1];
        const lastSectionBottom = lastSection.offsetTop + lastSection.offsetHeight;

        if (
            scrollY >= lastSection.offsetTop - 150 ||
            scrollY + window.innerHeight >= document.body.scrollHeight
        ) {
            current = lastSection.getAttribute("id");
        }

        // Update button styles
        buttons.forEach((button) => {
            button.classList.toggle(
                "active",
                button.getAttribute("data-target") === current
            );
            if (button.classList.contains("active")) {
                button.scrollIntoView({
                    behavior: "smooth",
                    block: "nearest",
                    inline: "center",
                });
            }
        });

        // Check if the last section is scrolled past
        stickyNav.classList.toggle(
            "scrolled-out",
            scrollY + window.innerHeight >= lastSectionBottom
        );
    }

    window.addEventListener("scroll", () => {
        if (!ticking) {
            ticking = true;
            window.requestAnimationFrame(() => {
                updateScroll();
                ticking = false;
            });
        }
    }, false);

    buttons.forEach((button) => {
        button.addEventListener("click", () => {
            const targetSection = document.getElementById(
                button.getAttribute("data-target")
            );
            const offset = window.innerHeight / 2 - 120;

            // Scroll to the section with an offset to ensure it's centered
            const targetPosition =
                targetSection.getBoundingClientRect().top + window.pageYOffset - offset;

            window.scrollTo({
                top: targetPosition,
                behavior: "smooth",
            });

            // Ensure the clicked button comes into view
            button.scrollIntoView({
                behavior: "smooth",
                block: "nearest",
                inline: "center",
            });
        });
    });

    console.log("Scrollspy module loaded.");
});
