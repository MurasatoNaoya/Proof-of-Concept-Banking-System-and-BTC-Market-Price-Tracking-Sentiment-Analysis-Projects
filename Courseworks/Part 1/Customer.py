# Name: Andrew Naoya McWilliam, Section: Customer class, to be later imported into the main file.  

# Class for storing customer information (e.g, name, username password, etc..) and data relating to 
# specific instances of wallet classes. Specifically, methods associated with the display, creation 
# and deletion of wallet class instances. 

from Wallets import * # Importing all wallet classes associated with the file 'Wallets'.

class Customer(): 

    # Defining a constructor that instantiates consumer objectss. 
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
        """
        Create a new wallet with a given name and wallet type.
        """
        
        # Additional textual interface to make the program more intuitive. 
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

        # Set up while loop to ensure a valid input in entered. 
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
            
            # Check if a wallet that is associated with the account, of the same name already exists. 
            # If such a wallet does exist, then the user will be prompted to enter another name. 
            if wallet_name in self.wallets: 
                print(' ')
                print("A wallet with this name already exists, please try a different name.")
                print(' ')

            if wallet_name.strip() == "": # Checking whether the provided name is only spaces, which is not a valid name. 
                print(' ')
                print('The entered name is only spaces and therefore is not valid.')
                print('Please try a different wallet name.')
                print(' ')

            else: 
                break # There is no other wallet with the same name and it's not just empty space, so the input is accepted. 
        
        self.wallet_id += 1
        wallet_id = f"{self.wallet_id:03d}"  # Format the wallet_id as a 3-digit string (e.g. 001, 002, etc.)
        # Create the appropriate type of wallet based on the provided type

        # Daily wallet selection.
        if wallet_type == 1:
            self.wallets[wallet_name] = DailyUseWallet(wallet_id, wallet_name) # wallet_type is also defined as a static attribute.
            print(' ')
            print(f'A Daily Use wallet of the name: "{wallet_name}", has been created.')
            print(f'This created wallet has the ID: {wallet_id}')
            print(' ')
            print(f'Returning to customer page of user: {self.username}...')
            print(' ')
            #print(self.wallets[wallet_name].wallet_type)

        # Savings wallet selection. 
        elif wallet_type == 2:
            self.wallets[wallet_name] = SavingsWallet(wallet_id, wallet_name) # wallet_type is also defined as a static attribute.
            print(' ')
            print(f'A Savings wallet of the name: "{wallet_name}", has been created.')
            print(f'This created wallet has the ID: {wallet_id}')
            print(' ')
            print(f'Returning to customer page of user: {self.username}...')
            print(' ')
            #print(self.wallets[wallet_name].wallet_type)

        # Holidays wallet selection.
        elif wallet_type == 3:
            self.wallets[wallet_name] = HolidaysWallet(wallet_id, wallet_name) # wallet_type is also defined as a static attribute. 
            print(' ')
            print(f'A Holidays wallet of the name: "{wallet_name}", has been created.')
            print(f'This created wallet has the ID: {wallet_id}')
            print(' ')
            print(f'Returning to customer page of user: {self.username}...')
            print(' ')
            #print(self.wallets[wallet_name].wallet_type)

        # Mortgage wallet selection. 
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
        """
        Display all available wallets and allows the user to select one by number.
        This function is used extensively for actions involved with wallets, like 
        depositing, withdrawing and transferring. If a wallet is selected, that 
        particular wallet instance is returned. 
        """

        # Additional textual interface to make the program more intuitive. 
        print("\n========= Wallet selection menu ==========")
        print(f'Welcome to the wallet selection menu, user {self.username}.')
        print('Please select one of the available wallets by entering its number.')
        print(' ')
        print('Available wallets:')
        for i, (name, wallet) in enumerate(self.wallets.items()):
            print(f"{i+1}. {wallet.wallet_id}, {wallet.wallet_type} wallet of name: {name} and balance {wallet.balance}")
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
        """
        Display all available wallets. 
        Users can press any key to exit the display screen.
        If the user exits the method, nothing is returned, in
        order to end the method. 
        """
        print(f"\n========= All available wallets for user: {self.username} ==========")
        print(' ')
        # Iterate through all wallets associated with the customer account and print the information of interest. 
        for i, (name, wallet) in enumerate(self.wallets.items()):
            print(f'{i+1}. ID: {wallet.wallet_id}, Name: {wallet.wallet_name}, Wallet Type: "{wallet.wallet_type}", Balance: {wallet.balance}, Nature of last transaction: {wallet.last_transaction}')
        print(' ')
        answer = input('Enter any key to return the wallet management menu')

        if answer != None: 
            return


    def delete_wallet(self): 
        '''
        Deletes a selected wallet associated with the customer account.
        Regardless of whether the deletion is confirmed or rejected, nothing 
        is returned, simply to exit out of the while loop and end the method. 
        '''
        
        # The select_wallet() method is implemented in order to specify the wallet the user wants to delete.≈
        wallet = self.select_wallet()
        

        print(' ')

        while True:
            # Prompt the user to confirm if they want to transfer the required amount from this wallet
            print(' ')
            confirm = input(f'Are you sure you want to delete your waller of name: "{wallet.wallet_name}", [y/n]?')
            
            if confirm.isnumeric() == True: 
                # When a value other than Y/y or N/n is inputted.
                print(' ')
                print("The entered value is not valid, please try again and answer with either y, or n.")

            # User confirms they want to delete the specified wallet. 
            elif confirm.lower() == 'y':
            
                del(self.wallets[wallet.wallet_name])   
                print(' ')
                print(f'Wallet of name: "{wallet.wallet_name}" has been deleted from your account.')

                return

            # User rejects / changes their mind about deleting the specified wallet. 
            elif confirm.lower() == 'n':
                
                print(' ')
                print(f'The deletion of wallet with name: "{wallet.wallet_name}" has been cancelled.')
                
                return

            else:
                # When a value other than Y/y or N/n is inputted.
                # As this is within a while loop, the user will be prompted for a valid input until they do. 
                print(' ')
                print("The entered value is not valid, please try again and answer with either y, or n.")

