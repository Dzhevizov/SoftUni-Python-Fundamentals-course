num_of_lines = int(input())
result = 0

for i in range(num_of_lines):
    char = input()
    result += ord(char)

print(f"The sum equals: {result}")