import random


def guess_the_number():
    """Игра 'Угадай число': компьютер загадывает число от 1 до 100."""
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    print("=" * 45)
    print("        ИГРА «УГАДАЙ ЧИСЛО»")
    print("=" * 45)
    print("Я загадал число от 1 до 100.")
    print(f"У вас есть {max_attempts} попыток, чтобы его угадать!")

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nПопытка {attempts + 1}/{max_attempts}. "
                              f"Введите число: "))
        except ValueError:
            print("Ошибка: нужно ввести целое число. Попробуйте снова.")
            continue

        attempts += 1

        # Проверка предположения пользователя
        if guess == secret_number:
            print(f"\nПоздравляю! Вы угадали число {secret_number} "
                  f"за {attempts} попыток!")
            break
        elif guess < secret_number:
            print("Загаданное число БОЛЬШЕ.")
        else:
            print("Загаданное число МЕНЬШЕ.")

        print(f"Осталось попыток: {max_attempts - attempts}")
    else:
        # Выполняется, если попытки закончились, а число не угадано
        print(f"\nПопытки закончились! "
              f"Было загадано число: {secret_number}")


if __name__ == "__main__":
    guess_the_number()