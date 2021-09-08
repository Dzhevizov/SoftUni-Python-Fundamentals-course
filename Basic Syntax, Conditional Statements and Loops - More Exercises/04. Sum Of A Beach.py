input_string = input()
input_string = input_string.lower()
counter = 0

counter += input_string.count("water")
counter += input_string.count("sand")
counter += input_string.count("fish")
counter += input_string.count("sun")

print(counter)