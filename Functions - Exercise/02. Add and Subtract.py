def sum_numbers(a, b):
    return a + b


def subtract(a, b):
    return a - b


def add_and_subtract(a, b, c):
    return a + b - c


num1 = int(input())
num2 = int(input())
num3 = int(input())
rez = sum_numbers(num1, num2)
print(subtract(rez, num3))
add_and_subtract(num1, num2, num3)
