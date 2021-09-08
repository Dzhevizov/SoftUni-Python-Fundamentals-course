energy = int(input())

wins_counter = 0

distance = input()

while not distance == "End of battle":

    distance = int(distance)

    if distance <= energy:
        energy -= distance
        wins_counter += 1

        if wins_counter % 3 == 0:
            energy += wins_counter

    else:
        print(f"Not enough energy! Game ends with {wins_counter} won battles and {energy} energy")
        exit(0)

    distance = input()

print(f"Won battles: {wins_counter}. Energy left: {energy}")
