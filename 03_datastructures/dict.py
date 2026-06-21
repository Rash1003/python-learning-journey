#empty dictionary
""" d={}
print(type(d)) """

#1D Dictionary
""" d1 = {"name":"Rashmi" , "age":"22" , "gender":"female" , "id":"1234"}
print(type(d1)) """

#2D Dictionary
""" d2 = {"name":"Rashmi",
 "age":22,
  "gender":"female",
   "id":1234,
    "subject": {
        "maths":90,
        "dsa":85,
        "python":95
    }
}
print(d2) """

#typeconversion
""" d3 = ([("name","Rashmi"), ("age",22),("sem",4), ("id",(1234))])
print(d3) """

#cannot have duplicate keys. updated value is printed. previous value is ignored
""" d4 = {"name": "rashmi", "name":"payal"}
print(d4) """

#mutable items as keys are not allowed
""" d5 = {"name":"Rashmi" , (1,2,3): 2 }
print(d5) """

#Accessing item from dictionary.
#Indexing not allowed.
""" d1 = {"name":"Rashmi" , "age":"22" , "gender":"female" , "id":"1234"}
a = d1[0]
print(a)
#this throws error """

#passing corresponding key for fetching the value stored inside it.
""" d1 = {"name":"Rashmi" , "age":"22" , "gender":"female" , "id":"1234"}
a = d1["name"]
print(a) """

""" d1 = {"name":"Rashmi" , "age":"22" , "gender":"female" , "id":"1234"}
b = d1.get("age")
print(b) """

#Adding new key value pair
""" d1 = {"name":"Rashmi" , "age":"22" , "gender":"female" , "id":"1234"}
d1["sem"] = 4
print(d1) """

#Remove key value pair
""" d1 = {"name":"Rashmi" , "age":"22" , "gender":"female" , "id":"1234" , "school": "sia"}
d1.popitem()
print(d1) """

#Delete
""" d1 = {"name":"Rashmi" , "age":"22" , "gender":"female" , "id":"1234"} """
""" del d1["name"]
print(d1) """

#clear
""" d1.clear()
print(d1) """

#fetching items from 2D dictionaries
""" d2 = {"name":"Rashmi",
 "age":22,
  "gender":"female",
   "id":1234,
    "subject": {
        "maths":90,
        "dsa":85,
        "python":95
    }
} """

""" a = d2["subject"]["dsa"]
print(a) """

#adding key value pair
""" d2 = {"name":"Rashmi",
 "age":22,
  "gender":"female",
   "id":1234,
    "subject": {
        "maths":90,
        "dsa":85,
        "python":95
    }
}

d2["subject"]["java"] = 55
print(d2) """

#deleting subject
""" d2 = {"name":"Rashmi",
 "age":22,
  "gender":"female",
   "id":1234,
    "subject": {
        "maths":90,
        "dsa":85,
        "python":95,
        "java":55
    }
}
del d2["subject"]["java"]
print(d2) """

#Editing key value
""" d2["gender"] = "male"
print(d2) """

#DICTIONARY OPERATIONS
#Membership oprations
""" d2 = {"name":"Rashmi",
 "age":22,
  "gender":"female",
   "id":1234,
    "subject": {
        "maths":90,
        "dsa":85,
        "python":95,
        "java":55
    }
} """

#throws error when value is passed
""" f = "Rashmi" in d2
print (f) """

#we should always pass keys.
""" g= "name" in d2
print(g) """

#Iteration operations #only keys will be traversed.
""" d1 = {"name":"Rashmi" , "age":"22" , "gender":"female" , "id":"1234"}
for i in d1:
    print(i) """

#want to print key along with values
""" d1 = {"name":"Rashmi" , "age":"22" , "gender":"female" , "id":"1234"}
for i in d1:
    print(i, d1[i])
 """

#Dictionary functions
#len()
""" d1 = {"name":"Rashmi" , "age":"22" , "gender":"female" , "id":"1234"} """
""" len = len(d1)
print(len) """
#sorted
""" sort = sorted(d1)
print(sort) """
#min #max
""" min = min(d1)
print(min)
max = max(d1)
print(max) """

#items/keys/values
""" items = d1.items()
print(items)

key = d1.keys()
print(key)

value = d1.values()
print(value) """

#Update
""" d1 = {"name":"Rashmi" , "age":"22" , "gender":"female" , "id":"1234"}
d2 = {"name":"payal", "sem":4}

d1.update(d2)
print(d1) """

#Dictionary Comprehension
# {key:value for vars in iterable}


#print numbers as keys and their squares as values
""" d3 = {i:i**2 for i in range(1,11)}
print(d3) """

#convert km distance into miles from an existing dictionary
""" d6 = {"mumbai":1000, "delhi":2000 , "bangalore":3000}
miles = {i:j*0.62 for i,j in d6.items()}
print(miles) """

#zip
""" days = ["Sunday" , "monday", "tuesday", "wednesday", "thursday", "friday" "saturday"]
temp = [27,28,36,45,25,29,42]
a = {i:j for (i,j) in zip(days,temp)}
print(a) """

#using if condition
""" products = {"iphone":10, "samsung": 0, "vivo": 2}
b = {i:j for (i,j) in products.items() if j!=0}
print(b) """

#nested compregension
#print tables from 2 to 4

table= {i:{j:i*j for j in range(1,11)} for i in range(2,5)}
print(table)
