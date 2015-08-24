import math

print("Ведите первое число: ")
x = float(input())
print("Ведите второе число: ")
y = float(input())
print("Ведите действие с числами: ")
calc = input(str())


if calc == "pow":
    print(pow(x, y))
else:
    print(" ")
