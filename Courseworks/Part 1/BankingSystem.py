# Name: Andrew Naoya McWilliam, Section: Banking System class, to be later imported into the main file. 

# Accounts for all funtionality that the banking system should have to
# accommodate and store customer information and present textual displays, 
# for the sake of an intelligible UI. 


import sys # sys imported from the Python standard library in order to exit the UOB banking system. 
import csv  # csv imported from the Python standard library in order to write customer information and encrypted password to retrievable .csv file. 

from Customer import Customer # Importing customer class from external file.
class BankingSystem(): 
    
    def __init__(self):

        self.system_account = 0 # Transaction fees start at zero for every run of the program. 
        self.customers = {} # Empty dictionary to store customer objects. 

    def main_display(self): 
        '''
        Displaying the text-based screen, where the customer will see their inital options.
        ''' 

        print("""
                ======= UOB Banking System =======
                
                  1. Create an account
                  2. Access an existing account
                  
                  or enter any other key to exit
                  """)


    def create_account(self):
        '''
        Variety of inputs are asked in order to create a customer profile,
        to be used later as a form of indentity in the UOB banking system.
        The newly generated customer is returned.
        '''

        print('To create an account, you will need to provide the following details:')
        print('First name, last name, country of residence, age, email, password and username')
        print(' ')
        while True:
            first_name = input('Please enter your first name: ')
            if not first_name.strip(): # A conditional statement checking if the input is soley blank space.
                                       # If it is, then the input will be rejected and looped until a valid answer is given. This is done for all inputs. 
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
            username = input('Please enter your username: ').rstrip()
            if not username.strip():
                print("Username cannot be empty or consist only of whitespace characters.")
            elif username in self.customers: # Usernames must be unique,
                                             # so this conditional statement rejects the input, 
                                             # if i's the same as the username of an exisiting customer. 
                print(f' The username: "{username}" is already taken. Please try another.')
            else:
                break

        while True:
            password = input('And finally, please enter your password: ').rstrip()
            if not password.strip():
                print("Password cannot be empty or consist only of whitespace characters.")
            elif password in self.customers: # Passwords must also be unqiue. So they are treated similarly to usernames. 
                print(f' The password: "{password}" is already taken. Please try another.')
            else:
                break
        
        # A new instance of the Customer class is defined and added to a dictionary, where its key is its username.
        new_customer = Customer(first_name, last_name, CofR, age, email, username, password)
        self.customers[new_customer.username] =  new_customer

        # Some additional text to make the textual interface more legible and understandable.
        print(' ')
        print('=====================================================================================')
        print(f'Customer of username {new_customer.username}, your banking account has been successfully created.')
        print('To access to your account, please first login using the 2nd option of the menu below.')
        print('Alternatively, you can choose the 1st option again to create another account. ')

        return new_customer
            

    def saver_encrypter(self, customer):
        '''
        Function that is executed after a customer account is formed that takes their key information; username 
        and password, encrypts the password using substitution and writes the username, password and 
        encrypted password to a .csv file. File accounts for customers across script runs. The specific customer
        who's information is to be stored is passed by a parameter, in the form of a Customer instance.
        '''

        # Listed in the dictonary are the key pairs for what the substitution encryptor replaces in the password.
        substitution_cipher_lower = {'a': '!','b': '@','c': '#','d': '$','e': '%','f': '^','g': '&', 'h': '*', 'i': '(', 'j': ')',
                                'k': '_','l': '+','m': '{', 'n': '}', 'o': '|', 'p': ':', 'q': '"', 'r': '<', 's': '>',  't': '?', 
                                'u': '[',  'v': ']', 'w': '~','x': '`',  'y': '-',  'z': '='}

        # Keys pairs for the upper case of those same letters.
        substitution_cipher_upper = {'A': 'Q','B': 'W','C': 'E', 'D': 'R', 'E': 'T','F': 'Y','G': 'U','H': 'I', 'I': 'O', 'J': 'P',
                                     'K': 'A','L': 'S', 'M': 'D', 'N': 'F', 'O': 'G','P': 'H','Q': 'J', 'R': 'K','S': 'L','T': 'Z',
                                     'U': 'X','V': 'C', 'W': 'V','X': 'B','Y': 'N', 'Z': 'M'}

        substitution_cipher_symbols = {v: k for k, v in substitution_cipher_lower.items()}

        # Adding ciphers together to account for all symbols. 
        substitution_cipher_lower.update(substitution_cipher_upper)
        substitution_cipher_lower.update(substitution_cipher_symbols)

        # Each individual item of inputted password is iterated through and substituted, relative to the final cipher. 
        encrypted_password = ''.join([substitution_cipher_lower[c] if c in substitution_cipher_lower else c for c in customer.password])

        # Open the file in append mode.
        with open('login_details.csv', 'a', newline='') as csvfile:
            # Create a CSV writer
            writer = csv.writer(csvfile)

            # Check if the file is empty to ensure the column titles are not appended to the .csv file every time the function is called. 
            csvfile.seek(0, 2)  # Go to the end of the file.
            if csvfile.tell() == 0:  # If the file is empty, write the titles.
                writer.writerow(['Username', 'Password', 'Encrypted Password']) # Column titles.

            # Write the row to the CSV file
            writer.writerow(['  ' + customer.username, '  ' + customer.password, '  ' + encrypted_password])


    def login_screen(self):
        '''
        The login interface for when users want to access a particular customer account.
        Returns the successful instance of the Customer object, if login passes.
        '''
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
                print('Returning to main menu..') # If the user enters the incorrect password, they are returned to the main UOB banking system page. 
                break

            else:
                # If the login is successful, break out of the loop and return the customer object, 
                # such that any further action is applied to that customer instance specifically.
                print(' ')
                print(f"Login successful, welcome {username}.") 
                
                return customer


    def login_check(self, username, password):
        """Verify the provided credentials for login and return the customer object for the logged in user.
            Takes in the username as a parameter that the user has inputted and similarly with the password.
            If the login details are accepted, the accepted customer instance is returned.
        """

        if username not in self.customers: # There is no matching username in the recorded list of customers. 
            raise ValueError("Unfortunately, an account with this username does not exist, please try again or exit this page.")

        if self.customers[username].password != password: # Similarly no matching passowords on the system. 
            raise ValueError("Incorrect password, please try again.")
        
        return self.customers[username] # This returns the customer object for the checked username. 

    

    def customer_display(self, customer): 
        '''
        Basic text-based interface for customer once they have logged in.
        Takes customer instance as a parameters in order to display the 
        username attribute.
        '''
        print(f"""
        ======= Customer account menu for user: {customer.username} =======
        
            1. Create a wallet
            2. Manage active wallets 
            3. Log out of account and return to main menu
            4. Close account
            
            """)
        

    def walletm_display(self, customer):
        '''
        Basic text-based interface for wallet management that a customer navigates to, 
        once they have logged in. Takes customer instance as a parameters in order to 
        display the username attribute.
        '''
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
        '''
        Ends the UOB banking system script.
        Implemented when the user chooses to leave the application.
        '''
        print(' ')
        print('You have chosen to exit the UOB banking system.')
        print('Thank you for your patronage, we hope to see you again soon!')
        print(' ')
        
        sys.exit() # Why importing sys is necessary. 




    def delete_row(self, filename, username):
        '''
        When a customer account is deleted, the saved customer information
        associated with the closed customer account is also deleted and 
        a new .csv file without the closed customer account is made. Takes the file name, 
        that will always be 'login_details.csv' and the specific customer's username as 
        parameters.
        '''
        
        rows = []

        # Open the file in read mode
        with open(filename, 'r', newline='') as csvfile:
            # Read the file
            reader = csv.reader(csvfile)
            # Iterate through the rows
            for row in reader:
                # If the username column does not match the desired username, keep the row. 
                if row[0].strip() != username: # .strip() is applied, as spaces may adversely affect results.
                    
                    # If there is no match, the row is appended to the empty list.
                    rows.append(row)

        # Open the file in write mode
        with open(filename, 'w', newline='') as csvfile:
            # Write the updated list of rows to the file using the appended to list. 
            writer = csv.writer(csvfile)
            writer.writerows(rows)





    def del_account(self, customer): 
        '''
        Close a customer account and delete all associated information with it / stored in it.
        Such information including: wallets, username and passwords, etc... 
        Takes the customer instance that wants to be deleted as a parameter.
        The Boolens True or False are returned if the deletion is confirmed or 
        rejected, respectively.
        '''

        # Additions to textual interface for the sake of being more legible.
        print(' ')
        print('If your account is closed, all account information, including any created wallets will be lost.')
        print('Please enter Y/y, for Yes and N/n, for No.')
        print(' ')
        # Input asking for confirmation.
        confirmation = input(f'{customer.username}, are sure you want to close your account?')

        # Input should be a letter, not a number, this conditional checks for that.
        if confirmation.isnumeric() == True: 
            print(' ')
            print('The entered value is not a valid option, please try again.')
            
        # Conditional for when the user confirms to delte their account. 
        elif confirmation.lower() == 'y':
            print(' ')
            print(f'The account of username: {customer.username}, has been closed.')
            self.delete_row('login_details.csv',customer.username )
            del(self.customers[customer.username])
            print('Now returning to main menu...')

            return True # Boolean indicating outcome. 
            
        # In case the customer made a mistake and doesn't want to delete their account / one of their accounts. 
        elif confirmation.lower() == 'n':
            print(' ')
            print(f'The deletion of the account with username: {customer.username}, has been cancelled.')
            print(f'Now returning to customer menu...')
            
            return False # Boolean indicating outcome. 


        else: # No valid option provided, loop continued until one is given. 
            print(' ')
            print('The value provided is not a valid option.')
            print('Please look at the available options and try again.')
            print(' ')
            print(' ')






    def select_customer(self, CustomerInstance):
        '''
        Displays all customers associated with the cuurent instance of
        the BankingSystem class and allows the present user / customer 
        to select one, a customer instance is passed in, in order to select
        a user other than that specific user. Used for global transfers in main.py.
        The selected customer instance is returned. 
        '''

        # More textual imterface for the sake of being understandable. 
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


