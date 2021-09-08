targets = [int(x) for x in input().split()]

target_counter = 0

shot_target = input()

while not shot_target == "End":

    shot_target = int(shot_target)

    if shot_target in range(len(targets)):
        if not targets[shot_target] == -1:
            temp = targets[shot_target]
            targets[shot_target] = -1
            target_counter += 1

            for i in range(len(targets)):
                if targets[i] > temp:
                    targets[i] -= temp
                elif -1 < targets[i] <= temp:
                    targets[i] += temp

    shot_target = input()

targets = [str(x) for x in targets]
print(f'Shot targets: {target_counter} -> {" ".join(targets)}')
