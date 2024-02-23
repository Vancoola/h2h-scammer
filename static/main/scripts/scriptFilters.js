const sliderEl = document.querySelector("#range2")
const sliderValue = document.querySelector(".value2")

sliderEl.addEventListener("input", (event) => {
    const tempSliderValue = event.target.value;
    sliderValue.textContent = tempSliderValue;

    const progress = (tempSliderValue / sliderEl.max) * 100;

    sliderEl.style.background = `linear-gradient(to right, #30B28C ${progress}%, #ccc ${progress}%)`;
})


const sliderEl2 = document.querySelector("#range3")
const sliderValue2 = document.querySelector(".value3")

sliderEl2.addEventListener("input", (event) => {
    const tempSliderValue = event.target.value;
    sliderValue2.textContent = tempSliderValue;

    const progress = (tempSliderValue / sliderEl.max) * 100;

    sliderEl2.style.background = `linear-gradient(to right, #30B28C ${progress}%, #ccc ${progress}%)`;
})


let btnFilter = document.querySelector('.filter-btn')
let modalFilter = document.querySelector('.modal-filter')
let closeFilter = document.querySelector('.close-filters')


btnFilter.addEventListener('click', function (){
    modalFilter.style.display = 'flex'
})


closeFilter.addEventListener('click', function (){
    modalFilter.style.display = 'none'
})

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function(e) {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        }
    });
}