def find_sign(num1, num2, num3):
    numbers = [num1, num2, num3]
    count_neg = 0
    for el in numbers:
        if el < 0:
            count_neg += 1
        elif el == 0:
            return 'zero'
    if count_neg % 2:
        return 'negative'
    else:
        return 'positive'


number1 = int(input())
number2 = int(input())
number3 = int(input())
print(find_sign(number1, number2, number3))

