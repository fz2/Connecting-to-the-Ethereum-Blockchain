from web3 import Web3
from web3.contract import Contract
from web3.providers.rpc import HTTPProvider
import requests
import json
import time

bayc_address = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
contract_address = Web3.to_checksum_address(bayc_address)

#You will need the ABI to connect to the contract
#The file 'abi.json' has the ABI for the bored ape contract
#In general, you can get contract ABIs from etherscan
#https://api.etherscan.io/api?module=contract&action=getabi&address=0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D
with open('/home/codio/workspace/abi.json', 'r') as f:
	abi = json.load(f) 

############################
#Connect to an Ethereum node
api_url = "https://eth-mainnet.g.alchemy.com/v2/IG7wrFRmtHeqWJhetwsW7pwjQxgcRuns" #YOU WILL NEED TO TO PROVIDE THE URL OF AN ETHEREUM NODE
provider = HTTPProvider(api_url)
web3 = Web3(provider)

def get_ape_info(apeID):
	assert isinstance(apeID,int), f"{apeID} is not an int"
	assert 1 <= apeID, f"{apeID} must be at least 1"
	data = {'owner': "", 'image': "", 'eyes': "" }
	contract = web3.eth.contract(address=contract_address,abi=abi)
	data['owner']= contract.functions.ownerOf(apeID).call()

	url = f"https://gateway.pinata.cloud/ipfs/QmeSjSinHpPnmXmspMjwiXyN6zS4E9zccariGR3jxcaWtq/{apeID}"
	headers = {'accept':'application/json', 
		   'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiJjNGNhZDA5Zi02ZGU3LTQ5Y2YtYWViZC0yYTNhYTAyZDE0M2EiLCJlbWFpbCI6InpoYW5nZnpAc2Vhcy51cGVubi5lZHUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicGluX3BvbGljeSI6eyJyZWdpb25zIjpbeyJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MSwiaWQiOiJGUkExIn0seyJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MSwiaWQiOiJOWUMxIn1dLCJ2ZXJzaW9uIjoxfSwibWZhX2VuYWJsZWQiOmZhbHNlLCJzdGF0dXMiOiJBQ1RJVkUifSwiYXV0aGVudGljYXRpb25UeXBlIjoic2NvcGVkS2V5Iiwic2NvcGVkS2V5S2V5IjoiMjMwM2E0MmRlNzQ4NmQ1NDk4MzQiLCJzY29wZWRLZXlTZWNyZXQiOiJiZWZlOTQxMzYzYzM2YTkzMDZhZThkN2VjYTI2ODA5NzVhMzY1NDQ1MjRkMjk4ODgzZjJjNWNlOTZmYTdmMTQ3IiwiZXhwIjoxNzYwOTkwNTk4fQ.xD_VUJBcNaexQxl16Juh7ov0F2FDCXdjjyT51NF7BKk'}
	response = requests.get(url, headers = headers)  
	response = response.json()
	attributes = response.get('attributes')
	for attribute in attributes:
		if attribute.get('trait_type') == 'Eyes':
			data['eyes'] = attribute.get('value')	
	data['image'] = response.get('image')
	print(data)
	
	assert isinstance(data,dict), f'get_ape_info{apeID} should return a dict' 
	assert all( [a in data.keys() for a in ['owner','image','eyes']] ), f"return value should include the keys 'owner','image' and 'eyes'"
	return data

