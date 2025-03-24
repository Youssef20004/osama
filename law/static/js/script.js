// Proloader
const proloader = document.querySelector("[data-proloader]");

window.addEventListener("load" , () => {
    proloader.classList.add("remove")
})
// header
const header = document.querySelector("[data-header]")

window.addEventListener("scroll" , function () {
    header.classList[window.scrollY > 100 ? "add" : "remove"]("active")
})


// navbar

const menuBtn = document.querySelector('.menu-btn');
const closeBtn = document.querySelector(".close-btn");
const navbar = document.querySelector(".navbar");


document.addEventListener('DOMContentLoaded', function() {
    const cardsContainer = document.querySelector('.sr');
    const scrollLeftBtn = document.querySelector('.scroll-left');
    const scrollRightBtn = document.querySelector('.scroll-right');
    function getCardWidth() {
        const card = cardsContainer.querySelector('.card');
        const style = window.getComputedStyle(card);
        const cardWidth = card.offsetWidth;
        const gap = parseInt(style.marginRight) || 15; // لو فيه margin أو gap
        return cardWidth + gap;
    }

    //  بعد الريلود يبدأ من الأول
    cardsContainer.scrollLeft = 0;

    scrollLeftBtn.addEventListener('click', () => {
        const scrollAmount = getCardWidth() * 1; // حرك كارتين
        cardsContainer.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
    });

    scrollRightBtn.addEventListener('click', () => {
        const scrollAmount = getCardWidth() * 1;
        cardsContainer.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    });

    //  لما تعمل ريفريش يبدأ من أول كارتين
    window.addEventListener('load', () => {
        cardsContainer.scrollLeft = 0;
    });
});

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}


menuBtn.addEventListener("click" , () => {
    navbar.classList.add("active");
});

closeBtn.addEventListener("click", () => {
    navbar.classList.remove("active");
})
