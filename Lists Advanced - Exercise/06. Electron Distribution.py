num_of_electrons = int(input())

shell_number = 1
filled_shells = []

while num_of_electrons > 0:
    max_number_of_electrons = 2 * (shell_number ** 2)
    if num_of_electrons >= max_number_of_electrons:
        num_of_electrons -= max_number_of_electrons
        filled_shells.append(max_number_of_electrons)
        shell_number += 1
    else:
        filled_shells.append(num_of_electrons)
        num_of_electrons = 0

print(filled_shells)
