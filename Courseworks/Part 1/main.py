import sys # sys is part of the Python standard library. Used primary in this script to exit the banking system. 

def main():
    base = True
    a = True 
    b = True 
    c = True

    BankingSystemInstance = BankingSystem()

    while base: 
        a = True
        BankingSystemInstance.main_display()

        while a:
            decision = input("Enter choice: ")
          
            if decision.isnumeric() == False: 
                BankingSystemInstance.terminate()
                
            
            elif int(decision) == 1:
                BankingSystemInstance.create_account()
                
                break

            elif int(decision) == 2: 
                if len(BankingSystemInstance.customers) == 0:
                    print(' ')
                    print('Currently, there are no available accounts for you to access.') 
                    print('Please create an account first, in order to proceed.')
                    print(' ')
                    break
                
                customer = BankingSystemInstance.login_screen()

                if customer == None: 
                    break

            else: 
                BankingSystemInstance.terminate()

                          
            while b:
                BankingSystemInstance.customer_display(customer)
                
                decision = input('Enter choice: ')

                if decision.isnumeric() == False: 
                    print(' ')
                    print('Please enter a valid options provided on the customer page.')

                if int(decision) == 1:
                    customer.create_wallet()
                

                elif int(decision) == 2:
                    break # Functionality not added yet. 

                else: 
                    print(' ')
                    print(f'Thank you, {customer.username}.')
                    print('Returning to main menu now...')

                    a = False
                    break 
                
            






class Customer(): 

    # Defining a constructor that instantiaties consumer objects. s
    def __init__(self, first_name, last_name, COR, age, email, username, password): 
        self.first_name = first_name
        self.last_name = last_name
        self.COR = COR
        self.age = age 
        self.email = email
        self.username = username 
        self.password = password

        self.wallets = {} # Empty dictionary where wallet objects created by the user are stored. 
        self.wallet_id = 0  # Initialise the wallet_id counter to 0
        self.wallet_valid = [1, 2, 3, 4]



    def create_wallet(self):

        
        """Create a new wallet with a given name and type."""
        
        print("\n========= Wallet creation menu ==========")
        print(f'Welcome to the wallet creation menue, user {self.username}.')
        print('Please select one of the options to create a wallet for your specific needs.')
        print(' ')
        print('Available wallet types - ')
        print("1. Daily use ")
        print("2. Savings ") 
        print("3. Holidays ")
        print("4. Mortgage ") 
        print(' ')
    
        while True:
            try:
                wallet_type = input('Please select the type of wallet you would like by entering one of the numbers above: ')
                wallet_type = int(wallet_type)
                if wallet_type in self.wallet_valid: 
                    break
                else:
                    print(' ')
                    print("An invalid wallet type as been selected, please try again or return to the account menu.")
                    print(' ')
            except ValueError:
                print(' ')
                print("An invalid input has been entered, please try again or return to the account menu.")
                print(' ')


        while True:
            wallet_name = input('Please enter a name for your wallet: ')
            
            if wallet_name in self.wallets: 
                print(' ')
                print("A wallet with this name already exists, please try a different name.")
                print(' ')

            else: 
                break
        
        self.wallet_id += 1
        wallet_id = f"{self.wallet_id:03d}"  # Format the wallet_id as a 3-digit string (e.g. 001, 002, etc.)
        # Create the appropriate type of wallet based on the provided type


        if wallet_type == 1:
            self.wallets[wallet_name] = DailyUseWallet(wallet_id)
            print(' ')
            print(f'A daily use wallet of the name: {wallet_name} has been created.')
            print(f'This created wallet has the ID: {wallet_id}')
            print(' ')
            print(f'Returning to customer page of user: {self.username} now...')
            print(' ')


        elif wallet_type == 2:
            self.wallets[wallet_name] = SavingsWallet(wallet_id)
            print(' ')
            print(f'A savings wallet of the name: {wallet_name} has been created.')
            print(f'This created wallet has the ID: {wallet_id}')
            print(' ')
            print(f'Returning to customer page of user: {self.username} now...')
            print(' ')



        elif wallet_type == 3:
            self.wallets[wallet_name] = HolidaysWallet(wallet_id)
            print(' ')
            print(f'A holidays wallet of the name: {wallet_name} has been created.')
            print(f'This created wallet has the ID: {wallet_id}')
            print(' ')
            print(f'Returning to customer page of user: {self.username} now...')
            print(' ')


                
        elif wallet_type == 4:
            self.wallets[wallet_name] = MortgageWallet(wallet_id)
            print(' ')
            print(f'A mortgage wallet of the name: {wallet_name} has been created.')
            print(f'This created wallet has the ID: {wallet_id}')
            print(' ')
            print(f'Returning to customer page of user: {self.username} now...')
            print(' ')

        
        







    def delete_wallet(self, wallet_name):
            """Delete a wallet with a given name."""
            if wallet_name not in self.wallets:
                raise ValueError("A wallet with this name does not exist")
            del self.wallets[wallet_name]









class BankingSystem(): 
    
    def __init__(self):

        self.transaction_fees = 0 # Transaction fees start at zero for every run of the program. 
        self.customers = {} # Empty dictionary to store customer objects. 


    def main_display(self):  # Displaying the text-based screen, where the customer will see their inital options. 

        print("""
                ======= UOB Banking System =======
                
                  1. Create an account
                  2. Access an existing account
                  
                  or enter any other key to exit
                  """)



    def create_account(self):

        print('To create an account, you will need to provide the following details:')
        print('First name, last name, country of residence, age, email, password and username')
        print(' ')
        first_name = input('Please enter your first name: ')
        last_name = input('Please enter your last name: ')
        CofR = input('Please enter your country of residence: ')
        age = input('Please enter your age / how old you are: ')
        email = input('Please enter your email: ')
        username = input('And finally, please enter your username: ').rstrip() # Appiled such that an accidential white space does not
        password = input('Please enter your password: ').rstrip()              # trigger an incorrect password. 
        
        new_customer = Customer(first_name, last_name, CofR, age, email, username, password)
        self.customers[new_customer.username] =  new_customer

        print('=====================================================================================')
        print(f'Customer of username {new_customer.username}, your banking account has been successfully created.')
        # print(f'{new_customer.username} and {new_customer.password}')
        print('To access to your account, please first login using the 2nd option of the menu below.')
        print('Alternatively, you can choose the 1st option again to create another account. ')


    def login_screen(self):
        while True:

            # Get the input for the login credentials
            print(' ')
            print('======== Login to account ========')
            username = input('Enter your username: ').rstrip() # Appiled such that an accidential white space does not
            password = input('Enter your password: ').rstrip() # trigger an incorrect password. 
    

            # Attempt to login with the provided credentials
            try:
                customer = self.login_check(username, password)
            except ValueError:
                # Print an error message if the login fails
                print(' ')
                print('The login details provided are incorrect, as they do not match any account on our system.')
                print('Returning to main menu..')
                break

            else:
                # If the login is successful, break out of the loop and return the customer object
                print(' ')
                print(f"Login successful, welcome {username}.") 
                
                return customer



    def login_check(self, username, password):
        """Verify the provided credentials and return the customer object for the logged in user."""

        if username not in self.customers:
            raise ValueError("Unfortunately, an account with this username does not exist, please try again or exit this page.")

        if self.customers[username].password != password:
            raise ValueError("Incorrect password, please try again.")
        
        return self.customers[username] # This returns the customer object for the checked username. 


    

    def customer_display(self, customer): 
        print(f"""
        ======= Account page for user: {customer.username} =======
        
            1. Create a wallet
            2.) Manage active wallets 
            
            or enter any other key to exit
            """)
        


    def terminate(self): 
        print(' ')
        print('You have chosen to exit the UOB banking system.')
        print('Thank you for your patronage, we hope to see you again soon!')
        print(' ')
        
        sys.exit()















class Wallet():
    def __init__(self, wallet_id):
        self.balance = 0  # Initial balance is 0
        self.wallet_id = wallet_id

    # All of the wallets have a deposit method, so this can be inherited for all variations. 
    def deposit(self, amount):
        """Deposit a given amount of money into the wallet."""
        self.balance += amount
        


class DailyUseWallet(Wallet):
    def withdraw(self, amount):
        """Withdraw a given amount of money from the wallet."""
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def transfer(self, amount, other_wallet):
        """Transfer a given amount of money to another wallet."""
        self.withdraw(amount)
        other_wallet.deposit(amount)

    def transfer_to_customer(self, amount, customer, customer_wallet_name):
        """Transfer a given amount of money to another customer's wallet."""
        self.withdraw(amount)
        customer.wallets[customer_wallet_name].deposit(amount)



class SavingsWallet(Wallet):
    def withdraw(self, amount):
        """Withdraw a given amount of money from the wallet."""
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount



class HolidaysWallet(DailyUseWallet):
    
    # Holiday wallets have all the same functionality as Daily Use Wallets. 
    # Meaning a error can be raised for the unwanted method, and it can be considered a Holiday wallet. 
    def transfer_to_customer(self, amount, recipient, wallet_name):
        """Transfer a given amount of money to another customer's wallet."""
        raise ValueError("Holidays wallets cannot be used to transfer funds to other customers")



class MortgageWallet(Wallet):
    # The mortgage wallet has the same functionality as the base Wallet class. 
    # So no additional functions need to be inherited. 
    pass 











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
