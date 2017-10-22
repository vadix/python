class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type)

    def open_restaurant(self):
        """Restaurant is open."""
        print("Restaurant " + self.restaurant_name.title() + " is open.")

    def set_number_served(self, served):
        """Add served person"""
        self.number_served = served

    def increment_number_served(self, served):
        """docs"""
        self.number_served += served

restaurant = Restaurant('tiflis', 'georgian')

print(restaurant.number_served)
restaurant.number_served = 5
print(restaurant.number_served)
restaurant.set_number_served(10)
print(restaurant.number_served)
restaurant.increment_number_served(10)
print(restaurant.number_served)

