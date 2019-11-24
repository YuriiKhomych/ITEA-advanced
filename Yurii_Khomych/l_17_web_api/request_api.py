import requests

post_response = requests.put("http://127.0.0.1:5000/1", data={"data": "todo title"})
response = requests.get("http://127.0.0.1:5000/1")
