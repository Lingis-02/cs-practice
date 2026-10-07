def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    return "ZeroDivisionError"

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {substract(num1, num2)}")
print(f"{num1} * {num2} = {multiply(num1, num2)}")
