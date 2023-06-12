class User():
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(f"User's first name is {self.first_name} and last name is {self.last_name}. User is {self.age} and user's gender is {self.gender}")

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}')

my_user = User('Medet', 'Mammetsahatow', 13, 'male')
my_user.describe_user()
my_user.greet_user()