from eth_keys import keys
from eth_utils import decode_hex
from secrets import token_bytes
from sha3 import keccak_256
import binascii


PK="0x"+keccak_256(token_bytes(32)).hexdigest()
#PK_bytes = decode_hex(PK)
PK_bytes = decode_hex("0x25b11fa19c1a45a4ab70f034fe0134271c70c68316f732dfcc83b1e275c46968")
Private_Key = keys.PrivateKey(PK_bytes)
pub_key = Private_Key.public_key
Public_Key = pub_key.to_hex()
Address_Key = pub_key.to_checksum_address()
print(Address_Key)

# print(Private_Key)
# print(Public_Key)
# print(Address_Key)