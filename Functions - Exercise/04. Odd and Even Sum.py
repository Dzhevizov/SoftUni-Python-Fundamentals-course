def find_odd_and_even_sum(number):
    even_sum = 0
    odd_sum = 0
    for digit in number:
        if not int(digit) % 2:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


input_number = input()
print(find_odd_and_even_sum(input_number))
