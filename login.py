email = input("Enter your email: ")
password = input("Enter your password: ")

if email == "Rash2@gmail.com" and password == "1234":
    print("Login successful!")

elif email == "Rash2@gmail.com" and password != "1234":
    print("Incorrect password. Please try again.")  

    password = input("Enter your password: ")
    if password == "1234":
        print("Login successful!")
    else:
        print("Incorrect password. Please try again.")   
        
else:   print("Invalid email or password. Please try again.")   