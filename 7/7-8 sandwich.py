sandwich_orders = ['tuna', 'chichen', 'meat', 'vegie']
finished_sandwiches = []
print("\nsandwich_orders ")
print(sandwich_orders)
print("\nfinished_sandwiches")
print(finished_sandwiches)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)
    
print("\nsandwich_orders ")
print(sandwich_orders)
print("\nfinished_sandwiches")
print(finished_sandwiches)