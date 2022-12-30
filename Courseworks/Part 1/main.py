
def main():

    BankingSystemInstance = BankingSystem()
    while (True): 

        BankingSystemInstance.main_display()

        while (True):
            decision = input("Enter choice: ")

            if int(decision) == 1:
                BankingSystemInstance.create_account()
                
                break

            elif int(decision) == 2: 
                BankingSystemInstance.login_screen()
                
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


    def create_wallet(self, wallet_name, wallet_type):
        """Create a new wallet with a given name and type."""
        if wallet_name in self.wallets:
            raise ValueError("A wallet with this name already exists")
        # Create the appropriate type of wallet based on the provided type
        if wallet_type == "daily_use":
            self.wallets[wallet_name] = DailyUseWallet()
        elif wallet_type == "savings":
            self.wallets[wallet_name] = SavingsWallet()
        elif wallet_type == "holidays":
            self.wallets[wallet_name] = HolidaysWallet()
        elif wallet_type == "mortgage":
            self.wallets[wallet_name] = MortgageWallet()
        else:
            # None of the inputted names match a wallet type. 
            # A ValueError is returned until a valid wallet name is inputted. 
            raise ValueError("Invalid wallet type")


    def delete_wallet(self, wallet_name):
            """Delete a wallet with a given name."""
            if wallet_name not in self.wallets:
                raise ValueError("A wallet with this name does not exist")
            del self.wallets[wallet_name]



class BankingSystem(): 

    
    
    def __init__(self):

        self.transaction_fees = 0 # Transaction fees start at zero for every run of the program. 
        self.customers = {} # Empty dictionary to store customer accounts. 


    def main_display(self):  # Displaying the text-based screen, where the customer will see their inital options. 

        print("""
                ======= UOB Banking System =======
                  1. Create an account
                  2. Access an existing account
                  
                  or enter any other key to exit
                  """)


    def login_screen(self):
        while True:
            # Print the menu options
            print("\nMenu Options:")
            print("1. Login using a username and password.")
            print("2. Quit, and return to main menue.")

            # Get the user's choice
            choice = int(input("Enter your choice: "))

            # Perform the appropriate action based on the user's choice
            if choice == 1:
                # Get the input for the login credentials
                username = input("Enter your username: ")
                password = input("Enter your password: ")

                # Attempt to login with the provided credentials
                try:
                    customer = self.login_check(username, password)
                except ValueError:
                    # Print an error message if the login fails
                    print('The login details provided are incorrect.')
                else:
                    # If the login is successful, break out of the loop and return the customer object
                    print("Login successful")
                    return customer
                    

            elif choice == 2:
                # Break the while loop and return to the main page. 
                print("Exiting login screen and returning to the main page..")

                break
            else:
                # Print an error message if an invalid choice is entered
                print("Invalid choice. Please try again.")

        











    def login_check(self, username, password):
        """Verify the provided credentials and return the customer object for the logged in user."""

        if username not in self.customers:
            raise ValueError("Unfortunately, an account with this username does not exist, please try again or exit this page.")

        if self.customers[username].password != password:
            raise ValueError("Incorrect password, please try again.")
        
        return self.customers[username]


        





    def create_account(self):

        print('To create an account, you will need to provide the following details:')
        print('First name, last name, country of residence, age, email, password and username')
        print(' ')
        first_name = input('Please enter your first name: ')
        last_name = input('Please enter your last name: ')
        CofR = input('Please enter your country of residence: ')
        age = input('Please enter your age / how old you are: ')
        email = input('Please enter your email: ')
        username = input('And finally, please enter your username: ')
        password = input('Please enter your password: ')
        
        new_customer = Customer(first_name, last_name, CofR, age, email,username, password)
        self.customers[new_customer.username] =  new_customer

        print('=====================================================================================')
        print(f'Customer of username {new_customer.username}, your banking account has been successfully created.')
        print('To access to your account, please first login using the 2nd option of the menu below.')
        print('Alternatively, you can choose the 1st option again to create another account. ')








class Wallet:
    def __init__(self):
        self.balance = 0  # Initial balance is 0

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
