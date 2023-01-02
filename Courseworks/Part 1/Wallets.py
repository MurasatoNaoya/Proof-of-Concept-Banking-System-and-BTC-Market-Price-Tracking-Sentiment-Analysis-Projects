# Base wallet class and all child wallet classes.
# To be later imoported into the main file.  


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