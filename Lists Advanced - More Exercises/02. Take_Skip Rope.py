given_string = input()
numbers_list = [int(x) for x in given_string if x.isdigit()]
non_numbers_list = [x for x in given_string if not x.isdigit()]

take_list = [numbers_list[i] for i in range(len(numbers_list)) if i % 2 == 0]
skip_list = [numbers_list[i] for i in range(len(numbers_list)) if not i % 2 == 0]

taken_list = []
skipped_list = []

is_end_of_list = False

for i in range(len(take_list)):
    for j in range(take_list[i]):
        if j not in range(len(non_numbers_list)):
            is_end_of_list = True
            break
        taken_list.append(non_numbers_list[j])

    if is_end_of_list:
        break

    for k in range(take_list[i]):
        non_numbers_list.pop(0)

    for l in range(skip_list[i]):
        if l not in range(len(non_numbers_list)):
            is_end_of_list = True
            break
        skipped_list.append(non_numbers_list[l])

    if is_end_of_list:
        break

    for m in range(skip_list[i]):
        non_numbers_list.pop(0)

print("".join(taken_list))

