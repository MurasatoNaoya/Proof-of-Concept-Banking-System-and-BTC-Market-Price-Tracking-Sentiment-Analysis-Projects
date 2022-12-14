
def main():
    while (True): 
        BankingSystemInstance = BankingSystem(transaction_fees = 0, customers = {})
        BankingSystemInstance.main_display()
        while (True):
            decision = input("Enter choice: ")


            if (int(decision)==1):
            
                BankingSystemInstance.create_account()
                
                break

            else: 
                print('You didnt input 1!')
                break 











class Customer(): 

    # Defining a constructor that instantiaties consumer objects. 
    def __init__(self, first_name, last_name, COR, age, email, password, username): 
        self.first_name = first_name
        self.last_name = last_name
        self.COR = COR
        self.age = age 
        self.email = email
        self.password = password
        self.username = username 





class BankingSystem(): 

    
    
    def __init__(self, transaction_fees, customers):

        self.transaction_fees = transaction_fees
        self.customers = customers


    def main_display(self):  # Displaying the initial text-based screen, where the customer will see their inital options. 

        print("""
                ======= UOB Banking System =======
                  1. Create an account
                  2. Access an existing account
                  
                  or enter any other key to exit
                  """)


    def create_account(self):

        print('To create an account, you will need to provide the following details:')
        print('First name, last name, country of residence, age, email, password and username')

        first_name = input('Please enter your first name:')
        last_name = input('Please enter your last name:')
        CofR = input('Please enter your country of residence:')
        age = input('Please enter your age / how old you are:')
        email = input('Please enter your email:')
        password = input('Please enter your password')
        username = input('And finally, please enter your username:')
        
        new_customer = Customer(first_name, last_name, CofR, age, email, password, username)
        self.customers.update({new_customer.username : new_customer})
        print(f'Customer of username {new_customer.username} your banking account has been successfully created.')
        print('=====================================================================================')
        print('To access to your account, please first login using the 2nd option of the menu below.')
        print('Alternatively, you can choose the 1st option again to create another account. ')














"""def create_wallet():

        pass


    #def delete_wallet(): 
#        pass

    
    def log_in(): 
        pass 


    def log_out():
        pass

    

    def deposit(): 
        pass
        
        input('How much would you like to withdraw?')

    
    def transfer(): 
        pass

 """


main()