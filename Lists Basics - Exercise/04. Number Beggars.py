input_string = input()
count_of_beggars = int(input())

list_of_offers = input_string.split(", ")
sums_taken = []

for i in range(count_of_beggars):
    sum_taken = 0
    for j in range(i, len(list_of_offers), count_of_beggars):
        sum_taken += int(list_of_offers[j])
    sums_taken.append(sum_taken)

print(sums_taken)