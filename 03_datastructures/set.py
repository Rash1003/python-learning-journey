#wrong syntax to create a set
""" s = {}
print(type(s)) """

#correct syntax to create a set. Use TypeConversion
""" s = set()
print(type(s)) """

#homogenous set
""" s = {1,2,3,4} """

#heterogenous set. 

# wrong syntax. Cannot store a mutable datatype in set.abs
""" s= {1,2,2.5,True,"payal", {1,2,3}}
print(s) """
#correct syntax. True wouldnt print bcz python prints true as 1. and duplicates are not in sets
#sets are unordered. position of items in output is determined by hashing internally.
""" s= {1,2,3,4,2.5, True, "payal"}
print(s) """

#duplicates not allowed
""" s = {1,1,2,2,3,3}
print(s) """

#Acessing items from set. Indexing doesnt work. Slicing is also not possible.
#we cannot access and edit set items
#wrong syntax

""" s= {1,2,3,4,5}
a = s[0]
print(a)"""

#add items in set

""" s = {1,2,3,4}
s.add(5)
print(s) """

#update a set
""" s={1,2,3,4}
s.update([5,6,7,8])
print(s) """

#deleteing whole set
"""
s={1,2,3,4}
del s
print(s) """

#deleting one item from set
#discard. if item to be deleted is not found in set it doesnot throw an error.
""" s = {1,2,3,4,5}
s.discard(5)
print(s) """

#remove. If the item to be deleted not found in a set then remove function throws an error. Thats the major diffrence.
""" s = {1,2,3,4,5}
s.remove(5)
print(s)
 """

#pop. deletes any random item.
""" s = {1,2,3,4,5}
s.pop()
print(s) """

#clear. deletes all the items from set making it an empty set.abs
""" s={1,2,3}
s.clear()
print(s)
 """

 #OPERATIONS ON SETS
 #UNION(|)  
""" s1 = {1,2,5,3,4}
s2 = {6,7,8,5}
w = s1 | s2
print(w)
#INTERSECTION(&)
x = s1 & s2
print(x)
#DIFFERENCE(-)
y = s1 - s2
print(y)
#SYMMETRIC DIFFERENCE(^)
z = s1 ^ s2
print(z)
#MEMBERSHIP OPERATOR
d = 1 in s1
print(d)
d = 1 in s2
print(d)
#ITERATION 
for i in s1:
    print(i) """


#SET FUNCTIONS
#len()
# min()
# max()
# sorted()

#UNION / UPDATE
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
""" s1.update(s2)
print(s1) """                               #permanently updates s1

#INTERSECTION / INTERSECTION_UPDATE

""" a = s1.intersection(s2)
print(a)
b = s1.intersection_update(s2)
print(s1)
 """
#difference / difference_update
""" s1.difference(s2)
print(s1)
s1.difference_update(s2)
print(s1) """

#symmetreic_difference / symmetric_difference_update

#isdisjoint
""" t=s1.disjoint(s2)
print(t) """

#issubset
""" u = s1.issubset(s2)
print(u) """

#issuperset
""" v = s1.issuperset(s2)
print(v) """


#copy
""" s1={1,2,3}
s2 = s1.copy()
print(s2) """

#frozenset
#immuatable version of python set
#same like list and tuple
#all operations will work on a frozenset except add del update etc
""" fs = frozenset([1,2,3])
print(fs) """

#set comprehension like list
a = {i for i in s2}
print(a)