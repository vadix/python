class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type)
    def open_restaurant(self):
        """Restaurant is open."""
        print("Restaurant " + self.restaurant_name.title() + " is open.")


restaurant1 = Restaurant('gvozd', 'belorusian')
restaurant2 = Restaurant('birkeller', 'german')
restaurant3 = Restaurant('gambrinus', 'world')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()