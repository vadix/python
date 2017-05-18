python_functions = {'sum': 'Sums start and the items of an iterable from left to right and returns the total. start defaults to 0. The iterable‘s items are normally numbers, and the start value is not allowed to be a string.',
                    'len': 'Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).',
                   'input': 'Equivalent to eval(raw_input(prompt)).',
                   'open': 'Open a file, returning an object of the file type described in section File Objects. If the file cannot be opened, IOError is raised. When opening a file, it’s preferable to use open() instead of invoking the file constructor directly.',
                   'print': 'Print objects to the stream file, separated by sep and followed by end. sep, end and file, if present, must be given as keyword arguments.'}

print('Function sum(): \n' + python_functions['sum'] + '\n')
print('Function len(): \n' + python_functions['len'] + '\n')
print('Function input(): \n' + python_functions['input'] + '\n')
print('Function open(): \n' + python_functions['open'] + '\n')
print('Function print(): \n' + python_functions['print'])
