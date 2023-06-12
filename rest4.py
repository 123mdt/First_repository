class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def open_restaurant(self):
        print(f'{self.restaurant_name} was opened')

    def describe_restaurant(self):
        print(f'{self.cuisine_type} is the best. This restaurant with fast food the best in Turkmenistan')

my_restaurant = Restaurant('Mc_Donalds', 'Fast food')
my_restaurant.open_restaurant()
my_restaurant.describe_restaurant()