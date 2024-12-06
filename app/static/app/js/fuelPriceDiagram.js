// Дані для графіка
    const fuelPriceData = {
        labels: ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень'],
        datasets: [
            {
                label: 'Ціна А95 за 1 літр (грн)',
                data: [52.5, 53.1, 53.8, 54.2, 54.9, 55.4, 56.0, 55.7, 56.8, 57.3, 56.9, 58.0],
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                fill: true,
                tension: 0.4
            },
            {
                label: 'Ціна Дизеля за 1 літр (грн)',
                data: [51.8, 52.5, 52.1, 53.2, 53.8, 54.1, 54.7, 54.3, 55.2, 55.8, 55.5, 56.5],
                borderColor: 'rgba(255, 99, 132, 1)',
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                fill: true,
                tension: 0.4
            }
        ]
    };

    // Налаштування графіка
    const config = {
        type: 'line',
        data: fuelPriceData,
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
    const ctx = document.getElementById('fuelPriceChart').getContext('2d');
    new Chart(ctx, config);