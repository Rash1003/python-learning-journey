#type and id

def square(num):
    return num**2
 
"""
print(type(square))    
print(id(square)) """

#reassign

""" x = square
a = x(3)
print(a)
 """
#returning function through other function

def f():
    def x(a,b):
        return a+b
    return x

val = f()(3,4)
print(val)