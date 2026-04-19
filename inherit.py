class Animal:
    def __init__(self, name):
        self.name = name
        self.isAlive = True


    def eat(self):
        print(f"{self.name} is eating! ")


    def sleep(self):
        print(f"{self.name} is sleeping! ")

    

class Dog(Animal):
    def speak(self):
        print("Woof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")


class Mouse(Animal):
    def speak(self):
        print("Squeeck!")



dog1 = Dog("Buchi")
cat1 = Cat("wuru")
#print(dog1.name)
print(cat1.name)
dog1.speak()