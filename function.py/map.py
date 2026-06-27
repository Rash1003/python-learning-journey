#map : mapping
#square each item of list

""" a = list(map(lambda x : x**2, [1,2,3,4]))
print(a) """

#extract values from a dictusing map

users = [
    {
        "name":"Rahul",
        "age":12,
        "gender":"male"
    },
    {
        "name":"Rashmi",
        "age":22,
        "gender":"female"
    },
    {
        "name":"Shagun",
        "age":16,
        "gender":"female"
        
    }
]
a = list(map(lambda users:users["name"] , users))
print(a)

b = list(map(lambda users:users["age"] , users))
print(b)

c = list(map(lambda users:users["gender"] , users))
print(c)