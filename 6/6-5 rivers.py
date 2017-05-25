rivers = {
    'nile':'egypt',
    'amazon':'South America',
    'yangtze':'Asia'
}

for river, country in rivers.items():
    print('The', river.title(), 'runs through', country.title())