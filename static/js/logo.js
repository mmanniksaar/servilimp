/*document.addEventListener("DOMContentLoaded", function () {
    const logo = document.getElementById("animated-logo");

    gsap.to(logo, {
        duration: 2,
        x: "-500%",
        rotation: 360, // Lisa pöörlemine liikumise animatsiooni sisse
        ease: "power1.inOut",
        onComplete: function () {
            // Funktsioon, mis käivitatakse liikumise ja pöörlemise lõppedes
            console.log("Liikumine ja pöörlemine on lõppenud");
        }
    });

    // Pöörlemise funktsioon
    function rotateLogo() {
        gsap.to(logo, { rotation: "+=360", ease: "power1.inOut" });
    }

    // Pöörlemise peatamise funktsioon
    function stopRotation() {
        gsap.to(logo, { rotation: 0, ease: "power1.inOut" });
    }

    // Logo pöörlemise sündmustiku kuulajad
    logo.addEventListener("mouseover", rotateLogo);
    logo.addEventListener("mouseout", stopRotation);

    gsap.to(".choice-container", { 
        duration: 3, // Animatsiooni kestus sekundites
        y: "-50%",   // Y-telg (vertikaalne) muutus
        ease: "power2.out" // Animatsiooni lihtsustamise funktsioon
    
    });
});
*/

document.addEventListener("DOMContentLoaded",
    function () {
        const logo = document.getElementById("animated-logo");

    // Funktsioon, mis arvutab animatsiooni alguspunkti sõltuvalt ekraani laiusest
    function calculateStartPosition() {
        const screenWidth = window.innerWidth;
        console.log("screenWidth: ",screenWidth);
        const logoWidth = logo.offsetWidth;
        const startPosition = screenWidth - (screenWidth/2); // Muutus siin
        //const startPosition = screenWidth + (logoWidth + 5 / 100 * screenWidth); // Muutus siin
        console.log("logoWidth: ",logoWidth);
        console.log("startPosition: ",startPosition);
        return startPosition;
    }

    gsap.to(logo, {
        duration: 2,
        x: -calculateStartPosition(), // Muutus siin
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

    gsap.to(".logo-container", {
        duration: 3,
        y: "-50%",
        ease: "power2.out"
    });

    // Kuulake akna suuruse muutusi ja värskendage animatsiooni alguspunkti
    window.addEventListener("resize", function () {
        gsap.to(logo, { x: -calculateStartPosition() }); // Muutus siin

    });
});
