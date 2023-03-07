import requests
import json

webhook_url = "http://127.0.0.1:5000/webhook"
data = {"msg_id":95248,"user":"Jules","message":"I said, I'm a Don!"}


r =  requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})