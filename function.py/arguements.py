#DEFAULT ARGUEMENT

#exponent function
""" def power(a=1,b=1):
    return a**b """
""" #when both the parameters are passed in functio call. """
""" a = power(2,2)
print(a) """
""" #when only one parameter is passed in function called the default values inside the brackets is taken. """
""" a = power(2)
print(a) """

#welcome guest. welcome customised name.
""" def greet(name = 'guest'):
    print("HELLO" , name) """
""" arguement passed """
""" greet('RASHMI') """
""" arguement not passed """
""" greet() """


#POSITIONAL ARGUEMENTS
#first arguement goes to first parameter. second arguement goes to second parameter.

""" c = power(2,3)
print(c) """


#KEYWORD ARGUEMENT
#when we dont know exactly n which position the parameter is, at such times we can use keyword arguement. this doesnot follow positional arguement 

""" def power(num=1 , expo=1):
    return num**expo

t = power(expo = 3, num = 2)
print(t) """


