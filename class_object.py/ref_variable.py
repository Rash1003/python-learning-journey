class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an instance of the Person class
p1 = Person("Rashmi", 22)
# Create a reference variable that points to the same object as p1
p2 = p1
print(id(p1))  # Print the memory address of p1
print(id(p2))  # Print the memory address of p2 (should be the same as p1)