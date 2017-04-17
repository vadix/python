guest_list = ['Steve Jobs', 'Bill Gates', 'Linus Torvalds', 'Richard Stallman']
for guest in guest_list:
    print("Welcome to my home " + guest)
missing_guest = 'Steve Jobs'
new_guest = 'Kernigan Ritchi'
print("Sorry " + missing_guest + " couldn't come")

guest_list.remove(missing_guest)
guest_list.append(new_guest)
for guest in guest_list:
    print("Welcome to my home " + guest)