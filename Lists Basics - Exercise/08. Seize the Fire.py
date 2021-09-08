fire_cells_list = input().split("#")
amount_of_water = int(input())

total_effort = 0
total_fire = 0
print("Cells: ")

for i in range(len(fire_cells_list)):
    fire_cells_info = fire_cells_list[i].split(" = ")
    type_of_fire = fire_cells_info[0]
    value_of_cell = int(fire_cells_info[1])
    if type_of_fire == "High" and value_of_cell in range(81, 126):
        if amount_of_water >= value_of_cell:
            amount_of_water -= value_of_cell
            total_effort += 0.25 * value_of_cell
            total_fire += value_of_cell
            print(f"- {value_of_cell}")
    if type_of_fire == "Medium" and value_of_cell in range(51, 81):
        if amount_of_water >= value_of_cell:
            amount_of_water -= value_of_cell
            total_effort += 0.25 * value_of_cell
            total_fire += value_of_cell
            print(f"- {value_of_cell}")
    if type_of_fire == "Low" and value_of_cell in range(1, 51):
        if amount_of_water >= value_of_cell:
            amount_of_water -= value_of_cell
            total_effort += 0.25 * value_of_cell
            total_fire += value_of_cell
            print(f"- {value_of_cell}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
