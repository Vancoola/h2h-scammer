$(window).scroll(function() {
    var height = $(window).scrollTop();
    /*Если сделали скролл на 100px задаём новый класс для header*/
    if(height > 10){
        $('header').addClass('header-fixed');
    } else{
        /*Если меньше 100px удаляем класс для header*/
        $('header').removeClass('header-fixed');
    }
});


window.addEventListener("DOMContentLoaded", function() {
    [].forEach.call( document.querySelectorAll('.telInput'), function(input) {
        var keyCode;
        function mask(event) {
            event.keyCode && (keyCode = event.keyCode);
            var pos = this.selectionStart;
            if (pos < 3) event.preventDefault();
            var matrix = "+7 (___) ___-__-__",
                i = 0,
                def = matrix.replace(/\D/g, ""),
                val = this.value.replace(/\D/g, ""),
                new_value = matrix.replace(/[_\d]/g, function(a) {
                    return i < val.length ? val.charAt(i++) || def.charAt(i) : a
                });
            i = new_value.indexOf("_");
            if (i != -1) {
                i < 5 && (i = 3);
                new_value = new_value.slice(0, i)
            }
            var reg = matrix.substr(0, this.value.length).replace(/_+/g,
                function(a) {
                    return "\\d{1," + a.length + "}"
                }).replace(/[+()]/g, "\\$&");
            reg = new RegExp("^" + reg + "$");
            if (!reg.test(this.value) || this.value.length < 5 || keyCode > 47 && keyCode < 58) this.value = new_value;
            if (event.type == "blur" && this.value.length < 5)  this.value = ""
        }

        input.addEventListener("input", mask, false);
        input.addEventListener("focus", mask, false);
        input.addEventListener("blur", mask, false);
        input.addEventListener("keydown", mask, false)

    });

});
AOS.init();


var swiper = new Swiper(".mySwiperBanner", {
    pagination: {
        el: ".swiper-paginationBanner",
    },
    centeredSlides: true,
    autoplay: {
        delay: 10000,
        disableOnInteraction: false,
    },
});


const btnNumDonate = document.querySelectorAll('.section2-container-top-block__in-person-meeting-template1');
const tabDonate = document.querySelectorAll('.table1')

btnNumDonate.forEach(function (item){
    item.addEventListener('click', function (){
        btnNumDonate.forEach(function (i){
            i.classList.remove('section2-container-top-active__in-person-meeting-template')
        })

        item.classList.add('section2-container-top-active__in-person-meeting-template')

        let tubIDDonate = item.getAttribute('data-tab');
        let tabActiveDonate = document.querySelector(tubIDDonate);

        tabDonate.forEach(function (item){
            item.classList.remove('table-active')
        })
        tabActiveDonate.classList.add('table-active')

    })
})


const btnNumDonate2 = document.querySelectorAll('.section2-container-top-block__in-person-meeting-template2');
const tabDonate2 = document.querySelectorAll('.table2')

btnNumDonate2.forEach(function (item){
    item.addEventListener('click', function (){
        btnNumDonate2.forEach(function (i){
            i.classList.remove('section2-container-top-active__in-person-meeting-template')
        })

        item.classList.add('section2-container-top-active__in-person-meeting-template')

        let tubIDDonate = item.getAttribute('data-tab-table');
        let tabActiveDonate = document.querySelector(tubIDDonate);

        tabDonate2.forEach(function (item){
            item.classList.remove('table-active')
        })
        tabActiveDonate.classList.add('table-active')

    })
})