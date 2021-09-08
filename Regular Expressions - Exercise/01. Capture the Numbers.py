import re

pattern = r"\d+"
text = input()

while text:
    matches = re.findall(pattern, text)
    if matches:
        print(*matches, end=" ")

    text = input()
