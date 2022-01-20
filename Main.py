from Transaction import Transaction
from Wallet import Wallet


if __name__ == '__main__':

    receiver ="0x8cf0726Bc2f166c3F0427A199cCaDcf993B0Ff8A"
    amount = 0.00001
    wallet = Wallet()

    
    #transaction = wallet.send_Transaction(receiver, amount )
    Balance = wallet.check_balance()

    print(Balance)
    #print(transaction.toJson())

