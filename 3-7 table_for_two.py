guest_list = ['Steve Jobs', 'Bill Gates', 'Linus Torvalds', 'Richard Stallman']
for guest in guest_list:
    print("Welcome to my home " + guest)
print('new guest is coming')
guest_list.insert(0, 'Kernigan Ritchi')
guest_list.insert(3, 'Dennis ')
guest_list.append('Guido van Rossum')

for guest in guest_list:
    print("Welcome to my home " + guest)

print('sorry, table only for two')


print("sorry, you couldn't come " + guest_list.pop(-1))
print("sorry, you couldn't come " + guest_list.pop(-1))
print("sorry, you couldn't come " + guest_list.pop(-1))
print("sorry, you couldn't come " + guest_list.pop(-1))
print("sorry, you couldn't come " + guest_list.pop(-1))
for guest in guest_list:
    print("Welcome to my home " + guest)
del guest_list[0]
del guest_list[0]

print(guest_list)