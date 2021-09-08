initial_health = 100
bitcoins = 0

dungeon_rooms = input().split("|")
room_counter = 0
curr_health = initial_health


def healing(amount, health):

    if amount + health <= initial_health:
        health += amount
    else:
        amount = initial_health - health
        health = initial_health

    print(f'You healed for {amount} hp.')
    print(f'Current health: {health} hp.')

    return health


def find_bitcoins(amount, bitcoin):

    bitcoin += amount
    print(f'You found {amount} bitcoins.')

    return bitcoin


def monster_fight(monster, amount, health, stage):

    health -= amount

    if health > 0:
        print(f'You slayed {monster}.')
    else:
        print(f'You died! Killed by {monster}.')
        print(f'Best room: {stage}')

    return health


for room in dungeon_rooms:

    room_counter += 1
    command, number = room.split()
    number = int(number)

    if command == "potion":
        curr_health = healing(number, curr_health)
    elif command == "chest":
        bitcoins = find_bitcoins(number, bitcoins)
    else:
        curr_health = monster_fight(command, number, curr_health, room_counter)
        if curr_health <= 0:
            break

if curr_health > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f'Health: {curr_health}')

