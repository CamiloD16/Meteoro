// let dataReload = document.getElementsByName("[data-reload]");
let language = {
    en: {
        descubre: "Discover the different types of weather in the city of your choice",
        inicio: "Home"
    },
    es: {
        descubre: "Descubre los diversos tipos de clima en la ciudad que elijas",
        inicio: "Inicio"
    }
}

if (window.location.hash) {
    if (window.location.hash === "#en") {
        descubre.textContent = language.en.descubre
        inicio.textContent = language.en.inicio
    }
}

for (i = 0; i <= $('.data-reload').length; i++) {
    $('.data-reload').click(function () {
        setTimeout(function () {
            location.reload();
        }, 100);
    })
}