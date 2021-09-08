capacity = 255
num_of_lines = int(input())
poured_water = 0

for i in range(num_of_lines):
    liters_of_water = int(input())
    if liters_of_water + poured_water > capacity:
        print("Insufficient capacity!")
    else:
        poured_water += liters_of_water

print(poured_water)