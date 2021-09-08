def check_palindrome(list_of_nums):
    list_of_nums = list_of_nums.split(", ")
    for element in list_of_nums:
        if element[:] == element[::-1]:
            print(True)
        else:
            print(False)


input_list = input()
check_palindrome(input_list)