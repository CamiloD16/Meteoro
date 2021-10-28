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

//GRAFICA 2//
var ctx2 = document.getElementById('myChart2').getContext('2d');
const data2 = {
    labels: ['Temperatura', 'Temperatura máxima', 'Sensación Térmica', 'Temperatura mínima', ],
    datasets: [{
        label: 'Temperatura hoy',
        data: [28, 27, 28, 28],
        fill: true,
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgb(255, 99, 132)',
        pointBackgroundColor: 'rgb(255, 99, 132)',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: 'rgb(255, 99, 132)'
    }, {
        label: 'Temperatura mañana',
        data: [26, 29, 30, 27],
        fill: true,
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgb(54, 162, 235)',
        pointBackgroundColor: 'rgb(54, 162, 235)',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: 'rgb(54, 162, 235)'
    }, {
        label: 'Temperatura pasado mañana',
        data: [27, 28, 29, 30],
        fill: true,
        backgroundColor: 'rgb(65, 231, 36,0.2)',
        borderColor: 'rgb(65, 231, 36)',
        pointBackgroundColor: 'rgb(65, 231, 36)',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: 'rgb(65, 231, 36)',
    }],
}

var myChart2 = new Chart(ctx2, {
    type: 'radar',
    data: data2,
    options: {
        elements: {
            line: {
                borderWidth: 3
            }
        }
    },
});