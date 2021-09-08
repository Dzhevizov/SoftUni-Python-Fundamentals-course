population = [int(x) for x in input().split(", ")]
min_wealth = int(input())

while True:

    min_el = 1000000
    max_el = 0

    min_index = 0
    max_index = 0

    for i in range(len(population)):
        if population[i] < min_el:
            min_el = population[i]
            min_index = i
        if population[i] > max_el:
            max_el = population[i]
            max_index = i

    if min_el < min_wealth:
        difference = min_wealth - min_el
        if max_el - difference < min_wealth:
            print("No equal distribution possible")
            exit(0)
        else:
            population[max_index] -= difference
            population[min_index] += difference

    else:
        break

print(population)