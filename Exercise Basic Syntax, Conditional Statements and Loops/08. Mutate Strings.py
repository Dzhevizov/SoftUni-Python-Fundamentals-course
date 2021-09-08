string1 = input()
string2 = input()
curr_string = ''
last_string = string1

for i in range(len(string1)):
    left_string = string2[:i + 1]
    right_string = string1[i + 1:]
    curr_string = left_string + right_string
    if not curr_string == last_string:
        print(curr_string)
    last_string = curr_string
