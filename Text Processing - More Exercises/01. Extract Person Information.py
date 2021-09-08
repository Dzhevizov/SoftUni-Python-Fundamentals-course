num_lines = int(input())

for _ in range(num_lines):

    text = input()

    name = text[text.index("@") + 1:text.index("|")]
    age = text[text.index("#") + 1:text.index("*")]

    print(f"{name} is {age} years old.")
