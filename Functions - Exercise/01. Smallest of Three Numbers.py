def find_smallest_num(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(find_smallest_num(num1, num2, num3))
