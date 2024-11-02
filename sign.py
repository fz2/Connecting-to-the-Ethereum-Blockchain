import eth_account
from web3 import Web3
from eth_account.messages import encode_defunct

def sign(m):
    w3 = Web3()
    # create an eth account and recover the address (derived from the public key) and private key
    # your code here
    account = "0xdd97b1b9f46CB7806bDB6eb54704814dCb162273"
    private_key = "0x9b9dd524b0dcc2c66f8c912cc577da7708b8ae9d064d73cfbabe6ca9cb96272f"

    eth_address = account.address()  # Eth account

    # generate signature
    # your code here
    msg = 'fz'
    message = encode_defunct(text=msg)
    signed_message = w3.eth.account.sign_message(message, private_key=private_key)

    assert isinstance(signed_message, eth_account.datastructures.SignedMessage)

    return eth_address, signed_message
 