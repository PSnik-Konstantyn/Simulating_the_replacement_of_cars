// Дані для гістограми
    const dvzRangeData = {
        labels: ['2010', '2012', '2014', '2016', '2018', '2020', '2022', '2024'], // Роки
        datasets: [{
            label: 'Дальність поїздки (км)',
            data: [500, 520, 530, 550, 560, 580, 600, 620], // Приклад даних
            backgroundColor: 'rgba(207,60,41,0.83)',
            borderColor: 'rgba(200,46,19,0.68)',
            borderWidth: 1
        }]
    };

    // Налаштування гістограми
    const dvzRangeConfig = {
        type: 'bar',
        data: dvzRangeData,
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
    const ctx2 = document.getElementById('dvzRangeChart').getContext('2d');
    new Chart(ctx2, dvzRangeConfig);