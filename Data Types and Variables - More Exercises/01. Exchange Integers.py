num1 = int(input())
num2 = int(input())
print(f"Before:\na = {num1}\nb = {num2}")
temp = num1
num1 = num2
num2 = temp
print(f"After:\na = {num1}\nb = {num2}")