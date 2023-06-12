class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 4

    def open_restaurant(self):
        print(f'{self.restaurant_name} was opened')

    def describe_restaurant(self):
        print(f'{self.cuisine_type} is the best. This restaurant with fast food the best in Turkmenistan')

    def set_number_served(self):
        print(f'The served tables are {self.number_served}')

my_restaurant = Restaurant('Mc_Donalds', 'Fast food')
my_restaurant.open_restaurant()
my_restaurant.describe_restaurant()