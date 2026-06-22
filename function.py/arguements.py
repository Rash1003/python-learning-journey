#DEFAULT ARGUEMENT

#exponent function
def power(a=1,b=1):
    return a**b
""" #when both the parameters are passed in functio call. """
a = power(2,2)
print(a)
""" #when only one parameter is passed in function called the default values inside the brackets is taken. """
a = power(2)
print(a)

#welcome guest. welcome customised name.
def greet(name = 'guest'):
    print("HELLO" , name)
""" arguement passed """
greet('RASHMI')
""" arguement not passed """
greet()

