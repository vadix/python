prompt = input("\nHow old are you? ")
age = int(prompt)

if age < 3:
    print("get your free ticket")
if age > 3 and age < 12:
    print("your price 10")
if age > 12:
    print("your price 15")