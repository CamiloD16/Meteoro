// var xmlhttp = new XMLHttpRequest();
// var url = "http://api.openweathermap.org/data/2.5/forecast?q=bogota&appid=f62b4de10d24119e0ef2a24f0cea1158";
// xmlhttp.open("GET", url, true);
// xmlhttp.send();
// xmlhttp.onreadystatechange = function(){
//     if(this.readyState == 4 && this.status==200){
//         var data= JSON.parse(this.responseText);
//         console.log(data)
//     }
// }

//GRAFICA 1//
var ctx1 = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx1, {
    type: 'bar',
    data: {
        labels: ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
        datasets: [{
            label: 'Semana actual',
            data: [32, 28, 31, 15, 24, 16, 27],
            backgroundColor: [
                'rgba(30, 99, 132, 0.6)',
                'rgba(30, 99, 132, 0.6)',
                'rgba(30, 99, 132, 0.6)',
                'rgba(30, 99, 132, 0.6)',
                'rgba(30, 99, 132, 0.6)',
                'rgba(30, 99, 132, 0.6)',
                'rgba(30, 99, 132, 0.6)'
            ],
            borderWidth: 3,
            hoverBorderWidth: 0,
            borderColor: 'rgba(0, 255, 132, 0.6)',
        }, {
            label: 'Semana pasada',
            data: [27, 23, 22, 13, 24, 10, 19],
            backgroundColor: [
                'rgba(150, 99, 132, 0.6)',
                'rgba(150, 99, 132, 0.6)',
                'rgba(150, 99, 132, 0.6)',
                'rgba(150, 99, 132, 0.6)',
                'rgba(150, 99, 132, 0.6)',
                'rgba(150, 99, 132, 0.6)',
                'rgba(150, 99, 132, 0.6)'
            ],
            borderWidth: 3,
            hoverBorderWidth: 0,
            borderColor: 'rgba(180, 255, 132, 0.6)',
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
            },
            xAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'aaaaaxx'
                }
            }]

        },

        responsive: true,
    }
});