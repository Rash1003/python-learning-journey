# current population is 10000 and it is decreasing by 10% every year. list the population of last ten years

#curr_pop = 10000

#for i in range (10 ,0, -1):
#    print(i, curr_pop)
#    curr_pop = curr_pop/1.1


# SEQUENCE SUM of the n numbers in series 1/1! + 2/2! + 3/3! + 4/4! + 5/5! + 6/6! ........ + n/n!

#n = int(input("Enter the number: "))

#result = 0 
#fact = 1

#for i in range(1 , n+1):
#    fact = fact*i
#    result = result + i/fact
#print(result)

#rows = int(input("Enter number of rows:"))
#star = "*"


#for i in range (1, rows+1):
 #   print( star * i)


#print something like 
#1
#121
#12321
#1234321


#row = int(input("Enter number of rows:"))

#for i in range(1,row+1):
#    for j in range(1, i+1):
#        print(j, end="")
#    for k in range(i-1, 0, -1):
#        print(k, end="")    
#    print()


rows = int(input("Enter number of rows:"))

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end="")

    print()


