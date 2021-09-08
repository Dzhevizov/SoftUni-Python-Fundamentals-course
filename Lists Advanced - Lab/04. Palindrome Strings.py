words_list = input().split()
searched_palindrome = input()

palindrome_list = [x for x in words_list if x[:] == x[::-1]]
print(palindrome_list)

palindrome_counter = 0
for el in palindrome_list:
    if searched_palindrome == el:
        palindrome_counter += 1
print(f'Found palindrome {palindrome_counter} times')
