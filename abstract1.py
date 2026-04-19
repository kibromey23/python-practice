from abc import ABC,abstractmethod
class Animal(ABC):

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        print("hello kb")


class Dog(Animal):
    def eat(self):
        print("dog is eating")

    def sleep(self):
        print("dog is sleeping")




dog = Dog()
dog.sleep()
dog.eat()

cm²
