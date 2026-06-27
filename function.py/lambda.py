#square using lambda function
""" sq = lambda x: x**2
s = sq(7)
print(s) """


#add
""" add = lambda x,y: x+y
a = add(6,8)
print(a)
 """
#check whether a in a string or not
""" str = lambda s: "a" in s
b = str("Rashmi")
print(b) """

#odd even
""" num = lambda x : "even" if x%2 == 0 else "odd"
t = num(5468)
print(t) """

#lambda function with High Order Function
""" def transform(f,L):
    output = []
    for i in L:
        output.append(f(i))
        
    print(output)

L = [1,2,3,4]        
a = transform(lambda x : x**2 , L)
print(a) """


