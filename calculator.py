
from os import system


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def modulus(x, y):
    return x % y


def exponent(x, y):
    return x ** y


def floor_divide(x, y):
    return x // y


system("cls")

print(
    """
    Калькулятор

    Выберите действие:
    [1] Прибавление
    [2] Отнимание
    [3] Умножение
    [4] Деление
    [5] Остаток от деления
    [6] Возведение в степень
    [7] Целочисленное деление
    
    """
)


def main():
    while True:
        choice = input("Введите действие (1 / 2 / 3 / 4 / 5 / 6 / 7): ")

        if choice in ("1", "2", "3", "4", "5", "6", "7"):
            try:
                num1 = float(input("Введите первое число: "))
            except ValueError:
                print("Введенное значение должно быть числом либо дробью")
                break
            try:
                num2 = float(input("Введите второе число: "))
            except ValueError:
                print("Введенное значение должно быть числом либо дробью")
                break

            if choice == "1":
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == "2":
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == "3":
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == "4":
                print(num1, "/", num2, "=", divide(num1, num2))

            elif choice == "5":
                print(num1, "%", num2, "=", modulus(num1, num2))

            elif choice == "6":
                print(num1, "^", num2, "=", exponent(num1, num2))

            elif choice == "7":
                print(num1, "//", num2, "=", floor_divide(num1, num2))

            next_calculation = input("Продолжить? (да/нет): ")
            if next_calculation == "нет":
                break

        else:
            raise ValueError("Введено неправильное значение")


if __name__ == "__main__":
    main()
