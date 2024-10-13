import random

def get_user_choice():
    choice = input("Введите ваш выбор (камень, ножницы, бумага): ").lower()
    while choice not in ["камень", "ножницы", "бумага"]:
        print("Некорректный выбор. Пожалуйста, выберите камень, ножницы или бумагу.")
        choice = input("Введите ваш выбор: ").lower()
    return choice

def get_computer_choice():
    return random.choice(["камень", "ножницы", "бумага"])

def display_choice(choice):
    if choice == "камень":
        print("Выбор: \n"
              "    _______  \n"
              "---'   ____) \n"
              "      (__/___) \n"
              "      (__/___) \n"
              "      (__/__)  \n"
              "---.__(_/__)   \n"
              "камень\n")
    elif choice == "ножницы":
        print("Выбор: \n"
              "       _______  \n"
              "---'   _______) \n"
              "---'   (_______ \n"
              "      (_______)  \n"
              "   ____(__/_)  \n"
              "---'   (__/_)  \n"
              "ножницы\n")
    elif choice == "бумага":
        print("Выбор: \n"
              "    ________  \n"
              "---'   _____)__ \n"
              "      (________) \n"
              "      (________) \n"
              "      (________) \n"
              "---.__(________)   \n"
              "бумага\n")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        return "Вы выиграли!"
    else:
        return "Компьютер выиграл!"

def main():
    print("Добро пожаловать в игру «камень-ножницы-бумага»!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"Ваш выбор:")
    display_choice(user_choice)
    
    print(f"Выбор компьютера:")
    display_choice(computer_choice)
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
