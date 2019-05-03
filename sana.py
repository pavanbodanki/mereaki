import requests
import json

url = 'https://api.ciscospark.com/v1/rooms'

headers = {
	"Authorization": "Bearer YOUR_TOKEN_HERE",
	"Content-Type": "application/json"
	}

payload = {
	"title": "New Room Name"
	}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.json())