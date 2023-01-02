import sys # sys is part of the Python standard library. Used primary in this script to exit the banking system. 


from Customer import Customer
from BankingSystem import BankingSystem
from Wallets import *

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
                                

if __name__=="__main__":
    main()
