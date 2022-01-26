from Transaction import Transaction
from Wallet import Wallet
from configparser import ConfigParser


if __name__ == '__main__':

    # create Wallet code
    wallet = Wallet() 

    #Impoort Wallet code
    # PK=""
    # wallet = Wallet(PK) #Impoort Wallet

    #Account Details
    print(wallet.privateKeyString())
    print(wallet.publicKeyString())
    print(wallet.AddressKeyString())
    print(wallet.check_balance())

    #transaction code
    
    receiver =""#Enter receiver Address 
    amount = 0 # Enter ammount 

    # send transaction
    transaction = wallet.send_Transaction(receiver, amount) 

    # transaction Details
    print(transaction.toJson())

