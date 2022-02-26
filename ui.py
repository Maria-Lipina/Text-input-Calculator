import controller

def get_value():
    return input()

def hello():
    print("Добро пожаловать!")

def menu():
    print("Выберите действие:\n1 - посмотреть инструкцию.\n2 - начать работу.\n3 - посмотреть историю операций")
    return input()

def instruct():
    print("""Инструкция:
Выражение задается следующим образом: 1. Первое число 2. Операция 3. Второе число

Калькулятор поддерживает работу со всеми видами чисел. Числа вводятся в калькулятор следующим образом:
Целые: -8 или 8
Обыкновенные дроби: 8/3
Десятичные дроби или вещественные числа: 8.1 или 8e1, 1., .1, 0.1, 1e+1, 1.e-3, 1.0e0
Комплексные числа: 8+3j или 8-3j

Калькулятор поддерживает четыре операции, которые так же вводятся пользователем:
Сложение: +
Вычитание: -
Умножение: *
Деление: /

При загрузке истории последние десять операций с числами выводятся на экран.
""")

# 
# Продолжение инструкции: необязательные сложности, но как же надо для нормального использования калькулятора:
# Чтобы вернуться в главное меню после вычислений, просмотра истории или инструкции введите menu
# Чтобы выйти из калькулятора на любом этапе работы, введите exit
# 

def show_result(x, op, y, res):
    record = f'{x} {op} {y} = {res} - это ui'
    print(record)
    return record