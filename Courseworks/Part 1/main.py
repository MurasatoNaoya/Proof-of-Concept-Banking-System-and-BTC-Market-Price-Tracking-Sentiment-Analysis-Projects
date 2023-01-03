import sys # sys is part of the Python standard library. Used primary in this script to exit the banking system. 

from Customer import Customer # Customer class imported from Customer file. 
from BankingSystem import BankingSystem # BankingSystem class imported from BankingSystem file. 
from Wallets import * # All classes from Wallet file imported.

def main(): 
    '''
    Definition of function that incorportates all functions
    from previously defined classes into a single 
    cohesive banking application. 
    '''
    # Booleans allowing for multiple while loops to be broken without several breaks.
    base = True
    a = True 
    b = True 
    c = True
    d = True 
    e = True 
    f = True

    print(' ')
    print('Welcome to the UOB banking system.')
    BankingSystemInstance = BankingSystem() # Creating an instance of the BankingSystem class. 

    while base: 
        a = True
        b = True
        c = True 
        e = True

        BankingSystemInstance.main_display() # Displaying the first main textual interface screen. 

        while a:
            decision = input("Enter choice: ")
          
            if decision.isnumeric() == False: 
                BankingSystemInstance.terminate() # If any other key than the provided options is entered, the UOB banking application will stop running. 
                
            
            elif int(decision) == 1: # If '1' is inputted, then the application begings account creation for the user. 
                cus1 = BankingSystemInstance.create_account()
                BankingSystemInstance.saver_encrypter(cus1)
                
                break

            elif int(decision) == 2: # If '2' is inputted, the user is prompted to enter their username and password to login. 
                                     # However, if there are no accounts on the banking system yet, it will reject the attempt to access an account. 
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
                BankingSystemInstance.customer_display(CustomerInstance) # Once the user has successfully logged in, they will be met with a customer menu. 
                c = True
                e = True
                
                while c:
                    decision = input('Enter choice: ')

                    if decision.isnumeric() == False: 
                        print(' ')
                        print('The entered value is not a valid option, please try again.')
                        break 
                    
                    if int(decision) == 1: # If '1' is entered, the user will be prompted into the wallet creation. 
                        CustomerInstance.create_wallet()
                        break

                    elif int(decision) == 2: # So long as the customer has an active wallet, they will be passed into the wallet management page. 
                        if len(CustomerInstance.wallets) ==0: # Checks to see if the user has any wallets. 
                            print(' ')
                            print('Currently, there are no active wallets associated with your account.') 
                            print('In order to proceed, first create a wallet.')
                            print(' ')

                            break # The user will be retuned to the customer menu, so long as they have no active wallets.
                        
                    elif int(decision) == 3: # If '3' is entered, the user is logged out and returned to the main menu page. 
                        print(' ')
                        print(f'Logging out of the account of username: {CustomerInstance.username}')
                        print('Returning to main menu now...')

                        a = False
                        b = False
    
                        break 

                    elif int(decision) == 4: # If '4' is entered, the user will be prompted to chose an account to delete
                                             # and all relevant information related to the account.

                        while d:
                            delete = BankingSystemInstance.del_account(CustomerInstance)

                            if delete == True: 
                                
                                a = False
                                b = False
                                c = False
                                e = False # This must be added to ensure while loop E is not mistakenly run afterwards. 
                                break

                            
                            elif delete == False:
                                
                                c = False
                                e = False # This must be added to ensure while loop E is not mistakenly run afterwards. 
                                break
                        
                        

            
                    while e: # The customer does have at least one active wallet, and is therefore passed to this wallet management page. 
                        BankingSystemInstance.walletm_display(CustomerInstance)
                        
                        while f: # If the user enters a value not in the numbered menu, they will be returned to the customer menu. 
                            decision = input('Enter choice: ')

                            if decision.isnumeric() == False:  
                                print(' ')
                                print('Returning to customer menu...')
                                
                                e = False
                                c = False
                                break 

                            if int(decision) == 1: # If '1' is selected, all active wallets of the user and their relevant information is displayed. 
                                CustomerInstance.display_wallets()
                                break

                                

                            elif int(decision) == 2: # If '2' is selected, the user will be able to select a wallet and specify an amount of money to keep in it. 
                                wallet = CustomerInstance.select_wallet()
                                wallet.deposit()
                                break

                                
                            elif int(decision) == 3: #Contrastingly, if '3' is selected, the user will be able to select a wallet and specify an amount of money to withdraw from it. 
                                wallet = CustomerInstance.select_wallet()
                                
                                try: 
                                    wallet.withdraw()
                                    break 
                                
                                except AttributeError: # Only "Daily Use" and "Savings" wallets can be withdrawn from, this try statements account for this.  
                                    print(' ')
                                    print(f'As the selected wallet is of type "{wallet.wallet_type}", it does not support withdraw functionality.')
                                    print('If you would like to withdraw from a wallet, please create either a "Daily Use" or "Savings" wallet instead. ')
                                    print(' ')
                                    break
                                
                            elif int(decision) == 4:
                                # Transfer between customer's local wallets.
                                if len(CustomerInstance.wallets) ==1: # Check for whether local transfer is even possible. 
                                    print(' ')
                                    print('You currently have only one active wallet, therefore local transfer is not possible.')
                                    print('Returning to wallet management menu...')
                                    break
                                try:
                                    print(' ')
                                    print('Please select your source wallet; the wallet you are sending an amount from.')
                                    wallet = CustomerInstance.select_wallet() # Defining the souce wallet to send funds from. 
                                    wallet.transfer_amount(CustomerInstance, BankingSystemInstance)
                                    break

                                except AttributeError: # Only "Daily Use" and "Holidays" wallets can be used to transfer between a user's wallets, this try statements account for this.  
                                    print(' ')
                                    print(f'As the selected source wallet is of type "{wallet.wallet_type}", it does not support local transfer functionality.')
                                    print('If you would like to transfer to a wallet, please use or create either a "Daily Use" or "Holidays" wallet instead.')
                                    print(' ')
                                    print('Returning to wallet management menu...')
                                    break

                            elif int(decision) == 5:
                                    # Transfer between customers, global wallets. 
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
                                    if wallet.wallet_type == 'Holidays': # "Holidays" wallets cannot be used for customer-to-customer transfers, this conditional statement therefore excludes them.
                                        print(' ')
                                        print(f'As the selected source wallet is of type "{wallet.wallet_type}", it does not support global transfer functionality.')
                                        print('If you would like to transfer to the wallet of another customer, please use or create a "Daily Use" wallet instead.')
                                        print(' ')
                                        print('Returning to wallet management menu...')
                                        break

                                    wallet.transfer_to_customer(CustomerInstance, customer_reciever, BankingSystemInstance)
                                    break

                                except AttributeError: # This accounts for the exclustions of the "Savings" and "Mortgage" type wallets that cannot be used for global, cuatomer-to-customer transfers. 
                                    print(' ')
                                    print(f'As the selected source wallet is of type "{wallet.wallet_type}", it does not support global transfer functionality.')
                                    print('If you would like to transfer to the wallet of another customer, please use or create a "Daily Use" wallet instead.')
                                    print(' ')
                                    print('Returning to wallet management menu...')
                                    break

                            
                            elif int(decision) == 6: # If '6' is entered, then a wallet is selected and then deleted from the user's customer account. 
                                                     # The externally stored .csv file keeping track of username, password and encrypted password is also updated to account for the deletion too. 
                                CustomerInstance.delete_wallet()
                                break 

                            else: # If none of the specified options are chosen, the user is returned to the customer menu. 
                                print(' ')
                                print('Returning to customer menu...')
                                
                                e = False
                                c = False
                                break 
                                
#  Running main() directly. 
if __name__=="__main__":
    main()


