#reduce using functools library
import functools

a = functools.reduce(lambda x,y: x+y , [1,2,3,4,5])
print(a)

#findmax

a = functools.reduce(lambda x,y: x if x>y else y, [15,654,789654,3456,454356])
print(a)