""" #empty tuple

t1 = ()
print(t1)

#create a tuple with single item

t1 = (2,)
print(t1)

#homogenous tuple
t3 = (1,2,3,4)
print(t3)

#heterogenous tuple
 t4 = (1,2,2.5,True,"payal", [1,2,3])
print(t4) 

#using type conversion
t5 = tuple("Hello")
print(t5)

#indexing
print(t3[0])
print(t3[-1]) """

#slicing 
""" t4 = (1,2,2.5,True,"payal", [1,2,3])
print (t4[::-1])
 """

 #2D tuple

""" t6 = (1,2,3,4,(5,6,7))
print(t6[4][0])
 """

 #tuples are immutable. hence it cant be edited

 #adding items are not possible

 #deleting whole tuple

""" t3 = (3,4,5)
del t3
print (t3)
 """

#operations on tuple
# + and *

""" t1 = (1,2,3,4)
t2 = (5,6,7,8)
 """
""" print(t1+t2)
print(t1*3)  """

#membership operator

""" print(1 in t1)
print(10 in t1) """

#iteration
""" for i in t2:
    print (i)
 """

 #functions

 #len()
""" t1 = (1,2,3,4)
a=len(t1)
print(a) """

#sum
""" t1 = (1,2,3,4)
a=sum(t1)
print(a)
 """
#min
""" t1 = (1,2,3,4)
a=min(t1)
print(a)
 """
#max
""" t1 = (1,2,3,4)
a=max(t1)
print(a) """

#sorted
""" t1 = (1,2,3,4)
a= sorted(t1, reverse = True)
print(a) """

#count
""" t1 = (1,2,3,4)
a= t1.count(3)
print(a) """

#index
""" t1 = (1,2,3,4)
a= t1.index(4)
print(a) """



