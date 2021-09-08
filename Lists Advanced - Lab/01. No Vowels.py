input_text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
output_list = [x for x in input_text if x.lower() not in vowels]
print("".join(output_list))
