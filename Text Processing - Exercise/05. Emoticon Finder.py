text = input()

for i in range(len(text)):

    if text[i] == ":":
        if (i + 1) in range(len(text)) and not text[i+1] == " ":
            print(f"{text[i]}{text[i+1]}")
