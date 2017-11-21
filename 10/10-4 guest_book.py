filename = 'guest_book.txt'

with open(filename, 'a') as file_object:
    while True:
        guest = input("Enter guest name or quit for exit\n")
        if guest == 'quit':
            break
        else:
            file_object.write(guest + '\n')
            print("Glad to see you " + guest)