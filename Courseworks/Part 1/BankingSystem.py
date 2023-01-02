# Banking System class.
# To be later imoported into the main file.  

import sys 
import csv 

from Customer import Customer
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

        return new_customer
            

    def saver_encrypter(self, customer):

        # Listed in the dictonary are the key pairs for what the substitution encryptor replaces in the password.
        substitution_cipher_lower = {'a': '!','b': '@','c': '#','d': '$','e': '%','f': '^','g': '&', 'h': '*', 'i': '(', 'j': ')',
                                'k': '_','l': '+','m': '{', 'n': '}', 'o': '|', 'p': ':', 'q': '"', 'r': '<', 's': '>',  't': '?', 
                                'u': '[',  'v': ']', 'w': '~','x': '`',  'y': '-',  'z': '='}

        substitution_cipher_upper = {'A': 'Q','B': 'W','C': 'E', 'D': 'R', 'E': 'T','F': 'Y','G': 'U','H': 'I', 'I': 'O', 'J': 'P',
                                     'K': 'A','L': 'S', 'M': 'D', 'N': 'F', 'O': 'G','P': 'H','Q': 'J', 'R': 'K','S': 'L','T': 'Z',
                                     'U': 'X','V': 'C', 'W': 'V','X': 'B','Y': 'N', 'Z': 'M'}

        substitution_cipher_symbols = {v: k for k, v in substitution_cipher_lower.items()}

        # Adding ciphers together to account for all symbols. 
        substitution_cipher_lower.update(substitution_cipher_upper)
        substitution_cipher_lower.update(substitution_cipher_symbols)

        encrypted_password = ''.join([substitution_cipher_lower[c] if c in substitution_cipher_lower else c for c in customer.password])

        # Open the file in append mode
        with open('login_details.csv', 'a', newline='') as csvfile:
            # Create a CSV writer
            writer = csv.writer(csvfile)

        # Check if the file is empty
            csvfile.seek(0, 2)  # Go to the end of the file
            if csvfile.tell() == 0:  # If the file is empty, write the titles
                writer.writerow(['Username', 'Password', 'Encrypted Password'])

            # Write the row to the CSV file
            writer.writerow(['  ' + customer.username, '  ' + customer.password, '  ' + encrypted_password])


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


