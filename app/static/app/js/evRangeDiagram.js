// Дані для гістограми
    const electricRangeData = {
        labels: ['2010', '2012', '2014', '2016', '2018', '2020', '2022', '2024'], // Роки
        datasets: [{
            label: 'Дальність поїздки (км)',
            data: [120, 150, 180, 200, 250, 300, 350, 400], // Приклад даних
            backgroundColor: 'rgba(75, 192, 192, 0.7)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    };

    // Налаштування гістограми
    const electricRangeConfig = {
        type: 'bar',
        data: electricRangeData,
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true,
                    position: 'top'
                },
                tooltip: {
                    callbacks: {
                        label: function (tooltipItem) {
                            return tooltipItem.raw + ' км';
                        }
                    }
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Роки'
                    }
                },
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Дальність поїздки (км)'
                    }
                }
            }
        }
    };

    // Рендер гістограми
    const ctx5 = document.getElementById('electricRangeChart').getContext('2d');
    new Chart(ctx5, electricRangeConfig);