prompt = "\nPlease add toping to your pizza:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(topping + " added to your pizza")