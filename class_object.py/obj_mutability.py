class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def greet(person):
    print(f"Hello, my name is {person.name} and I am {person.age} years old.")
    p1 = Person("Atul", 32)
    return person

# Create an instance of the Person class
p = Person("Rashmi", 22)
print(id(p))  # Print the memory address of p
x = greet(p) 
# Call the greet function and pass the object p as a parameter
print(id(x))  # Print the memory address of x (should be same as p)
