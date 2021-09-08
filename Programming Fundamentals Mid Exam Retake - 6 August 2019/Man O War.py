pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
max_health = int(input())

command_data = input()

while not command_data == "Retire":

    command_list = command_data.split()

    command = command_list[0]

    if command == "Fire":
        index = int(command_list[1])
        damage = int(command_list[2])

        if index in range(len(warship)):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit(0)

    elif command == "Defend":
        start_index = int(command_list[1])
        end_index = int(command_list[2])
        damage = int(command_list[3])

        if start_index in range(len(pirate_ship)) and end_index in range(len(pirate_ship)):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit(0)

    elif command == "Repair":
        index = int(command_list[1])
        health = int(command_list[2])

        if index in range(len(pirate_ship)):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health:
                pirate_ship[index] = max_health

    elif command == "Status":
        count = 0
        for el in pirate_ship:
            if el < max_health * 0.2:
                count += 1
        print(f"{count} sections need repair.")

    command_data = input()

print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(warship)}")
