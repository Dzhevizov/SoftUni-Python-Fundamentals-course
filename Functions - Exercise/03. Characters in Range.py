def find_characters(a, b):
    for i in range(ord(a) + 1, ord(b)):
        print(chr(i), end=" ")


char1 = input()
char2 = input()
find_characters(char1, char2)
