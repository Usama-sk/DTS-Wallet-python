import uuid
import time
import copy
from eth_utils import to_wei

class Transaction:

    def __init__(self,senderPublicKey, recieverPublicKey,value,nonce,gasPriceHex):
        self.to = recieverPublicKey
        self.nonce = nonce
        self.gasPrice = gasPriceHex
        self.gas = 21000
        self.value = to_wei(value,'ether')
        self.chainId = 4
        # self.senderPublicKey = senderPublicKey
        # self.type = "Transfer"
        # self.id = uuid.uuid1().hex
        # self.timesamp = time.time()
        # self.signature = ''

    
    def toJson(self):
        return self.__dict__

    def sign(self, signature):
        self.signature = signature

    def payload(self):
        jsonRepresentation = copy.deepcopy(self.toJson())
        jsonRepresentation['signature'] = ''
        return jsonRepresentation

    

    def equals(self, transaction):
        if self.id == transaction.id:
            return True
        else:
            return False