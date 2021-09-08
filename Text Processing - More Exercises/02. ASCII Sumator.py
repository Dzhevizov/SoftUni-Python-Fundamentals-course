start = input()
end = input()
text = input()

result = 0

for ch in text:
    if ord(ch) in range(ord(start) + 1, ord(end)):
        result += ord(ch)

print(result)
