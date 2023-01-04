# Name: Andrew Naoya McWilliam, Section: Base wallet class and all child wallet classes, to be later imoported into the main file.  

# Classes that describe the base wallet class that accounts for all callable attributes of all possible wallet instances, namely balance, walletID 
# and wallet name and last transaction. Additionally, all of the methods related to the various functionalities across 
# all of the wallet types (where applicable) supported on the UOB banking system (e.g, transfer, withdraw, etc..) . 


class Wallet():

    last_transaction = None # The last type of transaction of a wallet will be tracked so it can be later displayed. 
                            # It is initially set to None, but will be resassigned through future wallet actions. 

    def __init__(self, wallet_id, wallet_name):
        self.balance = 0  # Initial balance is 0
        self.wallet_id = wallet_id
        self.wallet_name = wallet_name

    # All wallets have a deposit feature, so this deposit method will be inherited for all wallet types. 
    def deposit(self):
        '''
        A user deposits / adds a specified amount to a wallet. 
        This functionality is universal regardless of wallet type, 
        so deposit as a function is defined in the parent class.
        '''
        while True: # The user will keep being prompted until they provide a valid input.
            try:
                print('If you have changed your mind about depositing to this wallet, enter any letter or character to return to the previous page.')
                amount = float(input('Enter the amount you would like to deposit: '))
                if amount > 0:
                    self.balance += amount # Depositing / adding amount. 
                    self.last_transaction = 'deposit' # Changing what the nature of the last transaction with to deposit. 
                    print(' ')
                    print(f'Successfully deposited {amount} into your wallet of name "{self.wallet_name}".') # Deposit confirmation. 
                    break
                else:
                    print(' ')
                    print('Invalid input. Please enter a positive number.')
            except ValueError:
                print(' ')
                print(f'Deposit to wallet of name: "{self.wallet_name}" cancelled.')
                print('Returning to wallet management page...')
                break




class DailyUseWallet(Wallet): # Inherits basic attributes and method (deposit) from the base class Wallet.
                              # This is the case for all wallet types available to customers. 
    wallet_type = 'Daily Use' 

    def withdraw(self, customer):
        '''
        A user withdraws / minus a specified amount from a wallet. 
        This functionality is only available to the "Daily Use", " Savings" 
        and "Holidays" wallet types. When the user has a balance of 0, 
        nothing is returned in order to exit the function, in spite of while
        loops.
        '''

        # Check if the wallet's balance is equal to 0. 
        # A wallet of balance 0 cannot be withdrawn from. 
        # if self.balance == 0:
        #     print('Sorry, you cannot withdraw from a wallet with a balance of 0.')
        #     return
            
        while True: # The user will keep being prompted until they provide a valid input.
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
                        # Check if any of the other wallets, of viable wallet type, have sufficient balance to transfer to the current wallet. 
                        for wallet_name, wallet in customer.wallets.items():
                            # Skip the current wallet. 
                            if wallet == self:
                                continue
                            if amount <= wallet.balance and wallet.wallet_type != 'Mortgage' and wallet.wallet_type != 'Savings': # Mortgage and Savings type wallets do not support transfers. 
                                # A wallet with sufficient balance has been found
                                # Prompt the user to confirm if they want to transfer the required amount from this wallet
                                confirm = input(f"The selected wallet doesn't have sufficient balance. Do you want to transfer {amount} from {wallet_name}? [y/n] ")
                                if confirm.lower() == 'y':
                                    # Transfer the required amount from the found wallet
                                    wallet.balance -= amount
                                    self.balance += amount
                                    wallet.last_transaction = 'transfer' # Change the nature of the last transaction to transfer. 
                                    self.last_transaction = 'withdraw' # Changing what the nature of the last transaction with to withdraw.
                                    print(' ')
                                    print(f'{amount} transferred from {wallet_name} to {self.wallet_name}, and then withdrawn from wallet of name "{self.wallet_name}".')
                                    print('Returning to wallet management menu...')
                                    return
                                    
                        else:
                            # No wallet with sufficient balance was found. 
                            print(' ')
                            print("None of your wallets have sufficient balance, or are of valid wallet type to complete this transaction.")
                            print('Returning to wallet management menu...')
                            return
                else:
                    print(' ')
                    print('Invalid input. Please enter a positive number.')
            except ValueError:
                print(' ')
                print(f'Withdrawl from wallet of name: "{self.wallet_name}" cancelled.')
                print('Returning to wallet management page...')

                break



    def transfer_amount(self, customer, banking_system):
        '''
        Transfer an specified amount between wallets. 
        This functionality is only available to the "Daily Use"
        and "Holidays" wallet types. The customer parameter represents
        the user that is transferring locally and the parameter banking_system 
        represents a BankingSystem instance, that is passed to access the system_account 
        attribute. Nothing is returned in order to exit the function, in spite of while
        loops.
        '''

        # Prompt the user to select the destination wallet
        while True: # The user will keep being prompted until they provide a valid input.
            print(' ')
            print('Please select your destination wallet; the wallet you are sending an amount to.')
            destination_wallet = customer.select_wallet()
            if destination_wallet != self:
                # Destination wallet is different from the source wallet, so the transfer can proceed
                break
            else:
                print("The source and destination wallets cannot be the same. Please select a different destination wallet.")

        while True: # The user will keep being prompted until they provide a valid input.
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
                            
                            # For a wallet substitute to mediate a transaction, they have the functionality to transfer locally in the first place. 
                            # Meaning they cannot be either a Savings or Mortgage wallet. 
                            if amount <= wallet.balance and wallet.wallet_type != 'Savings' and wallet.wallet_type != 'Mortgage': #
                                # A wallet with sufficient balance has been found
                                while True: 
                                    # Prompt the user to confirm if they want to transfer the required amount from this wallet
                                    print(' ')
                                    print('The selected wallet does not have sufficient balance, but sufficient funds were found in another of your wallets that supports local transfer.')
                                    confirm = input(f'Do you want to transfer {amount} from wallet of name: "{wallet_name}", [y/n]?')

                                    if confirm.isnumeric() == True: 
                                        # When a value other than Y/y or N/n is inputted.
                                            print("The entered value is not valid, please try again and answer with either y, or n.")


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


                                        

                                    elif confirm.lower() == 'n': # If the provided alternative wallet is rejected for whatever reason.
                                        print(' ')
                                        print(f'Wallet of name: "{wallet_name}" has been chosen to not be the mediary for this transfer.')
                                        print('Searching for other viable wallets to use as source wallet...')

                                        break


                                    else: 

                                        # When a value other than Y/y or N/n is inputted.
                                        print(' ')
                                        print("The entered value is not valid, please try again and answer with either y, or n.")

                        else:
                            # No wallet contain enough funds to transfer
                            print(' ')
                            print("The defined source wallet has insufficent funds for this transaction")
                            print('And there are no other wallets associated with your account that can facilitate this transfer, because of balance and/or wallet type.')
                            print('Please deposit additional funds to one of your wallets or define a smaller amount to transfer.')
                            print(' ')
                            print('Returning to wallet management menu...')

                            return

            except ValueError:
                # The entered amount is not a number
                print(' ')
                print("Please enter a valid amount to transfer.")
                print(' ')






    def transfer_to_customer(self, customer_sender, customer_reciever, banking_system ):
        '''
        The destination wallet of the other customer is selected from their available wallets
        and a specified amount to transfer to the other customer's wallet is chosen. 
        Checks for viability are carried out throughout this entire process.
        The customer parameters represent the source customer and the destination customer 
        respectively and the parameter banking_system represents the running BankingSystem instance, 
        that is passed to access the system_account attribute. Nothing is returned in order to 
        exit the function, in spite of while loops.
        '''

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

        while True: # The user will keep being prompted until they provide a valid input.

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
                        print(f'Successfully transferred {amount - transaction_fee} to the selected wallet of customer: "{customer_reciever.username}", post-fees (1.5% for global transfer).')

                        
                        return 


                    else:
                        # The current wallet doesn't have sufficient balance to complete the transaction
                        # Check if any of the other wallets have sufficient balance
                        for wallet_name, wallet in customer_sender.wallets.items():
                            #print('count')
                            # Skip the current wallet and the destination wallet
                            if wallet == self or wallet == destination_wallet:
                                continue
                            
                            # For a substitute wallet to be chosen to act as a valid mediary for a global transaction. 
                            # It must be a Daily Use wallet, as only Daily use wallets can be used for inter-customer transfers. 
                            if amount <= wallet.balance and wallet.wallet_type == 'Daily Use':
                                # A wallet with sufficient balance has been found
                                while True:
                                    # Prompt the user to confirm if they want to transfer the required amount from this wallet
                                    print(' ')
                                    print('The selected wallet does not have sufficient balance, but sufficient funds were found in another of your wallets that supports global transfer.')
                                    confirm = input(f'Do you want to transfer {amount} from wallet of name: "{wallet_name}", [y/n]?')

                                    if confirm.isnumeric() == True: 
                                        # When a value other than Y/y or N/n is inputted.
                                            print("The entered value is not valid, please try again and answer with either y, or n.")


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
                                        print(f'Successfully transferred {amount - transaction_fee} to the selected wallet of customer: "{customer_reciever.username}", post-fees (1.5% for global transfer).')
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
                                        print("The entered value is not valid, please try again and answer with either y, or n.")

                        else:
                            # No wallet contain enough funds to transfer
                            print(' ')
                            print("The defined source wallet has insufficent funds for this transaction")
                            print('And there are no other wallets associated with your account that can facilitate this transfer, due to lacking balance and/or wallet type. ')
                            print('Please deposit additional funds to one of your wallets or define a smaller amount to transfer.')
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
        
         
    def withdraw(self, customer):
        '''
        A user withdraws / minus a specified amount from a wallet. 
        This functionality is only available to the "Daily Use", " Savings" 
        and "Holidays" wallet types. When the user has a balance of 0, 
        nothing is returned in order to exit the function, in spite of while
        loops.
        '''

        # Check if the wallet's balance is equal to 0. 
        # A wallet of balance 0 cannot be withdrawn from. 
        # if self.balance == 0:
        #     print('Sorry, you cannot withdraw from a wallet with a balance of 0.')
        #     return
            
        while True: # The user will keep being prompted until they provide a valid input.
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
                        # Check if any of the other wallets, of viable wallet type, have sufficient balance to transfer to the current wallet. 
                        for wallet_name, wallet in customer.wallets.items():
                            # Skip the current wallet. 
                            if wallet == self:
                                continue
                            if amount <= wallet.balance and wallet.wallet_type != 'Mortgage' and wallet.wallet_type != 'Savings': # Mortgage and Savings type wallets do not support transfers.
                                # A wallet with sufficient balance has been found
                                # Prompt the user to confirm if they want to transfer the required amount from this wallet
                                confirm = input(f"The selected wallet doesn't have sufficient balance. Do you want to transfer {amount} from {wallet_name}? [y/n] ")
                                if confirm.lower() == 'y':
                                    # Transfer the required amount from the found wallet
                                    wallet.balance -= amount
                                    self.balance += amount
                                    wallet.last_transaction = 'transfer' # Change the nature of the last transaction to transfer. 
                                    self.last_transaction = 'withdraw' # Changing what the nature of the last transaction with to withdraw.
                                    print(' ')
                                    print(f'{amount} transferred from {wallet_name} to {self.wallet_name}, and then withdrawn from wallet of name "{self.wallet_name}".')
                                    print('Returning to wallet management menu...')
                                    return
                        else:
                            # No wallet with sufficient balance was found. 
                            print("None of your wallets have sufficient balance or are of valid wallet type to complete this transaction.")
                            print('Returning to wallet management menu...')
                            return
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
        '''
        Transfer an specified amount between wallets. 
        This functionality is only available to the "Daily Use"
        and "Holidays" wallet types. The customer parameter represents
        the user that is transferring locally and the parameter banking_system 
        represents the running BankingSystem instance, that is passed to access the system_account 
        attribute. Nothing is returned in order to exit the function, in spite of while
        loops. 
        '''

        # Prompt the user to select the destination wallet
        while True: # The user will keep being prompted until they provide a valid input.
            print(' ')
            print('Please select your destination wallet; the wallet you are sending an amount to.')
            destination_wallet = customer.select_wallet()
            if destination_wallet != self:
                # Destination wallet is different from the source wallet, so the transfer can proceed
                break
            else:
                print("The source and destination wallets cannot be the same. Please select a different destination wallet.")

        while True: # The user will keep being prompted until they provide a valid input.
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
                            
                            # For a wallet substitute to mediate a transaction, they have the functionality to transfer locally in the first place. 
                            # Meaning they cannot be either a Savings or Mortgage wallet. 
                            if amount <= wallet.balance and wallet.wallet_type != 'Savings' and wallet.wallet_type != 'Mortgage': 
                                # A wallet with sufficient balance has been found
                                while True: 
                                    # Prompt the user to confirm if they want to transfer the required amount from this wallet
                                    print(' ')
                                    print('The selected wallet does not have sufficient balance, but sufficient funds were found in another of your wallets that supports local transfer.')
                                    confirm = input(f'Do you want to transfer {amount} from wallet of name: "{wallet_name}", [y/n]?')

                                    if confirm.isnumeric() == True: 
                                        # When a value other than Y/y or N/n is inputted.
                                            print("The entered value is not valid, please try again and answer with either y, or n.")


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


                                        

                                    elif confirm.lower() == 'n': # If the provided alternative wallet is rejected for whatever reason.
                                        print(' ')
                                        print(f'Wallet of name: "{wallet_name}" has been chosen to not be the mediary for this transfer.')
                                        print('Searching for other viable wallets to use as source wallet...')

                                        break


                                    else: 

                                        # When a value other than Y/y or N/n is inputted.
                                        print(' ')
                                        print("The entered value is not valid, please try again and answer with either y, or n.")

                        else:
                            # No wallet contain enough funds to transfer
                            print(' ')
                            print("The defined source wallet has insufficent funds for this transaction")
                            print('And there are no other wallets associated with your account that can facilitate this transfer, due to lack of balance and/or wallet type.')
                            print('Please deposit additional funds to one of your wallets or define a smaller amount to transfer.')
                            print(' ')
                            print('Returning to wallet management menu...')

                            return

            except ValueError:
                # The entered amount is not a number
                print(' ')
                print("Please enter a valid amount to transfer.")
                print(' ')





class MortgageWallet(Wallet): 
    wallet_type = 'Mortgage' 

    # The mortgage wallet has the same functionality as the base Wallet class. 
    # So no additional functions need to be inherited. 
    pass 
