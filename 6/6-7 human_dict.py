human = {
    'vmolchanov':
    {
        'first_name': 'vadim',
        'last_name': 'molchanov',
        'age': '33',
        'city': 'minsk'
    },
    'akalechic':
    {
        'first_name': 'anastasia',
        'last_name': 'kalechic',
        'age': '31',
        'city':'borisov',
    },
    'rmiasnikov':
    {
        'first_name': 'rostislav',
        'last_name': 'miasnikov',
        'age': '32',
        'city': 'smolevichy'
    },
    }

for name, info in human.items():
    print('\nUsername: ' + name)
    full_name = info['first_name'] + ' ' + info['last_name'] + '\n'
    city = info['city']
    print(full_name.title() + city.title())