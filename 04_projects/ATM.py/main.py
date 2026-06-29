class Atm:                                  #USER DEFINED CLASS
    def __init__(self):                     #this is a Constructor
        self.pin = ''                       #these two are variables
        self.balance = 0
        self.menu()
        
    def menu(self):
        user_input = input("""
        1. press 1 to create pin
        2. press 2 to change pin
        3. press 3 to check balance
        4. press 4 to withdraw
        5. press anything else to exit
        """)

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.change_pin()
        elif user_input == "3":
            self.check_balance()
        elif user_input == "4":
            self.withdraw()
        else:
            exit()
    
    def create_pin(self):
        user_pin = input("create your pin:")
        self.pin = user_pin

        user_balance = int(input("enter your balance:"))
        self.balance = user_balance

        print("pin created succesfully")
        self.menu()

    def change_pin(self):
        old_pin = input("Enter old pin:")

        if old_pin == self.pin:
            new_pin = input("Enter new pin:")
            self.pin = new_pin
            print("Changed pin successfully")
            self.menu()
        else:
            print("Incorrect pin! try again.")
            self.change_pin()

    def check_balance(self):
        a = input("enter your pin:")
        if a == self.pin:
            print("Your balance is:" , self.balance)
            self.menu()    
        else:
            print("Incorrect pin! Try again")
            self.menu()

    def withdraw(self):
        a = input("Enter your pin:")
        if a == self.pin:
            amount = int(input("Enter your amount:" ))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Thankyou. Cash withdrawn succesfully! Your balance is:" , self.balance)
                
            else:
                print("Gareeb")
                
        else:
            print("Incorrect pin! Try Again.")
            self.withdraw()
        self.menu()
        

obj = Atm()
