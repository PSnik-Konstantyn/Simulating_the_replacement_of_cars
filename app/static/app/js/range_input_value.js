// Синхронізація значення поля years із прихованим полем у формі
    const yearsField = document.getElementById('id_years');
    const valueDisplay = document.getElementById('value');

    // Додаємо обробник події для зміни значення
    yearsField.addEventListener('input', function () {
        valueDisplay.textContent = this.value; // Оновлюємо відображення значення
    });