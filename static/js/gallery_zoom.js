$(document).ready(function() {
    
    var modal = document.getElementById("myModal");
    var modalImg = document.getElementById("img01");
    var captionText = document.getElementById("caption");

    $('.card__img').click(function() {
        modal.style.display = "block";
        modalImg.src = $(this).attr('src');
        captionText.innerHTML = $(this).attr('alt');
    });

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal || event.target == modalImg) {
        modal.style.display = "none";
    }
}
});

