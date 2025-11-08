class Animal:
# Constructor to initialize the animal with name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Method to return a description of the animal
    def describe(self):
        return f"{self.name} is {self.age} years old"
    # Generic speak method which will be overridden in subclasses
    def speak(self, sound):
        return f"{self.name} says {sound}"
# Define the subclass 'Dog' that inherits from 'Animal'
class Dog(Animal):
    # Dog's constructor includes an additional attribute 'breed'
    def __init__(self, name, age, breed):
        super().__init__(name, age) # Call the superclass (Animal) constructor
        self.breed = breed # Additional attribute for breed
    # Overridden speak method specific to dogs
    def speak(self):
        return f"{self.name} barks."
    # Define the subclass 'Cat' that also inherits from 'Animal'
class Cat(Animal):
    # Cat's constructor includes an additional attribute 'color'
    def __init__(self, name, age, color):
        super().__init__(name, age) # Call the superclass (Animal) constructor
        self.color = color # Additional attribute for color
    # Overridden speak method specific to cats
    def speak(self):
       return f"{self.name} meows."
# Create instances of Dog and Cat
my_dog = Dog("Rex", 5, "German Shepherd")
my_cat = Cat("Whiskers", 3, "Black")
# Output descriptions and sounds from each animal
print(my_dog.describe()) # Output: Rex is 5 years old
print(my_dog.speak()) # Output: Rex barks.
print(my_cat.describe()) # Output: Whiskers is 3 years old
print(my_cat.speak()) # Output: Whiskers meows.