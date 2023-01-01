import sys # sys is part of the Python standard library. Used primary in this script to exit the banking system. 

def main():
    base = True
    a = True 
    b = True 
    c = True
    d = True 
    e = True 
    f = True

    print(' ')
    print('Welcome to the UOB banking system.')
    BankingSystemInstance = BankingSystem()

    while base: 
        a = True
        b = True
        c = True 
        e = True

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
                    print('Currently, there are no registered accounts available for you to access.') 
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
                c = True
                e = True
                
                while c:
                    decision = input('Enter choice: ')

                    if decision.isnumeric() == False: 
                        print(' ')
                        print('The entered value is not a valid option, please try again.')
                        print('The login and return to the main menu, please press 3. ')
                        break 
                    
                    if int(decision) == 1:
                        customer.create_wallet()
                        break

                    elif int(decision) == 2:
                        if len(customer.wallets) ==0:
                            print(' ')
                            print('Currently, there are no active wallets associated with your account.') 
                            print('In order to proceed, first create a wallet.')
                            print(' ')

                            break 
                        
                    elif int(decision) == 3: 
                        print(' ')
                        print(f'Logging out of the account of username: {customer.username}')
                        print('Returning to main menu now...')

                        a = False
                        b = False
    
                        break 

                    elif int(decision) == 4: 

                        while d:
                            delete = BankingSystemInstance.del_account(customer)

                            if delete == True: 
                                
                                a = False
                                b = False
                                c = False
                                e = False # This must be added to ensure while loop E is not mistakenly run afterwards. 
                                break

                            
                            elif delete == False:
                                
                                c = False
                                e = False # This must be added to ensure while loop E is not mistakenly run afterwards. 
                                break
                        
                        


            
                    while e: 
                        BankingSystemInstance.walletm_display(customer)
                        
                        while f:
                            decision = input('Enter choice: ')

                            if decision.isnumeric() == False:  
                                print(' ')
                                print('Returning to customer menu...')
                                
                                e = False
                                c = False
                                break 

                            if int(decision) == 1:
                                customer.select_wallet()
                                

                            elif int(decision) == 2:
                                wallet = customer.select_wallet()
                                wallet.deposit()
                                break
                                
                            elif int(decision) == 3: 
                                wallet = customer.select_wallet()
                                wallet.withdraw()
                                break 

                            else: 
                                print(' ')
                                print('Returning to customer menu...')
                                
                                e = False
                                c = False
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
            wallet_name = input('Please enter a name for your wallet: ').rstrip()
            
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
            self.wallets[wallet_name] = DailyUseWallet(wallet_id, wallet_name) # wallet_type is also defined as a static attribute.
            print(' ')
            print(f'A Daily Use wallet of the name: {wallet_name}, has been created.')
            print(f'This created wallet has the ID: {wallet_id}')
            print(' ')
            print(f'Returning to customer page of user: {self.username}...')
            print(' ')
            #print(self.wallets[wallet_name].wallet_type)


        elif wallet_type == 2:
            self.wallets[wallet_name] = SavingsWallet(wallet_id, wallet_name) # wallet_type is also defined as a static attribute.
            print(' ')
            print(f'A Savings wallet of the name: {wallet_name}, has been created.')
            print(f'This created wallet has the ID: {wallet_id}')
            print(' ')
            print(f'Returning to customer page of user: {self.username}...')
            print(' ')
            #print(self.wallets[wallet_name].wallet_type)


        elif wallet_type == 3:
            self.wallets[wallet_name] = HolidaysWallet(wallet_id, wallet_name) # wallet_type is also defined as a static attribute. 
            print(' ')
            print(f'A Holidays wallet of the name: {wallet_name}, has been created.')
            print(f'This created wallet has the ID: {wallet_id}')
            print(' ')
            print(f'Returning to customer page of user: {self.username}...')
            print(' ')
            #print(self.wallets[wallet_name].wallet_type)


                
        elif wallet_type == 4:
            self.wallets[wallet_name] = MortgageWallet(wallet_id, wallet_name) # wallet_type is also defined as a static attribute. 
            print(' ')
            print(f'A Mortgage wallet of the name: {wallet_name}, has been created.')
            print(f'This created wallet has the ID: {wallet_id}')
            print(' ')
            print(f'Returning to customer page of user: {self.username}...')
            print(' ')
            #print(self.wallets[wallet_name].wallet_type)
        



    def delete_wallet(self, wallet_name):
            """Delete a wallet with a given name."""
            if wallet_name not in self.wallets:
                raise ValueError("A wallet with this name does not exist")
            del self.wallets[wallet_name]


    
    def select_wallet(self):

        """Display all available wallets and allow the user to select one by number."""
        print("\n========= Wallet selection menu ==========")
        print(f'Welcome to the wallet selection menu, user {self.username}.')
        print('Please select one of the available wallets by entering its number.')
        print(' ')
        print('Available wallets:')
        for i, (name, wallet) in enumerate(self.wallets.items()):
            print(f"{i+1}. {wallet.wallet_id}, {wallet.wallet_type} wallet of name: {name}")
        print(' ')

        # Prompt the user to select a wallet
        while True:
            selection = input('Enter a number to select a wallet: ')
            try:
                selection = int(selection)
                if 1 <= selection <= len(self.wallets): # Has to greater than or equal to 1 as that's the first specified option, and less than or equal to the available wallets. 
                    # Get the wallet name and wallet object corresponding to the selected number
                    wallet_name, wallet = list(self.wallets.items())[selection-1]
                    return wallet
                else:
                    print("Invalid selection. Please enter a number corresponding to one of the available wallets.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")







class BankingSystem(): 
    
    def __init__(self):

        self.system_account = 0 # Transaction fees start at zero for every run of the program. 
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

        print(' ')
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
                print('The login details provided are incorrect, as they do not match any registered account on our system.')
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
        ======= Customer account menu for user: {customer.username} =======
        
            1. Create a wallet
            2. Manage active wallets 
            3. Log out of account and return to main menu
            4. Close account
            
            """)
        


    def walletm_display(self, customer):
        print(f"""
        ======= Wallet management menu for user: {customer.username} =======
        
            1. Display detials and properties of active wallets
            2. Deposit to wallet
            3. Withdraw from wallet
            4. Local transfer between owned wallets
            5. Global transfer to another customer's wallet
            6. Delete a wallet
            
            or enter any other key to exit
            and return to the customer menu
            """)




    def terminate(self): 
        print(' ')
        print('You have chosen to exit the UOB banking system.')
        print('Thank you for your patronage, we hope to see you again soon!')
        print(' ')
        
        sys.exit()








    def del_account(self, customer): 


        print(' ')
        print('If your account is closed, all account information, including any created wallets will be lost.')
        print('Please enter Y/y, for Yes and N/n, for No.')
        print(' ')
        confirmation = input(f'{customer.username}, are sure you want to close your account?')

        if confirmation.isnumeric() == True: 
            print(' ')
            print('The entered value is not a valid option, please try again.')
            print('The login and return to the main menu, please press 3. ')
            
        elif confirmation.lower() == 'y':
            print(' ')
            print(f'The account of username: {customer.username}, has been closed.')
            del(self.customers[customer.username])
            print('Now returning to main menu...')

            return True
            

        elif confirmation.lower() == 'n':
            print(' ')
            print(f'The deletion of the account with username: {customer.username}, has been cancelled.')
            print(f'Now returning to customer menu...')
            
            return False


        else: 
            print(' ')
            print('The value provided is not a valid option.')
            print('Please look at the available options and try again.')
            print(' ')
            print(' ')







class Wallet():

    last_transaction = None

    def __init__(self, wallet_id, wallet_name):
        self.balance = 0  # Initial balance is 0
        self.wallet_id = wallet_id
        self.wallet_name = wallet_name

    # All wallets have a deposit feature, so this deposit method will be inherited for all wallet types. 
    def deposit(self):
        while True:
            try:
                print('If you have changed your mind about depositing to this wallet, enter any letter or character to return to the previous page.')
                amount = float(input('Enter the amount you would like to deposit: '))
                if amount > 0:
                    self.balance += amount
                    self.last_transaction = 'deposit' # Changing what the nature of the last transaction with to deposit. 
                    print(f'Successfully deposited {amount} into your wallet.')
                    break
                else:
                    print('Invalid input. Please enter a positive number.')
            except ValueError:
                print('Returning to wallet management page...')
                break


class DailyUseWallet(Wallet):
    wallet_type = 'Daily Use' 

    def withdraw(self):
            # Check if the wallet's balance is equal to 0
        if self.balance == 0:
            print('Sorry, you cannot withdraw from a wallet with a balance of 0.')
            return
        
        while True:
            try:
                print('If you have changed your mind about withdrawing from this wallet, enter any letter or character to return to the previous page.')
                amount = float(input('Enter the amount you would like to withdraw: '))
                if amount > 0:
                    if self.balance >= amount: # Check if balance is sufficient for withdrawal
                        self.balance -= amount
                        self.last_transaction = 'withdraw' # Changing what the nature of the last transaction with to withdraw. 
                        print(f'Successfully withdrawn {amount} from your wallet.')
                        break
                    else:
                        print('Insufficient balance to make this withdrawal. Please enter a different amount.')
                else:
                    print('Invalid input. Please enter a positive number.')
            except ValueError:
                print('Returning to wallet management page...')
                break


    def transfer(self, amount, other_wallet):
        """Transfer a given amount of money to another wallet."""
        self.withdraw(amount)
        other_wallet.deposit(amount)

    def transfer_to_customer(self, amount, customer, customer_wallet_name):
        """Transfer a given amount of money to another customer's wallet."""
        self.withdraw(amount)
        customer.wallets[customer_wallet_name].deposit(amount)



class SavingsWallet(Wallet):
    wallet_type = 'Savings'

    def __init__(self, wallet_id, wallet_name):
        super().__init__(wallet_id, wallet_name)
        
         
    def withdraw(self):

        if self.balance == 0:
            print('Sorry, you cannot withdraw from a wallet with a balance of 0.')
            return

        while True:
            try:
                print('If you have changed your mind about withdrawing from this wallet, enter any letter or character to return to the previous page.')
                amount = float(input('Enter the amount you would like to withdraw: '))
                if amount > 0:
                    if self.balance >= amount: # Check if balance is sufficient for withdrawal
                        self.balance -= amount
                        self.last_transaction = 'withdraw' # Changing what the nature of the last transaction with to withdraw. 
                        print(f'Successfully withdrawn {amount} from your wallet.')
                        break
                    else:
                        print('Insufficient balance to make this withdrawal. Please enter a different amount.')
                else:
                    print('Invalid input. Please enter a positive number.')
            except ValueError:
                print('Returning to wallet management page...')
                break




class HolidaysWallet(DailyUseWallet):
    wallet_type = 'Holidays' 
    
    # Holiday wallets have all the same functionality as Daily Use Wallets. 
    # Meaning a error can be raised for the unwanted method, and it can be considered a Holiday wallet. 
    def transfer_to_customer(self, amount, recipient, wallet_name):
        """Transfer a given amount of money to another customer's wallet."""
        raise ValueError("Holidays wallets cannot be used to transfer funds to other customers")



class MortgageWallet(Wallet): 
    wallet_type = 'Mortgage' 

    # The mortgage wallet has the same functionality as the base Wallet class. 
    # So no additional functions need to be inherited. 
    pass 


main()
