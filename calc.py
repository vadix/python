# coding=utf-8
import math

print("Ведите первое число: ")
x = input()
print("Ведите второе число: ")
y = input()
print("Ведите действие с числами: ")
calc = input()
if x == "" or y == "" or calc == "":
    print()
else:
    float(x)
    float(y)
    assert isinstance(calc, object)
    str(calc)
    if calc == "pow":
        print(pow(x, y))
    elif calc == "div":
        print(x // y)
    elif calc == "+":
        print(x + y)
    elif calc == "-":
        print(x - y)
    elif calc == "/":
        print(x / y)
    elif calc == "*":
        print(x * y)
    elif calc == "mod" and y == 0:
        print("Деление на 0!")
    elif calc == "mod":
        print(x % y)
    else:
        print()