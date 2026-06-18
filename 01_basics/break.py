lower = int(input("Enter lower limit:"))
upper = int(input("Enter upper limit:"))

for i in range(lower , upper +1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i)
