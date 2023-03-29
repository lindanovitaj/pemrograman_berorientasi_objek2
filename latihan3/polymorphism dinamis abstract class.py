class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def speak(self):
        return "Meow"
    
class Dog(Animal):
    def speak(self):
        return "Woof"

class Cow(Animal):
    def speak(self):
        return "Moo"

animals = [Cat(), Dog(), Cow()]
for animal in animals:
    print(animal.speak())
