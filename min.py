a = input("Enter the first number: ")
b = input("Enter the second number: ")  
c = input("Enter the third number: ")

def min(a, b, c):
    if a<=b and a<=c:
        print("The smallest number is:", a)
    elif b<=a and b<=c:
        print("The smallest number is:", b)
    else:
        print("The smallest number is:", c)

min(a, b, c)
