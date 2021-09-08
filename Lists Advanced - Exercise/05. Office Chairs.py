num_of_rooms = int(input())
free_chairs = 0
is_enough_chairs = True

for curr_room in range(1, num_of_rooms + 1):
    needed_chairs = 0
    chairs, visitors = input().split()
    num_of_chairs = len(chairs)
    num_of_visitors = int(visitors)
    if num_of_chairs >= num_of_visitors:
        free_chairs += num_of_chairs - num_of_visitors
    else:
        needed_chairs = num_of_visitors - num_of_chairs
        print(f'{needed_chairs} more chairs needed in room {curr_room}')
        is_enough_chairs = False

if is_enough_chairs:
    print(f'Game On, {free_chairs} free chairs left')
