text = input().split()
result = 0

for word in text:
    if word[0].islower():
        result += int(word[1:-1]) * (ord(word[0]) - 96)
    else:
        result += int(word[1:-1]) / (ord(word[0]) - 64)

    if word[-1].islower():
        result += ord(word[-1]) - 96
    else:
        result -= ord(word[-1]) - 64

print(f"{result:.2f}")
