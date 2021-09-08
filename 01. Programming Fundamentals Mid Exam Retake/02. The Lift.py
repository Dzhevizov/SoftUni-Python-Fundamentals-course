count_people = int(input())
lift = [int(x) for x in input().split()]
wagon_capacity = 4

for i in range(len(lift)):
    if lift[i] < wagon_capacity:
        take_lift = wagon_capacity - lift[i]
        if take_lift <= count_people:
            count_people -= take_lift
            lift[i] = wagon_capacity
        else:
            lift[i] += count_people
            count_people = 0
    if not count_people:
        break

if sum(lift) < wagon_capacity * len(lift):
    lift = [str(x) for x in lift]
    print(f"The lift has empty spots!\n{' '.join(lift)}")
else:
    lift = [str(x) for x in lift]
    if count_people > 0:
        print(f"There isn't enough space! {count_people} people in a queue!\n{' '.join(lift)}")
    else:
        print(f"{' '.join(lift)}")

