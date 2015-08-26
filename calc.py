# coding=utf-8
import math


x = float(input())
y = float(input())
calc = input()

if calc == "+":
    print(x + y)
if calc == "-":
    print(x - y)
if calc == "/":
    if y != 0:
        print(x / y)
    else:
        print("Деление на 0!")
if calc == "*":
    print(x * y)
if calc == "mod":
    if y != 0:
        print(x % y)
    else:
        print("Деление на 0!")
if calc == "pow":
    print(pow(x, y))
if calc == "div":
    if y != 0:
        print(x // y)
    else:
        print("Деление на 0!")