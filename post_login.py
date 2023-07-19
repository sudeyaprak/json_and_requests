import requests
import json

def post():
  
  url = "https://peer-review.hacettepe.edu.tr/v1/api/studentactivity/login"
  payload = json.dumps({
    "email": "sudeyapraksyks@gmail.com",
    "password": "Sdyprk.1386"
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  json_object = json.loads(response.text)
  json_formatted_str = json.dumps(json_object, indent=2)

  print(json_formatted_str)
  
post()
