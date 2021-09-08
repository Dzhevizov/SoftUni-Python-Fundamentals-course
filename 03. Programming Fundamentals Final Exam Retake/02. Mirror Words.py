import re

text = input()
pattern = r"(?P<surr>@|#)(?P<word1>[A-Za-z]{3,})(?P=surr){2}(?P<word2>[A-Za-z]{3,})(?P=surr)"

matches = re.finditer(pattern, text)

result = []
count = 0

for match in matches:

    word1 = match.group('word1')
    word2 = match.group('word2')

    count += 1

    if word1 == word2[::-1]:
        result.append((word1, word2))

if not count:
    print("No word pairs found!")
else:
    print(f"{count} word pairs found!")
if not result:
    print("No mirror words!")
else:
    print("The mirror words are:")
    for tup in result:
        if tup == result[-1]:
            print(f"{tup[0]} <=> {tup[1]}")
        else:
            print(f"{tup[0]} <=> {tup[1]}", end=", ")
