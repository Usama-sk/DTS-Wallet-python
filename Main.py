from Transaction import Transaction
from BlockchainUtils import BlockchainUtils
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
import secrets
from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256

if __name__ == '__main__':

    sender ='sender'
    receiver= 'receiver'
    amount = 1
    type= "TRANSFER"

    
    wallet = Wallet()
    Fwallet = Wallet()
    pool =TransactionPool()

    
    transaction = wallet.createTransaction(receiver, amount, nonce, )

    Pri_Key = wallet.privateKeyString()
    Pub_Key = wallet.publicKeyString()
    Address = wallet.AddressKeyString()
    signature = wallet.sign(transaction.toJson())
    print(transaction.toJson())

    # signatureValid = wallet.signatureValid(transaction.toJson(),signature , wallet.publicKeyString())
    
    # print("Private Key: "+ Pri_Key+"\n")
    # print("Public Key: "+ Pub_Key+"\n")
    # print("Address Key: "+ Address+"\n")
    # print("Signature: "+ signature+"\n")
    # print("Signature Validation: "+ str(signatureValid)+"\n")
    # print("Transaction: "+ str(transaction.toJson())+"\n")
    
    #signatureValid = wallet.signatureValid(transacton.payload(),signature , Fwallet.publicKeyString())
    #signatureValid = wallet.signatureValid(transacton.payload(),signature , wallet.publicKeyString())
    # if pool.transactionExists(transaction) == False:
    #     pool.addTransaction(transaction)
    # if pool.transactionExists(transaction) == False:
    #     pool.addTransaction(transaction)

    #block = Block(pool.transactions,'lastHash', 'forger', 1)
    #pa= wallet.AddressKeyString1(pbk)
    
    #print(signatureValid)
