""" a = 3/4 * 1/2
print(a)
o/p: 0.375 """
# We want this to be in a fraction. not in decimal.
#We are creating a datatype of fraction

class Fraction:

    #parameterised constructor
    def __init__(self,x,y):
        self.num = x
        self.den = y

    #another magic method __str__ This is executed automatically y default after out constructor.    
    def __str__(self):
        return "{}/{}".format(self.num,self.den)

    def __add__(self,other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den

        return "{}/{}".format(new_num,new_den)

    def __sub__(self,other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den

        return "{}/{}".format(new_num,new_den)
        

    def __mul__(self,other):
        new_num = self.num * other.num
        new_den = self.den * other.den

        return "{}/{}".format(new_num,new_den)

    def __truediv__(self,other):
        new_num = self.num * other.den
        new_den = self.den * other.num

        return "{}/{}".format(new_num,new_den)


    

fr1 = Fraction(3,4)
fr2 = Fraction(1,2)


print(fr1 + fr2)
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1 / fr2)

