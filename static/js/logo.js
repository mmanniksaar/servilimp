document.addEventListener("DOMContentLoaded", function () {
    const logo = document.getElementById("animated-logo");

    // Funktsioon, mis arvutab animatsiooni alguspunkti sõltuvalt ekraani laiusest
    function calculateStartPosition() {
        screenWidth = 0;
        const screenWidth = window.innerWidth;
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

    gsap.to(".choice-container", { 
        duration: 3,
        y: "-50%",
        ease: "power2.out"
    });

    // Kuulake akna suuruse muutusi ja värskendage animatsiooni alguspunkti
    window.addEventListener("resize", function () {
        gsap.to(logo, { x: -calculateStartPosition() }); // Muutus siin
    });
});
