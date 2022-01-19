# from web3 import Web3
# infura_url='https://mainnet.infura.io/v3/29547...' #your uri
# w3 = Web3(Web3.HTTPProvider(infura_url))

# w3.isConnected()
# import random
# import codecs
# import ecdsa
# import base64
# import time
# from sha3 import keccak_256

# def validate_signature(public_key, signature, message):
#     """Verifies if the signature is correct. This is used to prove
#     it's you (and not someone else) trying to do a transaction with your
#     address. Called when a user tries to submit a new transaction.
#     """
#     # public_key = (base64.b64decode(public_key)).hex()
#     # public_key = public_key.decode()
#     signature = base64.b64decode(signature)
#     vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1)
#     # Try changing into an if/else statement as except is too broad.
#     try:
#         return vk.verify(signature, message.encode())
#     except:
#         return False

# def sign_ECDSA_msg(private_key):
#     """Sign the message to be sent
#     private_key: must be hex

#     return
#     signature: base64 (to make it shorter)
#     message: str
#     """
#     # Get timestamp, round it, make it into a string and encode it to bytes
#     message = str(round(time.time()))
#     bmessage = message.encode()
#     sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
#     signature = base64.b64encode(sk.sign(bmessage))
#     return signature, message
# #from secp256k1 import PrivateKey
# # bits = random.getrandbits(256)

# # bits_hex = hex(bits)

# # private_key = bits_hex[2:]

# # #privkey = ecdsa.Private_key(bytes(bytearray.fromhex(private_key)), raw=True)


# # SECP256k1 is the Bitcoin elliptic curve
# sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
# private_key = sk.to_string().hex()
# vk = sk.get_verifying_key()
# public_key = vk.to_string().hex()
# public_key = public_key.encode()
# addrk = keccak_256(public_key).digest()
# addr = keccak_256(public_key).digest()[-20:]
# sig=sign_ECDSA_msg(private_key)
# signature = sig[0]
# msg= sig[1]
# verify= validate_signature(public_key.decode(), signature,msg)
# print("PK  : "+private_key)
# print("Pub_k  : "+public_key.decode())
# print("k_address  : "+addrk)
# print("address  : "+addr)
# print("signature  : "+signature.hex())
# print("msg  : "+msg)
# print("verify  : "+verify)

import requests
import json
from web3 import Web3
from eth_account import Account
from eth_keys import KeyAPI
from eth_utils import to_wei,big_endian_to_int ,remove_0x_prefix
from Transaction import Transaction
from BlockchainUtils import BlockchainUtils
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
import  binascii
from sha3 import keccak


def transaction_request(url,Value,Receiver_Address_Key):

    session = requests.Session()
    # url = "https://rinkeby.infura.io/v3/baebc9ef83e04e45aba18fb46a5ed675"
    headers = {'Content-type': 'application/json'}
    w3 = Web3(Web3.HTTPProvider(url))
    # # Check connection
    # w3.isConnected()
    # print(w3.isConnected())
    prikey ='0x25b11fa19c1a45a4ab70f034fe0134271c70c68316f732dfcc83b1e275c46968'
    acct = Account.from_key(prikey)
    # print("Address:", acct.address)
    # Prepare the data we will send
    data = {"jsonrpc": "2.0", "method": "eth_gasPrice", "params": [], "id":1}
    response = session.post(url, json=data, headers=headers)

    # Check if response is valid
    if response.ok:
        # Get result of the request and decode it to decimal
        gasPriceHex = response.json().get("result")
        gasPriceDecimal = int(gasPriceHex, 16)
    else:
        print('Error')

        # Handle Error



    # Set params and prepare data
    blockNumber = "latest"
    # Boolean indicating if we want the full transactions (True) or just their hashes (false)
    fullTrx = False
    params = [ blockNumber, fullTrx]
    data = {"jsonrpc": "2.0", "method": "eth_getBlockByNumber","params": params, "id": 1}

    response = session.post(url, json=data, headers=headers)

    # Check if response is valid
    if response.ok:
        # Get the block
        block = response.json().get("result")
        # Get the transactions contained in the block
        transactions = block.get("transactions")
    else:
        print('Error')
        # Handle Error


    params = [transactions[0]]
    data = {"jsonrpc": "2.0", "method": "eth_getTransactionByHash","params": params, "id": 3}

    response = session.post(url, json=data, headers=headers)

    if response.ok:
        transaction = response.json().get("result")
        #print(transaction)
    else:
        print('Error')
        # Handle Error




    # Get the nonce at the latest block
    params = ["0xD6d69DbB3BDcdA86F0d7309ec65e7AE369423973", "latest"]

    data = {"jsonrpc": "2.0", "method": "eth_getTransactionCount","params": params, "id": 3}

    response = session.post(url, json=data, headers=headers)

    if response.ok:
        nonce = response.json().get("result")
    else:
        print('Error')
        # Handle Error

    

    
    wallet = Wallet()


    
    transaction = wallet.createTransaction(Receiver_Address_Key, Value, nonce ,gasPriceHex )


    signed_txn = wallet.signTransaction(transaction.toJson(),prikey)
    def recover_address(data: str, signature: str) -> str:
        signature = binascii.unhexlify(remove_0x_prefix(signature))
        data = keccak(text=data)
        data = f"\\x19Ethereum Signed Message:\n{len(data)}{data}"
        data = bytes(data, 'ascii')

        # web3js outputs in rsv order
        vrs = (
            ord(signature[64:65]) - 27,
            big_endian_to_int(signature[0:32]),
            big_endian_to_int(signature[32:64]),
        )
        sig = KeyAPI.Signature(vrs=vrs)
        return sig.recover_public_key_from_msg(data).to_address()

    print(signed_txn)

    params = [signed_txn.rawTransaction.hex()]
    # Create our transaction



    data = {"jsonrpc": "2.0", "method": "eth_sendRawTransaction","params": params, "id": 4}

    response = session.post(url, json=data, headers=headers)

    if response.ok:
        receipt = response.json().get("result")
        print(receipt)
    else:
        print('Error')
        # Handle Error


url = "https://rinkeby.infura.io/v3/baebc9ef83e04e45aba18fb46a5ed675"
value = 0.00001
publi2 ="0x8cf0726Bc2f166c3F0427A199cCaDcf993B0Ff8A"

transaction_request(url, value, publi2)

# from secrets import token_bytes
# from Crypto.Signature import PKCS1_PSS
# from Transaction import Transaction
# from BlockchainUtils import BlockchainUtils
# from Crypto.Signature import PKCS1_PSS
# from Crypto.Hash import SHA512
# from ecdsa import SigningKey,VerifyingKey, SECP256k1
# from secrets import token_bytes
# import sha3, binascii
# from sha3 import keccak_256


# def key():

#     secrets256 = "25b11fa19c1a45a4ab70f034fe0134271c70c68316f732dfcc83b1e275c46968"
#     secretsKey = binascii.unhexlify(secrets256)
#     #Generate PK by ecdsa Algo for further requriments
#     SK = SigningKey.from_string(secretsKey, curve=SECP256k1)
#     print(SK.to_string().hex()) 
#     #Generate Public key by using Ecdsa Private key 
#     VK = SK.get_verifying_key()
#     print(VK.to_string().hex())
#     #Generate Address key by using Hash Algo by using Ecdsa Public Key
#     keccak = sha3.keccak_256()
#     keccak.update(VK.to_string())
#     print(  "0x"+ keccak.hexdigest()[24:])

# key()

# secret = "0x25b11fa19c1a45a4ab70f034fe0134271c70c68316f732dfcc83b1e275c46968"
# scrt= secret[2:]
# print(scrt)