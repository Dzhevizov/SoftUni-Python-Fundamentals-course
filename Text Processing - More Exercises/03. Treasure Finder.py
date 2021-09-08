key = [int(x) for x in input().split()]

text = input()

while not text == "find":

    i = 0
    new_text = ""

    for ch in text:
        if i >= len(key):
            i -= len(key)
        code = ord(ch) - key[i]
        new_text += chr(code)
        i += 1

    first = 0

    treasure_type = ""

    for ch in new_text:
        if ch == "&":
            if first == 0:
                first = new_text.index(ch) + 1
            else:
                break
        else:
            if not first == 0:
                treasure_type += ch

    treasure_coordinates = new_text[new_text.index("<") + 1:new_text.index(">")]

    print(f"Found {treasure_type} at {treasure_coordinates}")

    text = input()
