class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def greet(person):
    print(f"Hello, my name is {person.name} and I am {person.age} years old.")
    p1 = Person("Rashmi", 22)
    return p1

# Create an instance of the Person class
p = Person("Payal", 20)
x = greet(p)  # Pass the object p as a parameter to the greet function
print(x.name)
print(p.name)
