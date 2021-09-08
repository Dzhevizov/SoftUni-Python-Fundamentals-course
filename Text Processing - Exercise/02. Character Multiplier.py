word1, word2 = input().split()

result = 0
min_length = min(len(word1), len(word2))

for i in range(min_length):
    result += ord(word1[i]) * ord(word2[i])

if len(word1) > min_length:
    for ch in word1[min_length:]:
        result += ord(ch)
elif len(word2) > min_length:
    for ch in word2[min_length:]:
        result += ord(ch)

print(result)
