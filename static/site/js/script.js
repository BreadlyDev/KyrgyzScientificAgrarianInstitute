const swiper = new Swiper('.swiper', {
  direction: 'horizontal',
  loop: true,

  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },

  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
});

const booksDescription = document.querySelectorAll('.library-item-description')
function shortBooksDescription() {
    for (let i = 0; i < booksDescription.length; i++) {
        if (booksDescription[i].innerText.length > 1000) {
            booksDescription[i].innerText = booksDescription[i].innerHTML.substring(0, 1000) + '...'
        }
    }
}

shortBooksDescription()

const burgerButton = document.querySelectorAll('.header-menu-item.burger-button')[0]

burgerButton.addEventListener('click', () => {
    const headerBurgerMenu = document.querySelectorAll('.header-menu.burger')[0];

    if (headerBurgerMenu.classList.contains('visually-hidden')) {
        headerBurgerMenu.classList.remove('visually-hidden');
    } else {
        headerBurgerMenu.classList.add('visually-hidden');
    }
});