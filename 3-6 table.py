guest_list = ['Steve Jobs', 'Bill Gates', 'Linus Torvalds', 'Richard Stallman']
for guest in guest_list:
    print("Welcome to my home " + guest)
print('new guest is coming')
guest_list.insert(0, 'Kernigan Ritchi')
guest_list.insert(3, 'Dennis ')
guest_list.append('Guido van Rossum')

for guest in guest_list:
    print("Welcome to my home " + guest)