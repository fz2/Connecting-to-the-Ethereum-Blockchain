import requests
import json

def pin_to_ipfs(data):
    assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
    headers = {'accept':'application/json', 
		   'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiJjNGNhZDA5Zi02ZGU3LTQ5Y2YtYWViZC0yYTNhYTAyZDE0M2EiLCJlbWFpbCI6InpoYW5nZnpAc2Vhcy51cGVubi5lZHUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicGluX3BvbGljeSI6eyJyZWdpb25zIjpbeyJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MSwiaWQiOiJGUkExIn0seyJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MSwiaWQiOiJOWUMxIn1dLCJ2ZXJzaW9uIjoxfSwibWZhX2VuYWJsZWQiOmZhbHNlLCJzdGF0dXMiOiJBQ1RJVkUifSwiYXV0aGVudGljYXRpb25UeXBlIjoic2NvcGVkS2V5Iiwic2NvcGVkS2V5S2V5IjoiMjMwM2E0MmRlNzQ4NmQ1NDk4MzQiLCJzY29wZWRLZXlTZWNyZXQiOiJiZWZlOTQxMzYzYzM2YTkzMDZhZThkN2VjYTI2ODA5NzVhMzY1NDQ1MjRkMjk4ODgzZjJjNWNlOTZmYTdmMTQ3IiwiZXhwIjoxNzYwOTkwNTk4fQ.xD_VUJBcNaexQxl16Juh7ov0F2FDCXdjjyT51NF7BKk'}
    response = requests.post('https://api.pinata.cloud/pinning/pinJSONToIPFS', json = data, headers = headers)
    cid = response.json()
    print(cid)
    return cid
