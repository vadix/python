sandwich_orders = ['tuna', 'pastrami', 'chichen', 'pastrami', 'meat', 'vegie', 'pastrami']
finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("sorry we don't have pastrami")


while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)

print("\nsandwich_orders ")
print(sandwich_orders)
print("\nfinished_sandwiches")
print(finished_sandwiches)