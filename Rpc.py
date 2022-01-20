import requests
import json
from eth_account import Account
from eth_keys import KeyAPI
from eth_utils import to_wei,big_endian_to_int ,remove_0x_prefix
from sha3 import keccak_256

class network:
    def __init__(self,Address):
        self.session = requests.Session()
        self.url = "https://rinkeby.infura.io/v3/baebc9ef83e04e45aba18fb46a5ed675"
        #self.url = "https://rinkeby.infura.io/v3/"+Infura_id
        self.headers = {'Content-type': 'application/json'}
        self.Address =Address


    def get_balance(self):
      # Get the balance
        params = [self.Address, "latest"]

        data = {"jsonrpc": "2.0", "method": "eth_getBalance","params": params, "id": 1}
        
        try:
            response = self.session.post(self.url, json=data, headers=self.headers)
            Balance_wei  = response.json().get("result")
            return Balance_wei
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)
       

    def gas_Price(self):
        data = {"jsonrpc": "2.0", "method": "eth_gasPrice", "params": [], "id":1}
        response = self.session.post(self.url, json=data, headers=self.headers)

        # Check if response is valid
        try:
            # Get result of the request and decode it to decimal
            gasPriceHex = response.json().get("result")
            gasPriceDecimal = int(gasPriceHex, 16)
            return gasPriceDecimal
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)

  
    def get_Latest_Block(self):

        # Set params and prepare data
        blockNumber = "latest"
        # Boolean indicating if we want the full transactions (True) or just their hashes (false)
        fullTrx = False
        params = [ blockNumber, fullTrx]
        data = {"jsonrpc": "2.0", "method": "eth_getBlockByNumber","params": params, "id": 1}
        
        try:
            response = self.session.post(self.url, json=data, headers= self.headers)
            # Get the block
            block = response.json().get("result")
            # Get the transactions contained in the block
            transactions = block.get("transactions")
            return transactions
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)

    def eth_getTransactionByHash(self):

        transactions = self.get_Latest_Block(self.Address)
        params = [transactions[0]]
        data = {"jsonrpc": "2.0", "method": "eth_getTransactionByHash","params": params, "id": 3}

        try:
            response = self.session.post(self.url, json=data, headers= self.headers)
            transaction = response.json().get("result")
            return transactions
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)
 
        # Handle Error
    def get_nonce(self):

        # Get the nonce at the latest block
        params = [self.Address, "latest"]

        data = {"jsonrpc": "2.0", "method": "eth_getTransactionCount","params": params, "id": 3}

        
        try:
            response = self.session.post(self.url, json=data, headers= self.headers)
            nonce = response.json().get("result")
            return nonce
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)


    def send_transaction(self,signed_txn):

        params = [signed_txn.rawTransaction.hex()]
        # Create our transaction
        data = {"jsonrpc": "2.0", "method": "eth_sendRawTransaction","params": params, "id": 4}

        try:
            response = self.session.post(self.url, json=data, headers= self.headers)
            receipt = response.json().get("result")
            return receipt
        except requests.exceptions.HTTPError as e:
            return "Error: " + str(e)
   








