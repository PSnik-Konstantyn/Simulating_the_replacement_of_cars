function visualizeCars(data) {
    const container = document.getElementById('visualization');
    container.innerHTML = ''; // Очищаємо попередній вміст

    console.log('Received data:', data); // Лог для перевірки структури

    const resultData = data[0][1]; // Отримуємо вкладені дані з "result"

    // Ітеруємо кожен рік і його значення
    Object.entries(resultData).forEach(([year, values]) => {
        console.log(`Year: ${year}, Values:`, values);

        // Перевіряємо, чи values — це масив
        if (!Array.isArray(values) || values.length !== 2) {
            console.error(`Invalid data for year ${year}:`, values);
            return; // Пропускаємо некоректні дані
        }

        const [dvzPercent, electricPercent] = values; // Витягуємо частки ДВЗ та електромобілів

        const totalCars = 20; // Загальна кількість іконок для кожного року
        const dvzCars = Math.round((dvzPercent / 100) * totalCars);
        const electricCars = totalCars - dvzCars;

        const yearContainer = document.createElement('div');
        yearContainer.classList.add('year');

        const yearTitle = document.createElement('h6');
        yearTitle.textContent = `Рік ${year} - відношення машин з дзв до електромобілів: ${dvzPercent} : ${electricPercent}`;
        yearContainer.appendChild(yearTitle);

        const carsContainer = document.createElement('div');
        carsContainer.classList.add('cars');

        // Генерація іконок для ДВЗ
        for (let i = 0; i < dvzCars; i++) {
            const car = document.createElement('div');
            car.classList.add('car');
            carsContainer.appendChild(car);
        }

        // Генерація іконок для електромобілів
        for (let i = 0; i < electricCars; i++) {
            const car = document.createElement('div');
            car.classList.add('car', 'electric');
            carsContainer.appendChild(car);
        }

        carsContainer.appendChild(yearContainer)
        // yearContainer.appendChild(carsContainer);
        // container.appendChild(yearContainer);
        container.appendChild(carsContainer);
    });
}
