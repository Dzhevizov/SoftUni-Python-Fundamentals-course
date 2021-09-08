text = input()

counter = 0

for ch in set(text.lower()):
    if not ch.isdigit():
        counter += 1

print(f"Unique symbols used: {counter}")

word = ""
multiplier = ""

for i in range(len(text)):
    if not text[i].isdigit():
        word += text[i]
    else:
        multiplier += text[i]
        if ((i+1) in range(len(text))) and text[i+1].isdigit():
            continue
        print(word.upper() * int(multiplier), end="")
        word = ""
        multiplier = ""
