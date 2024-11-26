$(document).ready(function() {
  var modal = document.getElementById("myModal");
  var modalImg = document.getElementById("img01");
  /* var captionText = document.getElementById("caption"); */

  $('.client-container img').click(function() {
      modal.style.display = "block";
      modalImg.src = $(this).attr('src');
      /* captionText.innerHTML = $(this).attr('alt'); */

      var clientImageSrc = $(this).data('client-image-src');
      modalImg.src = clientImageSrc;
  });

  window.onclick = function(event) {
    if (event.target == modal || event.target == modalImg) {
      modal.style.display = "none";
    }
  }
});
