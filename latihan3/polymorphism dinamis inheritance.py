class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("WOOF!!")

class Cat(Animal):
    def speak(self):
        print("Meows..")

class Harimau(Animal):
    def speak(self):
        print("Rraawrrr...")

class Kuda(Animal):
    def speak(self):
        print("Hhiiiiaaa....")

def speak(animal):
        animal.speak()

animal = Animal()
dog = Dog()
cat = Cat()
harimau = Harimau()
kuda= Kuda()

speak(animal)
speak(dog)
speak(cat)
speak(harimau)
speak(kuda)
