document.addEventListener("DOMContentLoaded", function () {
    const logo = document.getElementById("animated-logo");

    gsap.to(logo, {
        duration: 2,
        x: -1600,
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




