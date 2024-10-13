from datetime import datetime

# Функция для расчета возраста
def calculate_age():
    # Запрос даты рождения у пользователя
    birth_date_input = input("Введите дату рождения (дд/мм/гггг): ")
    
    try:
        # Преобразование введенной даты в объект datetime
        birth_date = datetime.strptime(birth_date_input, "%d/%m/%Y")
        today = datetime.now()  # Текущая дата
        
        # Расчет возраста
        age = today.year - birth_date.year
        
        # Проверка, был ли день рождения в этом году
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        print(f"Ваш возраст: {age} лет")
    
    except ValueError:
        print("Ошибка: введите дату в корректном формате (дд/мм/гггг).")

# Запуск функции
if __name__ == "__main__":
    calculate_age()
