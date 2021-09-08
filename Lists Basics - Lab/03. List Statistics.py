num_of_integers = int(input())

list_of_positives = []
list_of_negatives = []

for i in range(num_of_integers):
    curr_int = int(input())
    if curr_int >= 0:
        list_of_positives.append(curr_int)
    else:
        list_of_negatives.append(curr_int)

print(list_of_positives)
print(list_of_negatives)
print(f'Count of positives: {len(list_of_positives)}. Sum of negatives: {sum(list_of_negatives)}')
