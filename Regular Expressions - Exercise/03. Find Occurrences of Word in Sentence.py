import re

text = input().lower()
pattern = rf"\b{input().lower()}\b"

matches = re.findall(pattern, text)

print(len(matches))
