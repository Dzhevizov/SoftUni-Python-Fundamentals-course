n = int(input())
first_char = ''
second_char = ''
third_char = ''

for i in range(n):
    first_char = chr(97 + i)
    for j in range(n):
        second_char = chr(97 + j)
        for k in range(n):
            third_char = chr(97 + k)
            print(first_char+second_char+third_char)