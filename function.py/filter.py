#filters the values from the list

L = [2,4,7,8,9,6]
a = list(filter(lambda x: x>5 , L))
print(a)

#words starting from a
L = ["apple","arrow","bat","cat","ant","fun"]
a = list(filter(lambda s: s.startswith("a"), L))
print(a)