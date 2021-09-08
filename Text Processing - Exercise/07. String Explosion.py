text = input()
result = ""
power = 0

for i in range(len(text)):
    if text[i] == ">":
        power += int(text[i+1])

        result += text[i]
    else:
        if power > 0:
            power -= 1
            continue
        else:
            result += text[i]

print(result)
