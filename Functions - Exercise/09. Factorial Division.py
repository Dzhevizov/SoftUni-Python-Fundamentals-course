def factorial_calc(number):
    factorial = 1
    for i in range(number, 0, -1):
        factorial *= i
    return factorial


def factorial_divider(number1, number2):
    num1_factorial = factorial_calc(number1)
    num2_factorial = factorial_calc(number2)
    result = num1_factorial / num2_factorial
    print(f'{result:.2f}')


num1 = int(input())
num2 = int(input())
factorial_divider(num1, num2)


