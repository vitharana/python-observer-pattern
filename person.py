from event import post_event
class Person:
    def __init__(self, name, age, city) -> None:
        self.name = name
        self.age = age
        self.city = city

        post_event("print-details-on-creation", self)

        # print(f"Person called {self.name} was created")
        # print("Object Ref", self)

    def print_myself(self):
        my_self = f"My name is {self.name}, I am {self.age} and I live in {self.city}"

        post_event("normal-print", my_self)
        post_event("capital-print", my_self)
        post_event("all-print",my_self)
        # print(my_self)
        # print(my_self.upper())


