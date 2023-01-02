# Customer class. 
# To be later imoported into the main file.  


from Wallets import *

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



