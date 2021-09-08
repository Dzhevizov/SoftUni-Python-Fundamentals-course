import math


def find_length_of_line(x1, y1, x2, y2):
    length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return length


def find_closest_point_to_zero(x1, y1, x2, y2):
    distance1 = (x1 ** 2 + y1 ** 2) ** 0.5
    distance2 = (x2 ** 2 + y2 ** 2) ** 0.5
    if distance1 <= distance2:
        return f'({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})'
    else:
        return f'({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})'


firstX = float(input())
firstY = float(input())
secondX = float(input())
secondY = float(input())
thirdX = float(input())
thirdY = float(input())
fourthX = float(input())
fourthY = float(input())

line1 = find_length_of_line(firstX, firstY, secondX, secondY)
line2 = find_length_of_line(thirdX, thirdY, fourthX, fourthY)

if line1 >= line2:
    print(find_closest_point_to_zero(firstX, firstY, secondX, secondY))
else:
    print(find_closest_point_to_zero(thirdX, thirdY, fourthX, fourthY))
