import re

text = input()

cool_threshold = 1

cool_threshold_pattern = r"\d"
digits = re.findall(cool_threshold_pattern, text)
for digit in digits:
    cool_threshold *= int(digit)

print(f"Cool threshold: {cool_threshold}")

emoji_validator = r"(?P<sep>[:]{2}|[*]{2})(?P<emoji>[A-Z][a-z]{2,})(?P=sep)"
valid_emojis = re.finditer(emoji_validator, text)

print(f"{len(list(valid_emojis))} emojis found in the text. The cool ones are:")

valid_emojis = re.finditer(emoji_validator, text)

for match in valid_emojis:

    threshold = 0

    sep = match.group('sep')
    emoji = match.group('emoji')

    for ch in emoji:
        threshold += ord(ch)

    if threshold >= cool_threshold:
        print(f"{sep}{emoji}{sep}")
