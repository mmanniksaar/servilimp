/* document.addEventListener("DOMContentLoaded", function () {
    const logo = document.getElementById("animated-logo");

    function calculateStartPosition() {
        const screenWidth = window.innerWidth;
        const logoWidth = logo.offsetWidth;
        const startPosition = screenWidth + (logoWidth + 5 / 100 * screenWidth); // Muutus siin
        console.log(startPosition);

        return startPosition;
    } */

/*     gsap.to(logo, {
        duration: 2,
        x: -calculateStartPosition(),
        rotation: 360,
        ease: "power1.inOut",
        onComplete: function () {
        }
    }); */

/*     function rotateLogo() {
        gsap.to(logo, { rotation: "+=360", ease: "power1.inOut" });
    } */

/*     function stopRotation() {
        gsap.to(logo, { rotation: 0, ease: "power1.inOut" });
    }

    logo.addEventListener("mouseover", rotateLogo);
    logo.addEventListener("mouseout", stopRotation);

    window.addEventListener("resize", function () {
        console.log(calculateStartPosition()); 
        gsap.to(logo, { x: -calculateStartPosition() });
    }); 
});*/
