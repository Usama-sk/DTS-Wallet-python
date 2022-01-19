from Transaction import Transaction
from BlockchainUtils import BlockchainUtils
import secrets
import  binascii
from sha3 import keccak_256
from eth_account import Account
from eth_keys import keys
from eth_utils import decode_hex

class Wallet():
    def __init__(self):
        self.keyPair = {}
        PK="0x"+keccak_256(token_bytes(32)).hexdigest()
        #PK_bytes = decode_hex(PK)
        PK_bytes = decode_hex("0x25b11fa19c1a45a4ab70f034fe0134271c70c68316f732dfcc83b1e275c46968")
        secrets256 = keccak_256(token_bytes(32)).hexdigest()
    #Generate PK by ecdsa Algo for further requriments
        Private_Key = keys.PrivateKey(PK_bytes)
        self.keyPair['Private_Key'] = Private_Key
    #Generate Public key by using Ecdsa Private key 
        pub_key = Private_Key.public_key
        self.keyPair['Public_Key'] = pub_key.to_hex()
    #Generate Address key by using Hash Algo by using Ecdsa Public Key
        self.keyPair['Address_Key'] =  pub_key.to_checksum_address()

    def sign(self,data):
        PK = self.keyPair['Private_Key']
        return Account.signTransaction(data,PK)  

    @staticmethod
    def signatureValid(self,data, signature, publicKeyString):
        signature = binascii.unhexlify(signature)
        dataHash = BlockchainUtils.hash(data)
        publicKey = VerifyingKey.from_string(bytes.fromhex(publicKeyString), curve=SECP256k1)
        signatureValid = publicKey.verify(signature, dataHash)
        return signatureValid


    def privateKeyString(self):
            privateKeyString =  self.keyPair['Private_Key']
            return privateKeyString

    def publicKeyString(self):
        publicKeyString = self.keyPair['Public_Key']
        return publicKeyString
        
    def AddressKeyString(self):
        AddressKeyString = self.keyPair['Address_Key']
        return AddressKeyString


    def createTransaction(self,receiver , value,nonce,gasPriceHex):
        transaction = Transaction(self.publicKeyString(),receiver , value, nonce , gasPriceHex)
        signature = self.sign(transaction.payload())
        #transaction.sign(signature)
        return transaction    
