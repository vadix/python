filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

print('---------------------------')

with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())

print('---------------------------')

with open(filename) as file_object:
    lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line

    print(pi_string)