print("Input the person's description:")
name = input("Enter the person's name:").title()
age = input("How old is the person?:")
hair_colour = input("What is the person's hair colour?:")
eye_colour = input("What is the person's eye colour?:")


class Adult:

    def __int__(self, name, age, hair_colour, eye_colour):
        """The function __init__() is a special function in Python classes. It is run as soon as an object of a class is
        instantiated. The method is useful to do any initialization you want to do with your object.
        :param name: The name of the person
        :param age: The age of the person
        :param hair_colour: The colour of the person's hair
        :param eye_colour: The colour of the person's eyes"""
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    def can_drive(self):
        print(f"{name} is old enough to drive.")


class Child(Adult):

    def __int__(self):
        """The function __int__ is a function that is used to initialize the class
        The super function calls the initialization of Adult"""
        super().__int__(name, age, hair_colour, eye_colour)

    def can_drive(self):
        """If the age is less than 18, print a message saying the person is too young to drive. Otherwise, call the can_drive()
        method from the Adult class."""
        if int(age) < 18:
            print(f"{name} is too young to drive.")
        else:
            Adult.can_drive(self)


call2 = Child()
call2.can_drive()
