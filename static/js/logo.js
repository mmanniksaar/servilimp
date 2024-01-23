document.addEventListener("DOMContentLoaded", function () {
    const logo = document.getElementById("animated-logo");

    function calculateStartPosition() {
        const screenWidth = window.innerWidth;
        console.log(screenWidth);
        const logoWidth = logo.offsetWidth;
        const startPosition = screenWidth + (logoWidth + 5 / 100 * screenWidth); // Muutus siin
        return startPosition;
    }

    gsap.to(logo, {
        duration: 2,
        x: -calculateStartPosition(),
        rotation: 360,
        ease: "power1.inOut",
        onComplete: function () {
            console.log("Liikumine ja pöörlemine on lõppenud");
        }
    });

    function rotateLogo() {
        gsap.to(logo, { rotation: "+=360", ease: "power1.inOut" });
    }

    function stopRotation() {
        gsap.to(logo, { rotation: 0, ease: "power1.inOut" });
    }

    logo.addEventListener("mouseover", rotateLogo);
    logo.addEventListener("mouseout", stopRotation);

    window.addEventListener("resize", function () {
        gsap.to(logo, { x: -calculateStartPosition() });
    });
});
