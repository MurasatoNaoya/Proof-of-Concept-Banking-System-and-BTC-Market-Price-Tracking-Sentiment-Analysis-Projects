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
                
                CustomerInstance = BankingSystemInstance.login_screen()

                if CustomerInstance == None: 
                    break

            else: 
                BankingSystemInstance.terminate()

                          
            while b:
                BankingSystemInstance.customer_display(CustomerInstance)
                c = True
                e = True
                
                while c:
                    decision = input('Enter choice: ')

                    if decision.isnumeric() == False: 
                        print(' ')
                        print('The entered value is not a valid option, please try again.')
                        break 
                    
                    if int(decision) == 1:
                        CustomerInstance.create_wallet()
                        break

                    elif int(decision) == 2:
                        if len(CustomerInstance.wallets) ==0:
                            print(' ')
                            print('Currently, there are no active wallets associated with your account.') 
                            print('In order to proceed, first create a wallet.')
                            print(' ')

                            break 
                        
                    elif int(decision) == 3: 
                        print(' ')
                        print(f'Logging out of the account of username: {CustomerInstance.username}')
                        print('Returning to main menu now...')

                        a = False
                        b = False
    
                        break 

                    elif int(decision) == 4: 

                        while d:
                            delete = BankingSystemInstance.del_account(CustomerInstance)

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
                        BankingSystemInstance.walletm_display(CustomerInstance)
                        
                        while f:
                            decision = input('Enter choice: ')

                            if decision.isnumeric() == False:  
                                print(' ')
                                print('Returning to customer menu...')
                                
                                e = False
                                c = False
                                break 

                            if int(decision) == 1:
                                CustomerInstance.display_wallets()
                                break

                                

                            elif int(decision) == 2:
                                wallet = CustomerInstance.select_wallet()
                                wallet.deposit()
                                break
                                
                            elif int(decision) == 3: 
                                wallet = CustomerInstance.select_wallet()
                                
                                try: 
                                    wallet.withdraw()
                                    break 
                                
                                except AttributeError:
                                    print(' ')
                                    print(f'As the selected wallet is of type "{wallet.wallet_type}", it does not support withdraw functionality.')
                                    print('If you would like to withdraw from a wallet, please create either a "Daily Use" or "Savings" wallet instead. ')
                                    print(' ')
                                    print('Returning to wallet management menu...')
                                    break
                                
                            elif int(decision) == 4:
                                # Transfer between customer's local wallets.
                                try:
                                    print(' ')
                                    print('Please select your source wallet; the wallet you are sending an amount from.')
                                    wallet = CustomerInstance.select_wallet() # Defining the souce wallet to send funds from. 
                                    wallet.transfer_amount(CustomerInstance, BankingSystemInstance)
                                    break

                                except AttributeError:
                                    print(' ')
                                    print(f'As the selected source wallet is of type "{wallet.wallet_type}", it does not support local transfer functionality.')
                                    print('If you would like to transfer to a wallet, please use or create either a "Daily Use" or "Holidays" wallet instead.')
                                    print(' ')
                                    print('Returning to wallet management menu...')
                                    break


                            elif int(decision) == 5:
                                    # Transfer between customers, global wallets
                                try:
                                    if len(BankingSystemInstance.customers) ==1: 
                                        print('You are currently the only customer in our system, therefore global transfer is not possible at the moment.')
                                        break
                                    print('Please select the other user on our system you would like to tranfer an amount to - ')
                                    customer_reciever = BankingSystemInstance.select_customer(CustomerInstance)

                                    if len(customer_reciever.wallets) == 0:
                                        print('The selected customer does not have any active wallets to transfer to.')
                                        break

                                    print(' ')
                                    print(f'Customer of username: "{customer_reciever.username}", has been selected as the recipient for customer transfer.')

                                    wallet = CustomerInstance.select_wallet() # Defining the souce wallet to send funds from. 
                                    if wallet.wallet_type == 'Holidays':
                                        print(' ')
                                        print(f'As the selected source wallet is of type "{wallet.wallet_type}", it does not support global transfer functionality.')
                                        print('If you would like to transfer to the wallet of another customer, please use or create a "Daily Use" wallet instead.')
                                        print(' ')
                                        print('Returning to wallet management menu...')
                                        break

                                    wallet.transfer_to_customer(CustomerInstance, customer_reciever, BankingSystemInstance)
                                    break

                                except AttributeError:
                                    print(' ')
                                    print(f'As the selected source wallet is of type "{wallet.wallet_type}", it does not support global transfer functionality.')
                                    print('If you would like to transfer to the wallet of another customer, please use or create a "Daily Use" wallet instead.')
                                    print(' ')
                                    print('Returning to wallet management menu...')
                                    break

                            
                            elif int(decision) == 6: 
                                CustomerInstance.delete_wallet()
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
            print(f'A Daily Use wallet of the name: "{wallet_name}", has been created.')
            print(f'This created wallet has the ID: {wallet_id}')
            print(' ')
            print(f'Returning to customer page of user: {self.username}...')
            print(' ')
            #print(self.wallets[wallet_name].wallet_type)


        elif wallet_type == 2:
            self.wallets[wallet_name] = SavingsWallet(wallet_id, wallet_name) # wallet_type is also defined as a static attribute.
            print(' ')
            print(f'A Savings wallet of the name: "{wallet_name}", has been created.')
            print(f'This created wallet has the ID: {wallet_id}')
            print(' ')
            print(f'Returning to customer page of user: {self.username}...')
            print(' ')
            #print(self.wallets[wallet_name].wallet_type)


        elif wallet_type == 3:
            self.wallets[wallet_name] = HolidaysWallet(wallet_id, wallet_name) # wallet_type is also defined as a static attribute. 
            print(' ')
            print(f'A Holidays wallet of the name: "{wallet_name}", has been created.')
            print(f'This created wallet has the ID: {wallet_id}')
            print(' ')
            print(f'Returning to customer page of user: {self.username}...')
            print(' ')
            #print(self.wallets[wallet_name].wallet_type)


                
        elif wallet_type == 4:
            self.wallets[wallet_name] = MortgageWallet(wallet_id, wallet_name) # wallet_type is also defined as a static attribute. 
            print(' ')
            print(f'A Mortgage wallet of the name: "{wallet_name}", has been created.')
            print(f'This created wallet has the ID: {wallet_id}')
            print(' ')
            print(f'Returning to customer page of user: {self.username}...')
            print(' ')
            #print(self.wallets[wallet_name].wallet_type)
        

    
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
            print(' ')
            selection = input('Enter a number to select a corresponding wallet: ')
            print(' ')
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


    def display_wallets(self): 
        
        """Display all available wallets """
        print(f"\n========= All available wallets for user: {self.username} ==========")
        print(' ')
        for i, (name, wallet) in enumerate(self.wallets.items()):
            print(f'{i+1}. ID: {wallet.wallet_id}, Name: {wallet.wallet_name}, Wallet Type: "{wallet.wallet_type}", Balance: {wallet.balance}, Nature of last transaction: {wallet.last_transaction}')
        print(' ')
        answer = input('Enter any key to return the wallet management menu')

        if answer != None: 
            return



    def delete_wallet(self): 
        
        wallet = self.select_wallet()
        

        print(' ')

        while True:
            # Prompt the user to confirm if they want to transfer the required amount from this wallet
            print(' ')
            confirm = input(f'Are you sure you want to delete your waller of name: "{wallet.wallet_name}", [y/n]?')
            
            if confirm.isnumeric() == True: 
                # When a value other than Y/y or N/n is inputted.
                print(' ')
                print("The entered value is not valid, please try again ans answer with either y, or n.")


            elif confirm.lower() == 'y':
            
                del(self.wallets[wallet.wallet_name])   
                print(' ')
                print(f'Wallet of name: "{wallet.wallet_name}" has been deleted from your account.')

                return

            
            elif confirm.lower() == 'n':
                
                print(' ')
                print(f'The deletion of wallet with name: "{wallet.wallet_name}" has been cancelled.')
                
                return

            else:
                # When a value other than Y/y or N/n is inputted.
                print(' ')
                print("The entered value is not valid, please try again ans answer with either y, or n.")







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
        while True:
            first_name = input('Please enter your first name: ')
            if not first_name.strip():
                print("First name cannot be empty or consist only of whitespace characters.")
            else:
                break
        while True:
            last_name = input('Please enter your last name: ')
            if not last_name.strip():
                print("Last name cannot be empty or consist only of whitespace characters.")
            else:
                break
        while True:
            CofR = input('Please enter your country of residence: ')
            if not CofR.strip():
                print("Country of residence cannot be empty or consist only of whitespace characters.")
            else:
                break
        while True:
            age = input('Please enter your age / how old you are: ')
            if not age.strip():
                print("Age cannot be empty or consist only of whitespace characters.")
            else:
                break
        while True:
            email = input('Please enter your email: ')
            if not email.strip():
                print("Email cannot be empty or consist only of whitespace characters.")
            else:
                break
            
        while True:
            username = input('And finally, please enter your username: ').rstrip()
            if not username.strip():
                print("Username cannot be empty or consist only of whitespace characters.")
            elif username in self.customers: # Usernames must be unique. 
                print(f' The username: "{username}" is already taken. Please try another.')
            else:
                break

        while True:
            password = input('Please enter your password: ').rstrip()
            if not password.strip():
                print("Password cannot be empty or consist only of whitespace characters.")
            elif password in self.customers: # Passwords must also be unqiue. 
                print(f' The password: "{password}" is already taken. Please try another.')
            else:
                break

        new_customer = Customer(first_name, last_name, CofR, age, email, username, password)
        self.customers[new_customer.username] =  new_customer

        print(' ')
        print('=====================================================================================')
        print(f'Customer of username {new_customer.username}, your banking account has been successfully created.')
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
        
            1. Display details of active wallets
            2. Deposit to wallet
            3. Withdraw from wallet
            4. Local transfer between owned wallets
            5. Global transfer to another customer's wallet
            6. Delete a wallet
            
            or enter any other value to exit
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
            print('The1 value provided is not a valid option.')
            print('Please look at the available options and try again.')
            print(' ')
            print(' ')



    def select_customer(self, CustomerInstance):

        """Display all available customers and allow the user to select one by number."""
        print("\n========= Customer selection menu ==========")
        print(f'Welcome to the customer selection menu, user {CustomerInstance.username}.')
        print('Please select one of the available customers by entering its number.')
        print(' ')
        print('Available customers:')
        for i, (username, customer) in enumerate(self.customers.items()):
            if customer != CustomerInstance:
                # Do not display the currently logged in customer
                print(f"{i+1}. {customer.username}")
        print(' ')

        # Prompt the user to select a customer
        while True:
            print(' ')
            selection = input('Enter a number to select a corresponding customer: ')
            print(' ')
            try:
                selection = int(selection)
                if 1 <= selection <= len(self.customers): # Has to be greater than or equal to 1 as that's the first specified option, and less than or equal to the available customers. 
                    # Get the customer object corresponding to the selected number
                    customer = list(self.customers.values())[selection-1]
                    return customer
                else:
                    print("Invalid selection. Please enter a number corresponding to one of the available customers.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")















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
                    print(' ')
                    print(f'Successfully deposited {amount} into your wallet of name "{self.wallet_name}".')
                    break
                else:
                    print(' ')
                    print('Invalid input. Please enter a positive number.')
            except ValueError:
                print(' ')
                print(f'Deposit to wallet of name: "{self.wallet_name}" cancelled.')
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
                print(' ')
                print('If you have changed your mind about withdrawing from this wallet, enter any letter or character to return to the previous page.')
                amount = float(input('Enter the amount you would like to withdraw: '))
                if amount > 0:
                    if self.balance >= amount: # Check if balance is sufficient for withdrawal
                        self.balance -= amount
                        self.last_transaction = 'withdraw' # Changing what the nature of the last transaction with to withdraw. 
                        print(' ')
                        print(f'Successfully withdrawn {amount} from your wallet of name "{self.wallet_name}".')
                        break
                    else:
                        print(' ')
                        print('Insufficient balance to make this withdrawal. Please enter a more suitable amount.')
                else:
                    print(' ')
                    print('Invalid input. Please enter a positive number.')
            except ValueError:
                print(' ')
                print(f'Withdrawl from wallet of name: "{self.wallet_name}" cancelled.')
                print('Returning to wallet management page...')
                break



    def transfer_amount(self, customer, banking_system):
        # Prompt the user to select the destination wallet
        while True:
            print(' ')
            print('Please select your destination wallet; the wallet you are sending an amount to.')
            destination_wallet = customer.select_wallet()
            if destination_wallet != self:
                # Destination wallet is different from the source wallet, so the transfer can proceed
                break
            else:
                print("The source and destination wallets cannot be the same. Please select a different destination wallet.")

        while True:

            try:
                amount = float(input("Enter the amount you want to transfer: "))

                if amount == 0:
                    print('')
                    print('The provided input was invalid, please enter a non-zero amount to transfer.')
                    print(' ')


                elif amount > 0:
                    # Check if the current wallet has sufficient balance to complete the transaction
                    if amount <= self.balance:
                        # Transfer the amount
                        self.balance -= amount

                        # The fee applied to local transfers is 0.5%, sent to the banking system's 'system_account' attribute.
                        transaction_fee = amount * 0.005
                        banking_system.system_account += transaction_fee
                        
                        # The recipient only recieves 99.5% of the sent amount.
                        destination_wallet.balance += (amount - transaction_fee)

                        self.last_transaction = 'local transfer' # Change the nature of the last transaction to transfer
                        destination_wallet.last_transaction = 'local transfer' # Change the nature of the last transaction to transfer
                        print(f"Successfully transferred {amount - transaction_fee} to the selected wallet, post-fees (0.5% for local transfer.)")

                        
                        return 


                    else:
                        # The current wallet doesn't have sufficient balance to complete the transaction
                        # Check if any of the other wallets have sufficient balance
                        for wallet_name, wallet in customer.wallets.items():
                            #print('count')
                            # Skip the current wallet and the destination wallet
                            if wallet == self or wallet == destination_wallet:
                                continue

                            if amount <= wallet.balance:
                                # A wallet with sufficient balance has been found
                                while True:
                                    # Prompt the user to confirm if they want to transfer the required amount from this wallet
                                    print(' ')
                                    print('The selected wallet does not have sufficient balance, but sufficient funds were found in another of your wallets')
                                    confirm = input(f'Do you want to transfer {amount} from wallet of name: "{wallet_name}", [y/n]?')

                                    if confirm.isnumeric() == True: 
                                        # When a value other than Y/y or N/n is inputted.
                                            print("The entered value is not valid, please try again ans answer with either y, or n.")


                                    elif confirm.lower() == 'y':
                                        # Transfer the required amount from the found wallet
                                        wallet.balance -= amount

                                        # The fee applied to local transfers is 0.5%, sent to the banking system's 'system_account' attribute.
                                        transaction_fee = amount * 0.005
                                        banking_system.system_account += transaction_fee

                                        # The recipient only recieves 99.5% of the sent amount. 
                                        destination_wallet.balance += (amount - transaction_fee)

                                        wallet.last_transaction = 'local transfer' # Change the nature of the last transaction to transfer
                                        destination_wallet.last_transaction = 'local transfer' # Change the nature of the last transaction to transfer

                                        print(' ')
                                        print(f"Successfully transferred {amount - transaction_fee} to the selected wallet, post-fees (0.5% for local transfer..")
                                        print(' ')
                                        print('Returning to wallet management menu...')
                                        
                                        return


                                        

                                    elif confirm.lower() == 'n':
                                        print(' ')
                                        print(f'Wallet of name: "{wallet_name}" has been chosen to not be the mediary for this transfer.')
                                        print('Searching for other viable wallets to use as source wallet...')

                                        break


                                    else: 

                                        # When a value other than Y/y or N/n is inputted.
                                        print(' ')
                                        print("The entered value is not valid, please try again ans answer with either y, or n.")

                        else:
                            # No wallet contain enough funds to transfer
                            print(' ')
                            print("The defined source wallet has insufficent funds for this transaction")
                            print('And there are no other wallets associated with your account that can facilitate this transfer.')
                            print('Please deposit additional funds to one of your wallets or define a smaller amount in order to transfer to carry out this transaction.')
                            print(' ')
                            print('Returning to wallet management menu...')

                            return

            except ValueError:
                # The entered amount is not a number
                print(' ')
                print("Please enter a valid amount to transfer.")
                print(' ')






    def transfer_to_customer(self, customer_sender, customer_reciever, banking_system ):
# Prompt the user to select the destination wallet
        while True:
            print(' ')
            print('Please select your destination wallet; the wallet you are sending an amount to.')
            destination_wallet = customer_reciever.select_wallet()
            if destination_wallet != self:
                # Destination wallet is different from the source wallet, so the transfer can proceed
                break
            else:
                print("The source and destination wallets cannot be the same. Please select a different destination wallet.")

        while True:

            try:
                amount = float(input("Enter the amount you want to transfer: "))

                if amount == 0:
                    print('')
                    print('The provided input was invalid, please enter a non-zero amount to transfer.')
                    print(' ')


                elif amount > 0:
                    # Check if the current wallet has sufficient balance to complete the transaction
                    if amount <= self.balance:
                        # Transfer the amount
                        self.balance -= amount

                        # The fee applied to local transfers is 1.5%, sent to the banking system's 'system_account' attribute.
                        transaction_fee = amount * 0.015
                        banking_system.system_account += transaction_fee
                        
                        # The recipient only recieves 98.5% of the sent amount.
                        destination_wallet.balance += (amount - transaction_fee)

                        self.last_transaction = 'global transfer' # Change the nature of the last transaction to transfer
                        destination_wallet.last_transaction = 'global transfer' # Change the nature of the last transaction to transfer
                        print(f'Successfully transferred {amount - transaction_fee} to the selected wallet of customer: "{customer_reciever.username}", post-fees (1.5% for global transfer.')

                        
                        return 


                    else:
                        # The current wallet doesn't have sufficient balance to complete the transaction
                        # Check if any of the other wallets have sufficient balance
                        for wallet_name, wallet in customer_sender.wallets.items():
                            #print('count')
                            # Skip the current wallet and the destination wallet
                            if wallet == self or wallet == destination_wallet:
                                continue

                            if amount <= wallet.balance:
                                # A wallet with sufficient balance has been found
                                while True:
                                    # Prompt the user to confirm if they want to transfer the required amount from this wallet
                                    print(' ')
                                    print('The selected wallet does not have sufficient balance, but sufficient funds were found in another of your wallets')
                                    confirm = input(f'Do you want to transfer {amount} from wallet of name: "{wallet_name}", [y/n]?')

                                    if confirm.isnumeric() == True: 
                                        # When a value other than Y/y or N/n is inputted.
                                            print("The entered value is not valid, please try again ans answer with either y, or n.")


                                    elif confirm.lower() == 'y':
                                        # Transfer the required amount from the found wallet
                                        wallet.balance -= amount

                                        # The fee applied to local transfers is 1.5%, sent to the banking system's 'system_account' attribute.
                                        transaction_fee = amount * 0.015
                                        banking_system.system_account += transaction_fee

                                        # The recipient only recieves 98.5% of the sent amount. 
                                        destination_wallet.balance += (amount - transaction_fee)

                                        wallet.last_transaction = 'global transfer' # Change the nature of the last transaction to transfer
                                        destination_wallet.last_transaction = 'global transfer' # Change the nature of the last transaction to transfer

                                        print(' ')
                                        print(f'Successfully transferred {amount - transaction_fee} to the selected wallet of customer: "{customer_reciever.username}", post-fees (1.5% for global transfer..')
                                        print(' ')
                                        print('Returning to wallet management menu...')
                                        
                                        return


                                        

                                    elif confirm.lower() == 'n':
                                        print(' ')
                                        print(f'Wallet of name: "{wallet_name}" has been chosen to not be the mediary for this transfer.')
                                        print('Searching for other viable wallets to use as source wallet...')

                                        break


                                    else: 

                                        # When a value other than Y/y or N/n is inputted.
                                        print(' ')
                                        print("The entered value is not valid, please try again ans answer with either y, or n.")

                        else:
                            # No wallet contain enough funds to transfer
                            print(' ')
                            print("The defined source wallet has insufficent funds for this transaction")
                            print('And there are no other wallets associated with your account that can facilitate this transfer.')
                            print('Please deposit additional funds to one of your wallets or define a smaller amount in order to transfer to carry out this transaction.')
                            print(' ')
                            print('Returning to wallet management menu...')

                            return

            except ValueError:
                # The entered amount is not a number
                print(' ')
                print("Please enter a valid amount to transfer.")
                print('')





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
                print(' ')
                print('If you have changed your mind about withdrawing from this wallet, enter any letter or character to return to the previous page.')
                amount = float(input('Enter the amount you would like to withdraw: '))
                if amount > 0:
                    if self.balance >= amount: # Check if balance is sufficient for withdrawal
                        self.balance -= amount
                        self.last_transaction = 'withdraw' # Changing what the nature of the last transaction with to withdraw. 
                        print(' ')
                        print(f'Successfully withdrawn {amount} from your wallet of name "{self.wallet_name}".')
                        break
                    else:
                        print(' ')
                        print('Insufficient balance to make this withdrawal. Please enter a more suitable amount.')
                else:
                    print(' ')
                    print('Invalid input. Please enter a positive number.')
            except ValueError:
                print(' ')
                print(f'Withdrawl from wallet of name: "{self.wallet_name}" cancelled.')
                print('Returning to wallet management page...')
                break




class HolidaysWallet(DailyUseWallet):
    wallet_type = 'Holidays' 
    
    # Holiday wallets have all the same functionality as Daily Use Wallets. 
    # Meaning a error can be raised for the unwanted method, and it can be considered a Holiday wallet. 



    def transfer_amount(self, customer, banking_system): # A customer instance must be passed in order to have access to wallet information and a banking class instance to get the system_account attribute. 
    # Prompt the user to select the destination wallet
        
        if self.wallet_type == 'Holidays': 
            print(' ')
            print(f'As the selected source wallet is of type "{wallet.wallet_type}", it does not support global transfer functionality.')
            print('If you would like to transfer to the wallet of another customer, please use or create a "Daily Use" wallet instead.')
            print(' ')
            print('Returning to wallet management menu...')

            return
        
        while True:
            print(' ')
            print('Please select your destination wallet; the wallet you are sending an amount to.')
            destination_wallet = customer.select_wallet()
            if destination_wallet != self:
                # Destination wallet is different from the source wallet, so the transfer can proceed
                break
            else:
                print("The source and destination wallets cannot be the same. Please select a different destination wallet.")

        while True:

            try:
                amount = float(input("Enter the amount you want to transfer: "))

                if amount == 0:
                    print('')
                    print('The provided input was invalid, please enter a non-zero amount to transfer.')
                    print(' ')


                elif amount > 0:
                    # Check if the current wallet has sufficient balance to complete the transaction
                    if amount <= self.balance:
                        # Transfer the amount
                        self.balance -= amount

                        # The fee applied to local transfers is 0.5%, sent to the banking system's 'system_account' attribute.
                        transaction_fee = amount * 0.005
                        banking_system.system_account += transaction_fee
                        
                        # The recipient only recieves 99.5% of the sent amount.
                        destination_wallet.balance += (amount - transaction_fee)

                        self.last_transaction = 'local transfer' # Change the nature of the last transaction to transfer
                        destination_wallet.last_transaction = 'local transfer' # Change the nature of the last transaction to transfer
                        print(f"Successfully transferred {amount - transaction_fee} to the selected wallet, post-fees (0.5% for local transfer.)")

                        
                        return 


                    else:
                        # The current wallet doesn't have sufficient balance to complete the transaction
                        # Check if any of the other wallets have sufficient balance
                        for wallet_name, wallet in customer.wallets.items():
                            #print('count')
                            # Skip the current wallet and the destination wallet
                            if wallet == self or wallet == destination_wallet:
                                continue

                            if amount <= wallet.balance:
                                # A wallet with sufficient balance has been found
                                while True:
                                    # Prompt the user to confirm if they want to transfer the required amount from this wallet
                                    print(' ')
                                    print('The selected wallet does not have sufficient balance, but sufficient funds were found in another of your wallets')
                                    confirm = input(f'Do you want to transfer {amount} from wallet of name: "{wallet_name}", [y/n]?')

                                    if confirm.isnumeric() == True: 
                                        # When a value other than Y/y or N/n is inputted.
                                            print("The entered value is not valid, please try again ans answer with either y, or n.")


                                    elif confirm.lower() == 'y':
                                        # Transfer the required amount from the found wallet
                                        wallet.balance -= amount

                                        # The fee applied to local transfers is 0.5%, sent to the banking system's 'system_account' attribute.
                                        transaction_fee = amount * 0.005
                                        banking_system.system_account += transaction_fee

                                        # The recipient only recieves 99.5% of the sent amount. 
                                        destination_wallet.balance += (amount - transaction_fee)

                                        wallet.last_transaction = 'local transfer' # Change the nature of the last transaction to transfer
                                        destination_wallet.last_transaction = 'local transfer' # Change the nature of the last transaction to transfer

                                        print(' ')
                                        print(f"Successfully transferred {amount - transaction_fee} to the selected wallet, post-fees (0.5% for local transfer..")
                                        print(' ')
                                        print('Returning to wallet management menu...')
                                        
                                        return


                                        

                                    elif confirm.lower() == 'n':
                                        print(' ')
                                        print(f'Wallet of name: "{wallet_name}" has been chosen to not be the mediary for this transfer.')
                                        print('Searching for other viable wallets to use as source wallet...')

                                        break


                                    else: 

                                        # When a value other than Y/y or N/n is inputted.
                                        print(' ')
                                        print("The entered value is not valid, please try again ans answer with either y, or n.")

                        else:
                            # No wallet contain enough funds to transfer
                            print(' ')
                            print("The defined source wallet has insufficent funds for this transaction")
                            print('And there are no other wallets associated with your account that can facilitate this transfer.')
                            print('Please deposit additional funds to one of your wallets or define a smaller amount in order to transfer to carry out this transaction.')
                            print(' ')
                            print('Returning to wallet management menu...')

                            return

            except ValueError:
                # The entered amount is not a number
                print(' ')
                print("Please enter a valid amount to transfer.")
                print('')






class MortgageWallet(Wallet): 
    wallet_type = 'Mortgage' 

    # The mortgage wallet has the same functionality as the base Wallet class. 
    # So no additional functions need to be inherited. 
    pass 



main()
