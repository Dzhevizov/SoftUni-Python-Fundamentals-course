n = int(input())

for i in range(1, n + 1):
    sum1 = 0
    for symbol in str(i):
        sum1 += int(symbol)
    if sum1 == 5 or sum1 == 7 or sum1 == 11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')
