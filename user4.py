class User():
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(f"User's last name is {self.last_name} and first name is {self.first_name}. User is {self.gender} and her age is {self.age}")

    def greet_user(self):
        print(f'Hello {self.first_name}')

my_user = User('Dawut', 'Shaimow', 16, 'male')
my_user.describe_user()
my_user.greet_user()