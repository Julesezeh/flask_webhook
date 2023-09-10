import requests,json



requests.post("http://127.0.0.1:5000/", headers={"Content-type":"application/json"},data=json.dumps({"name":"Thomas","mat_number":"ENG1793812"}))