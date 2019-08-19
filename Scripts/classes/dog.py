class Dog():
    """Простая модель собаки."""
    def __init__(self, name, age):
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age
    def sit(self):
        """Собака садится по команде."""
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        """Собака перекатывается по команде."""
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog1 = Dog('willie1', 16)
print("My dog's name is " + my_dog1.name.title() + ".")
print("My dog is " + str(my_dog1.age) + " years old.")


my_dog1 = my_dog
print("My dog's name is " + my_dog1.name.title() + ".")
print("My dog is " + str(my_dog1.age) + " years old.")

my_dog1.sit()
my_dog1.roll_over()
