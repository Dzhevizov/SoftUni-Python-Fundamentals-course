num_of_lines = int(input())
brackets_counter = 0

for i in range(num_of_lines):
    string = input()
    if string == "(":
        if not brackets_counter:
            brackets_counter += 1
        else:
            print("UNBALANCED")
            exit(0)
    elif string == ")":
        if not brackets_counter:
            print("UNBALANCED")
            exit(0)
        else:
            brackets_counter = 0

if not brackets_counter:
    print("BALANCED")
else:
    print("UNBALANCED")