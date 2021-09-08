import math


def find_closest_point(x1, y1, x2, y2):
    distance1 = (x1 ** 2 + y1 ** 2) ** 0.5
    distance2 = (x2 ** 2 + y2 ** 2) ** 0.5
    if distance1 <= distance2:
        return f'({math.floor(x1)}, {math.floor(y1)})'
    else:
        return f'({math.floor(x2)}, {math.floor(y2)})'


X1 = float(input())
Y1 = float(input())
X2 = float(input())
Y2 = float(input())

print(find_closest_point(X1, Y1, X2, Y2))
