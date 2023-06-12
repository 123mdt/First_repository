class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
            
    def open_restaurant(self):
        print(f'{self.restaurant_name} opened')

    def describe_restaurant(self):
        print(f'{self.cuisine_type} is the best. This restaurant with Turkish food the best in Turkmenistan')
    
my_restaurant1 = Restaurant('MB', 'Turkish food')
my_restaurant1.describe_restaurant()
    
my_restaurant2 = Restaurant('RIM', 'Italian food')
my_restaurant2.describe_restaurant()
    
my_restaurant3 = Restaurant('Mc_Donalds', 'Fast food')
my_restaurant3.describe_restaurant()