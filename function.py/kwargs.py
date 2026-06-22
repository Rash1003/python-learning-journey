#kwargs forms a dictionary with key value pairs 
#KWARGS

def capital(**kwargs):
    for (key,value) in kwargs.items():
        print(key, "->" , value)

capital(india = "delhi", pakistan = "islamabad", nepal = "kathmandu")
