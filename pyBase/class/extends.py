class Animal(object):
    def __init__(self):
        pass

    def run(self):
        print("Animal is running...")


class Dog(Animal):
    def __init__(self):
        super().__init__()
        pass

    def run(self):
        print("A dog is running...")

    def eat(self):
        print("Dog is eating")


class Cat(Animal):
    def __init__(self):
        super().__init__()
        pass

    def run(self):
        print("A cat is running...")

    def eat(self):
        print("Cat is eating")


def run_twice(animal):
    animal.run()
    animal.run()


if __name__ == '__main__':
    dog = Dog()
    cat = Cat()
    run_twice(cat)
    run_twice(dog)
