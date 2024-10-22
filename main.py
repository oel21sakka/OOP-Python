from abc import ABC, abstractmethod


class Animal(ABC):
    total_animals = 0

    def __init__(self, name, age, color):
        self.__name = name
        self.__age = age
        self.__color = color
        Animal.total_animals += 1

    @abstractmethod
    def speak(self):
        pass

    def get_info(self, *args, **kwargs):
        info = f"Name: {self.__name}, Age: {self.__age}, Color: {self.__color}"
        if args:
            info += f"\n Additional Info:\n {', '.join(args)}"
        if kwargs:
            info += f"\n Properties:\n {', '.join([f'{key}: {value}' for key, value in kwargs.items()])}"
        return info

    @classmethod
    def get_total_animals(cls):
        return cls.total_animals

    @staticmethod
    def animal_type():
        return "This is an animal."

    def __del__(self):
        Animal.total_animals -= 1


class Dog(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.__breed = breed

    def speak(self):
        return "howhow!"

    def get_info(self, *args, **kwargs):
        info = super().get_info(*args, **kwargs)
        info += f"\n Breed: {self.__breed}"
        return info


class Cat(Animal):
    def speak(self):
        return "meow!"


class Bird(Animal):
    def speak(self):
        return "swsw!"


def animal_sound(animal):
    print(f"{animal.get_info()} and says: {animal.speak()}")


dog = Dog("yasta", 5, "Brown", "Labrador")
cat = Cat("orange", 3, "orange")
bird = Bird("tweety", 1, "Yellow")

animal_sound(dog)
animal_sound(cat)
animal_sound(bird)

print(f"Total animals created: {Animal.get_total_animals()}")
print(Animal.animal_type())

print('yasta data:', dog.get_info("loves to play", "friendly", habitat="house"))
print('orange data:', cat.get_info(habitat="apartment"))

del bird
print(f"Total animals created after tweety RIP: {Animal.get_total_animals()}")

