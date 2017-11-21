filename = 'reason.txt'

with open(filename, 'a') as file_object:
    while True:
        reason = input("What do you like in programming?\n")
        if reason == 'quit':
            break
        else:
            file_object.write(reason + '\n')
