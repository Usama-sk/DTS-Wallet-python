from Transaction import Transaction
from Rpc import network
from secrets import token_bytes
import secrets
import  binascii
from sha3 import keccak_256
from eth_account import Account
from eth_keys import keys
from eth_utils import decode_hex, from_wei 

class Wallet:
    def __init__(self,Pri_Key : None):
        self.keyPair = {}
        if(Pri_Key == None):
            PK="0x"+keccak_256(token_bytes(32)).hexdigest()
            PK_bytes = decode_hex(PK)
        else:
            PK_bytes = decode_hex(Pri_Key)
        
    #Generate PK by ecdsa Algo for further requriments
        Private_Key = keys.PrivateKey(PK_bytes)
        self.keyPair['Private_Key'] = Private_Key
    #Generate Public key by using Ecdsa Private key 
        self.pub_key = Private_Key.public_key
        self.keyPair['Public_Key'] = self.pub_key.to_hex()
        
    #Generate Address key by using Hash Algo by using Ecdsa Public Key
        self.keyPair['Address_Key'] =  self.pub_key.to_checksum_address()

    def sign(self,data):
        PK = self.keyPair['Private_Key']
        return Account.signTransaction(data,PK)  

    def privateKeyString(self):
            privateKeyString =  self.keyPair['Private_Key']
            return privateKeyString

    def publicKeyString(self):
        publicKeyString = self.keyPair['Public_Key']
        return publicKeyString
        
    def AddressKeyString(self):
        AddressKeyString = self.keyPair['Address_Key']
        return AddressKeyString


    def send_Transaction(self,receiver , value):
        transaction = Transaction(self.AddressKeyString(),receiver , value)
        signed_txn = self.sign(transaction.payload())
        transaction.sign(signed_txn.rawTransaction.hex())
        net = network(self.AddressKeyString())
        receipt = net.send_transaction(signed_txn)
        transaction.save_receipt(receipt)
        return transaction    

    def check_balance(self):
        net = network(self.AddressKeyString())
        value = net.get_balance()
        balance = int(value,16)
        balance =from_wei(balance,'ether')
        return balance