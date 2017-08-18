def sandwich_ingredients(*ingredients):
    print("\nyour ingridens: ")
    for ingredient in ingredients:
        print(ingredient)

sandwich_ingredients("butter", "onion", "chicken")
sandwich_ingredients("butter1", "onion2", "chicken3", "butter4", "onion5", "chicken6")
sandwich_ingredients("onion")