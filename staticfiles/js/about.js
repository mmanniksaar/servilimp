document.addEventListener("DOMContentLoaded", function () {


const tl = gsap.timeline({
    onComplete: () => {
      // Liikumine on lõppenud, saate käivitada värvi muutmise animatsiooni
      gsap.to("#animated_first", { color: "#ccc", duration: 2 });
    },
  });
  
  tl.from("#animated_first", {
    x: "100%", // Alustab väljaspoolt paremal
    duration: 1, // Animatsiooni kestvus sekundites
    ease: "power2.out", // Animatsiooni lihtsustusfunktsioon (võib muuta vastavalt soovile)
  });
  
  const tl1 = gsap.timeline({
    onComplete: () => {
      // Liikumine on lõppenud, saate käivitada värvi muutmise animatsiooni
      gsap.to("#animated_second", { color: "#ccc", duration: 2 });
    },
  });
  
  tl1.from("#animated_second", {
    x: "-100%", // Alustab väljaspoolt paremal
    duration: 1, // Animatsiooni kestvus sekundites
    ease: "power2.out", // Animatsiooni lihtsustusfunktsioon (võib muuta vastavalt soovile)
  });
      
  const tl2 = gsap.timeline({
    onComplete: () => {
      // Liikumine on lõppenud, saate käivitada värvi muutmise animatsiooni
      gsap.to("#animated_third", { color: "#ccc", duration: 2 });
    },
  });
  
  tl2.from("#animated_third", {
    x: "100%", // Alustab väljaspoolt paremal
    duration: 1, // Animatsiooni kestvus sekundites
    ease: "power2.out", // Animatsiooni lihtsustusfunktsioon (võib muuta vastavalt soovile)
  });
});