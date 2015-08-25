import math

print("Ведите первое число: ")
x = input()
if x =="":
    exit
else:
    float(x)
    
print("Ведите второе число: ")
y = input()
if y =="":
    exit
else:
    float(y)
    
print("Ведите действие с числами: ")
calc = input()
if calc =="":
    exit
else:
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


