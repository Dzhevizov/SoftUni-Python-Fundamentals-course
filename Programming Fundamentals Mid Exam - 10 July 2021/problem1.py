food_per_month = float(input())
hay_per_month = float(input())
cover_per_month = float(input())
weight = float(input())

for i in range(1, 31):

    food_per_month -= 0.3

    if i % 2 == 0:
        hay_per_month -= food_per_month * 0.05

    if i % 3 == 0:
        cover_per_month -= weight / 3

    if food_per_month < 0.01 or hay_per_month < 0.01 or cover_per_month < 0.01:
        print("Merry must go to the pet store!")
        exit(0)

print(f"Everything is fine! Puppy is happy! Food: {food_per_month:.2f}, \
Hay: {hay_per_month:.2f}, Cover: {cover_per_month:.2f}.")
