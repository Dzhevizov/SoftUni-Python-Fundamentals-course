def first_letter_decoder(given_string):
    ascii_code_list = []
    left_list = []
    for el in given_string:
        if ord(el) in range(48, 58):
            ascii_code_list.append(el)
        else:
            left_list.append(el)
    ascii_code = "".join(ascii_code_list)
    first_letter = chr(int(ascii_code))
    left_list[0], left_list[-1] = left_list[-1], left_list[0]
    left_string = "".join(left_list)
    new_string = first_letter + left_string
    return new_string


input_words = input().split()
new_list = [first_letter_decoder(x) for x in input_words]
output_string = ' '.join(new_list)
print(output_string)




