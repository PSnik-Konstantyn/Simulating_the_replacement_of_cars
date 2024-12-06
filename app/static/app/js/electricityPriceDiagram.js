// Дані для графіка
    const electricityPriceData = {
        labels: ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень'],
        datasets: [
            {
                label: 'Ціна за 1 кВт на публічній зарядній станції (грн)',
                data: [12.0, 12.3, 12.7, 13.2, 13.8, 14.1, 14.6, 15.0, 15.3, 15.8, 16.2, 16.9],
                borderColor: 'rgb(84,177,76)',
                backgroundColor: 'rgba(115,255,103,0.2)',
                fill: true,
                tension: 0.4
            },
            {
                label: 'Ціна за 1 кВт домашній зарядній станції (грн)',
                data: [4.32, 4.32, 4.32, 4.32, 4.32, 4.32, 4.32, 4.32, 4.32, 4.32, 4.32, 4.32],
                borderColor: 'rgb(39,100,237)',
                backgroundColor: 'rgba(79,125,209,0.2)',
                fill: true,
                tension: 0.4
            }
        ]
    };

    // Налаштування графіка
    const config1 = {
        type: 'line',
        data: electricityPriceData,
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function (tooltipItem) {
                            return tooltipItem.raw + ' грн';
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: false,
                    ticks: {
                        stepSize: 2
                    }
                }
            }
        }
    };

    // Створення графіка
    const ctx1 = document.getElementById('electricityPriceChart').getContext('2d');
    new Chart(ctx1, config1);