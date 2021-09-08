key = int(input())
lines = int(input())

for i in range(lines):
    character = input()
    print(chr(ord(character) + key), end='')
