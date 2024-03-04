from requests import request
from json import loads

URL = "https://aves.ninjas.cl/api/birds"

payload = {}
headers = {}

response = request("GET", URL, headers = headers, data = payload)
print(loads(response.text))

print("status:", response.status_code)
dicc_posts= loads(response.text)
#print(dicc_posts)
