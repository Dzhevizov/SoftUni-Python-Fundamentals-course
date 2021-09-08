num_of_rows = int(input())
row = []
battlefield = []
destroyed_ships = 0

for i in range(num_of_rows):
    row = [int(x) for x in input().split()]
    battlefield.extend(row)

attack_list = input().split()

for i in range(len(attack_list)):
    attack = attack_list[i].split("-")
    r = int(attack[0])
    c = int(attack[1])

    field = r * len(row) + c
    if battlefield[field]:
        battlefield[field] -= 1
        if not battlefield[field]:
            destroyed_ships += 1

print(destroyed_ships)
