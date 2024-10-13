import random

# Функция для поиска кратных чисел
def find_multiples_of_x():
    # Генерация списка случайных чисел от 0 до 200
    numbers = [random.randint(0, 200) for _ in range(10)]
    print("Сгенерированные числа:", numbers)
    
    # Запрос цифры X у пользователя
    while True:
        try:
            x = int(input("Введите цифру X для поиска кратных чисел: "))
            if x <= 0:
                print("Ошибка: X должно быть положительным числом.")
                continue
            break
        except ValueError:
            print("Ошибка: введите корректное целое число.")
    
    # Использование лямбда-функции для фильтрации кратных чисел
    multiples = list(filter(lambda num: num % x == 0, numbers))
    
    # Вывод найденных кратных чисел
    if multiples:
        print(f"Числа, кратные {x}: {multiples}")
    else:
        print(f"Нет чисел, кратных {x}.")

# Запуск функции
if __name__ == "__main__":
    find_multiples_of_x()
