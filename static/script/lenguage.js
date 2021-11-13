// let dataReload = document.getElementsByName("[data-reload]");
let language = {
    en: {
        descubre: "Discover the different types of weather in the city of your choice",
        inicio: "Home" , 
        pronostico: "Forecast" ,
        contam: "Pollution" ,
        proyecto: "Draft" , 
        contactanos: "Contact us" ,
        conocambi: "Know the climate changes that are coming!" , 
        Busca: "Search" ,
        contaminacion: "Air pollution",
        monocar: "Carbon monoxide (CO)",
        mononitro: "Nitrogen monoxide (NO)",
        dionitro: "Nitrogen dioxide (NO2)",
        concenozo: "Ozone concentration (O3)",
        dioazu: "Sulfur dioxide (SO2)",
        mateparti: "Fine particulate matter (PM2.5)",
        partigru: "Coarse particles (PM10)",
        concenamo: "Ammonia concentration (NH3)",
        buen:"Well",
        regu:"Regular",
        mode:"Moderate",
        malo:"Bad",
        pesi:"Appalling",
        calidair:"Air quality", 
        hoyx:"Today:",
        sensatermica:"The current wind chill is",
        humedad:"Humidity:",
        pasmaña:"Day after tomorrow:", 
        temtura:"Temperature: 0°C",
        conta:"Contact us"

       
        

    },
    es: {
        descubre: "Descubre los diversos tipos de clima en la ciudad que elijas",
        inicio: "Inicio" , 
        pronostico: "Pronostico" ,
        contam: "Contaminacion", 
        proyecto: "Proyecto" , 
        contactanos: "Contáctanos" ,
        conocambi: "Conoce los cambios climáticos que se aproximan!" , 
        Busca: "Buscar" ,
        contaminacion: "Contaminación del aire",
        monocar: "Monóxido de carbono (CO)",
        mononitro: "Monóxido de nitrógeno (NO)",
        dionitro: "Dióxido de nitrógeno (NO2)",
        concenozo:"Сoncentración de ozono (O3)",
        dioazu: "Dióxido de azufre (SO2)",
        mateparti: "Materia de partículas finas (PM2.5)",
        partigru: "Partículas gruesas (PM10)",
        concenamo: "Сoncentración de amoníaco (NH3)",
        buen:"Bueno",
        regu:"Regular",
        mode:"Moderado",
        malo:"Malo",
        pesi:"Pésimo",
        calidair:"Calidad del aire",
        hoyx:"Hoy:",
        sensatermica:"La sensación térmica actual es de", 
        humedad:"Humedad:",
        pasmaña:"Pasado mañana:", 
        temtura:"Temperatura: 0°C",
        conta:"Contáctanos"
        
        
    }
}

if (window.location.hash) {
    if (window.location.hash === "#en") {
        descubre.textContent = language.en.descubre
        inicio.textContent = language.en.inicio
        pronostico.textContent = language.en.pronostico
        contam.textContent = language.en.contam
        proyecto.textContent = language.en.proyecto
        contactanos.textContent = language.en.contactanos
        conocambi.textContent = language.en.conocambi
        Busca.textContent = language.en.Busca
        maña.textContent = language.en.maña
        contaminacion.textContent = language.en.contaminacion
        monocar.textContent = language.en.monocar
        mononitro.textContent = language.en.mononitro
        dionitro.textContent = language.en.dionitro
        concenozo.textContent = language.en.concenozo
        dioazu.textContent = language.en.dioazu
        mateparti.textContent = language.en.mateparti
        partigru.textContent = language.en.partigru
        concenamo.textContent = language.en.concenamo
        buen.textContent = language.en.buen
        regu.textContent = language.en.regu
        mode.textContent = language.en.mode
        malo.textContent = language.en.malo
        pesi.textContent = language.en.pesi
        calidair.textContent = language.en.calidair
        hoyx.textContent = language.en.hoyx
        sensatermica.textContent = language.en.sensatermica
        humedad.textContent = language.en.humedad
        pasmaña.textContent = language.en.pasmaña
        temtura.textContent = language.en.temtura
        conta.textContent = language.en.conta
    
     

    
    }
}

for (i = 0; i <= $('.data-reload').length; i++) {
    $('.data-reload').click(function () {
        setTimeout(function () {
            location.reload();
        }, 100);
    })
}