document.addEventListener("DOMContentLoaded", function () {
    const lightbox = document.getElementById("lightbox");
    const lightboxImage = document.getElementById("lightboxImage");
    const closeLightbox = document.getElementById("closeLightbox");

    const cards = document.querySelectorAll(".card");

    cards.forEach(function (card) {
        card.addEventListener("click", function () {
            const imgSrc = card.querySelector("img").src;
            lightboxImage.src = imgSrc;
            lightbox.style.display = "block";
        });
    });

    closeLightbox.addEventListener("click", function () {
        lightbox.style.display = "none";
    });

    window.addEventListener("click", function (event) {
        if (event.target === lightbox) {
            lightbox.style.display = "none";
        }
    });
});

