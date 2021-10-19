var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
        datasets: [{
            label: 'Semana actual',
            data: [36, 28, 31, 20, 25, 13, 20],
            backgroundColor: [
                'rgba(0, 99, 132, 0.6)',
                'rgba(30, 99, 132, 0.6)',
                'rgba(60, 99, 132, 0.6)',
                'rgba(90, 99, 132, 0.6)',
                'rgba(120, 99, 132, 0.6)',
                'rgba(150, 99, 132, 0.6)',
                'rgba(180, 99, 132, 0.6)'
            ],
            borderWidth: 3,
            hoverBorderWidth: 0,
            borderColor: 'rgba(0, 255, 132, 0.6)',
        }, {
            label: 'Semana pasada',
            data: [12, 24, 20, 11, 23, 52, 32],
            backgroundColor: [
                'rgba(180, 99, 132, 0.6)',
                'rgba(150, 99, 132, 0.6)',
                'rgba(120, 99, 132, 0.6)',
                'rgba(90, 99, 132, 0.6)',
                'rgba(60, 99, 132, 0.6)',
                'rgba(30, 99, 132, 0.6)',
                'rgba(0, 99, 132, 0.6)'    
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
        // legend: {
        //     display: true,
        //     position: 'top',
        //     labels: {
        //         boxWidth: 80,
        //         fontColor: 'black'
        //     }
        // }
    }
});