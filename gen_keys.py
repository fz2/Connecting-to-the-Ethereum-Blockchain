from web3 import Web3
import eth_account
import os

def get_keys(challenge,keyId = 0, filename = "eth_mnemonic.txt"):
    """
    Generate a stable private key
    challenge - byte string
    keyId (integer) - which key to use
    filename - filename to read and store mnemonics

    Each mnemonic is stored on a separate line
    If fewer than (keyId+1) mnemonics have been generated, generate a new one and return that
    """
    w3 = Web3()
    msg = eth_account.messages.encode_defunct(challenge)

	#YOUR CODE HERE

    eth_addr = "0xeD2dDD618865a33291a27905592a61Bac72B2450"
    private_key = "0xcffe332d968720c6657f7895a2f237721f5c817907be2a16a0845b3557115bcd"
    sig = w3.eth.account.sign_message(msg, private_key=private_key)

    assert eth_account.Account.recover_message(msg,signature=sig.signature.hex()) == eth_addr, f"Failed to sign message properly"

    #return sig, acct #acct contains the private key
    return sig, eth_addr

if __name__ == "__main__":
    for i in range(4):
        challenge = os.urandom(64)
        sig, addr= get_keys(challenge=challenge,keyId=i)
        print( addr )
