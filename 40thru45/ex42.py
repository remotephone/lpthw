## Animal is-a object (yes, sort of confusing) look at the extra credit.
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has a salary and a name
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat that has-a name Satan
satan = Cat("Satan")

## mary is-a Person that is-a Mary
mary = Person("Mary")

## frank is-a Employee named Frank with a Salary of 120000
frank = Employee("Frank", 120000)

## rover is-a pet of frank
frank.pet = rover

## Fish has a flipper
flipper = Fish()

## Salmon is-a crouse
crouse = Salmon()

## Halibut has a harry
harry = Halibut()
