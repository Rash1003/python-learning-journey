#args
#we can pass numerous variable parameters.

#without args
""" def multiply(a,b):
    return a*b

a = multiply(2,3)
print(a) """

#with using args
#we dont know how many parameters user will be providing. in that case we use args.
""" def multiply(*args):
    product = 1

    for i in args:
        product = product*i
    
    print (product)

multiply(1,2,3,4,5) """

