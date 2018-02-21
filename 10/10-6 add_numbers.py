
try:
    print("Enter first digit: ")
    x = input()
    print("Enter second digit: ")
    y = input()
    first_number = int(x)
    second_number = int(y)
    print(first_number + second_number)
except TypeError:
    print("use only digits")