def gmagicians(magicians, great_magicians):
    while magicians:
        current_magician = magicians.pop()
        great_magicians.append("great " + current_magician)


def show_magicians(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

magicians = ['lsjdfs', 'lsjdf', 'slkjfsjf']
great_magicians = []


gmagicians(magicians, great_magicians)
show_magicians(magicians)
show_magicians(great_magicians)
