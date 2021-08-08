from typing import Any
import requests
import json

URL  = 'http://localhost/message1/predict'
request_data = "fire"
request = json.dumps({'data': request_data})
print(request)

response = requests.get('http://localhost/message/hi')
print(response.text)

json_response = requests.post(URL, data=request)
print(json_response.text)

'''
PS C:\Users\Durga\anaconda3\fastapi_project_git\app> python .\test_api.py
{"data": "fire"}
{"message":"{'label': 0}"}
{"message":"{'label': 1}"}

'''