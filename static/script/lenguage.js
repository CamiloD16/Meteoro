let language = {
    en: {
        descubre: "Discover the different types of weather in the city of your choice",
        inicio: "Home" , 
        proyecto: "Draft" , 
        contactanos: "Contact Us" ,
        conocambi: "Know the climate changes that are coming!" , 
        Busca: "Search" ,
        contaminacion: "Air pollution",
        monocar: "Carbon monoxide(CO)",
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
        mana:"Tomorrow",
        pasmana:"Day after tomorrow", 
        navbarDropdown: "Languages",
       
        

    },
    es: {
        descubre: "Descubre los diversos tipos de clima en la ciudad que elijas",
        inicio: "Inicio" , 
        proyecto: "Proyecto" , 
        contactanos: "Contáctanos" ,
        conocambi: "Conoce los cambios climáticos que se aproximan!" , 
        Busca: "Buscar" ,
        contaminacion: "Contaminación del aire",
        monocar: "Monóxido de carbono",
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
        mana:"Mañana",
        sensatermica:"La sensación térmica actual es de", 
        humedad:"Humedad:",
        pasmana:"Pasado mañana", 
        navbarDropdown: "Idiomas",
        
    }
}

if (window.location.hash) {
    if (window.location.hash === "#en") {
        descubre.textContent = language.en.descubre
        inicio.textContent = language.en.inicio
        proyecto.textContent = language.en.proyecto
        contactanos.textContent = language.en.contactanos
        conocambi.textContent = language.en.conocambi
        Busca.textContent = language.en.Busca
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
        pasmana.textContent = language.en.pasmana
        mana.textContent = language.en.mana
        navbarDropdown.textContent=language.en.navbarDropdown
    }
}

for (i = 0; i <= $('.data-reload').length; i++) {
    $('.data-reload').click(function () {
        setTimeout(function () {
            location.reload();
        }, 100);
    })
}