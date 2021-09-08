text = input()

result = " "

for ch in text:
    if not ch == result[-1]:
        result += ch

print(result.strip())
