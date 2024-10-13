def get_number():
    for num in range(30):
        if num % 2 != 0:  # Проверка на нечетность
            yield num

# Основная логика для получения значений
def main():
    generator = get_number()
    
    # Получаем все нечетные числа из генератора
    odd_numbers = list(generator)
    
    # Проверяем, достаточно ли чисел для вывода
    if len(odd_numbers) >= 5:
        print(f"Первое нечетное число: {odd_numbers[0]}")
        print(f"Пятое нечетное число: {odd_numbers[4]}")
        print(f"Последнее нечетное число: {odd_numbers[-1]}")
    else:
        print("Недостаточно нечетных чисел в диапазоне.")

# Запуск основной функции
if __name__ == "__main__":
    main()
