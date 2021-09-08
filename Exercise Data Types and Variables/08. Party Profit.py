import math
party_size = int(input())
days = int(input())

profit = 0

for curr_day in range(1, days+1):
    if not curr_day % 10:
        party_size -= 2
    if not curr_day % 15:
        party_size += 5
    profit += 50 - 2 * party_size
    if not curr_day % 3:
        profit -= 3 * party_size
    if not curr_day % 5:
        profit += 20 * party_size
        if not curr_day % 3:
            profit -= 2 * party_size

print(f"{party_size} companions received {math.floor(profit / party_size)} coins each.")