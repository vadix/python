filename = 'guest.txt'

with open(filename, 'a') as file_object:
    print("Enter guest name")
    guest = input()
    file_object.write(guest)