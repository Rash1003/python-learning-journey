#1D list Homogenous
""" L = [1, 2, 3, 4, 5]
print(L)

#2D list Heterogenous   
M = [1,2,[3,4,5]]
print(M)

#3D list Heterogenous
N = [1,2,[3,4,[5,6]]]
print(N)

#3D list Homogenous
O = [[1,2,3], [4,5,6], [7,8,9]]
print(O)

#Type Conversion in list
print (list["PAYAL"])
 """

""" L = [1, 2, 3, 4, 5]
L.append([6,7,8])
print(L)
 """

""" L = [1, 2, 3, 4, 5]
L.extend([6,7,8])
print(L) """

""" L  = [1, 2, 3, 4, 5]
L.insert(2, 10)
print(L) """


""" L  = [1, 2, 3, 4, 5]
L[0:2] = [10,20,30]
print(L)
 """
""" L  = [1, 2, 3, 4, 5]
del L[0:2]
print(L)
 """

# ADD 1 to 10 numbers in a list

""" L= []
for i in range (1,11):
    L.append(i)
print(L)

M = [i for i in range (1,11)]
print(M) """

#scalar multiplication with vector

""" s = [2,3,4]
v = -3

L = []
for i in s:
    L.append(i*v)
print(L) """

""" s = [2,3,4]
v = -3

L = [i*v for i in s]
print(L) """

#Add squares

""" L = [2,4,6,8,10]
s = [i**2 for i in L]
print(s)
 """

# add cubes
""" L = [2,4,6,8,10]
s = [i**3 for i in L]
print(s)
 """

# print all the number divisible by 5 from 1 to 50

""" L = [i for i in range (1,51) if i%5 ==0 ]
print(L) """

#find languages startig with P

""" L = ["java", "php", "python", "c"]
s = [i for i in L if i[0] == "p"]
print(s) """

#Nested if with list comprehension
 
""" basket = ["apple", "banana", "guava" , "pineapple" , "litchi" , "grapes"]
my_fruits = ["guava" , "grapes" , "pineapple"]

s = [fruit for fruit in my_fruits if fruit in basket if fruit[0] == "g" ]
print(s) """

#print a (3x3) matrix using list comprehension
 
""" s = [[i*j for i in range(1,4)] for j in range(1,4)]
print(s)
 """

#print a cartesian product on list

""" L1 = [1,2,3,4]
L2 = [5,6,7,8]

s = [i*j for i in L1 for j in L2]
print(s) """

# List traversal itemwise

""" L = [1,2,3,4]

for i in L:
    print(i)
"""

#List Traversal Indexwise

""" L = [1,2,3,4]

for i in range(0,len(L)):
    print(L[i])

"""

#zip function in list
""" L1 = [2,3,4,5]
L2 = [-2, -3, -4, -5]

s = list(zip(L1,L2))
print(s)
 """
#add the items for 2 lists together using zip

""" L1 = [2,3,4,5]
L2 = [-2, -3, -4, -5]

zip = list(zip(L1,L2))
s = [i+j for i,j in zip]
print(s)
 """

 