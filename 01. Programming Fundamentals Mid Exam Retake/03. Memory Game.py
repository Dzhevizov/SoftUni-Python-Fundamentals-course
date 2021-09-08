sequence = input().split()

move = input()
move_counter = 0
is_winner = False

while not move == "end":

    move_counter += 1
    move_indexes = move.split()
    index1 = int(move_indexes[0])
    index2 = int(move_indexes[1])

    if index1 not in range(len(sequence)) or index2 not in range(len(sequence)) or index1 == index2:
        sequence.insert((len(sequence) // 2), f"-{move_counter}a")
        sequence.insert((len(sequence) // 2), f"-{move_counter}a")
        print("Invalid input! Adding additional elements to the board")

    elif sequence[index1] == sequence[index2]:
        print(f"Congrats! You have found matching elements - {sequence[index1]}!")
        sequence.pop(index1)
        if index1 < index2:
            sequence.pop(index2-1)
        else:
            sequence.pop(index2)

    elif not sequence[index1] == sequence[index2]:
        print("Try again!")

    if len(sequence) == 0:
        print(f"You have won in {move_counter} turns!")
        is_winner = True
        break

    move = input()

if not is_winner:
    print(f"Sorry you lose :(\n{' '.join(sequence)}")
