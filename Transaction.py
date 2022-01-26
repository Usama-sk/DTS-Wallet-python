import uuid
import time
import copy
from eth_utils import to_wei
from Rpc import network

class Transaction:

    def __init__(self,senderAddressKey, recieverAddressKey,value,):
        net = network(senderAddressKey)
        self.to = recieverAddressKey
        self.nonce = net.get_nonce()
        self.gasPrice = net.gas_Price()
        self.gas = 21000
        self.value = to_wei(value,'ether')
        self.chainId = 4
        self.senderAddressKey = senderAddressKey
        self.type = "Transfer"
        self.id = uuid.uuid1().hex
        self.timesamp = time.time()
        self.signature = ''
        self.receipt =''

    
    def toJson(self):
        return self.__dict__

    def sign(self, signature):
        self.signature = str(signature)
    
    def save_receipt(self,receipt):
        self.receipt = receipt
    
    def payload(self):
        jsonRepresentation = copy.deepcopy(self.toJson())
        keys_to_remove = ['senderAddressKey', 'type','id','timesamp','signature','receipt']
        for key in keys_to_remove:
            del jsonRepresentation[key]
        return jsonRepresentation
