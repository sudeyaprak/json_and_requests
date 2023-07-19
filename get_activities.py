import requests

def get():
  
  url = "https://peer-review.hacettepe.edu.tr/v1/api/studentactivity?UserId=36f8374a-de3b-43f1-8f8d-d990e2fc1f18"

  payload = {}
  headers = {}

  response = requests.request("GET", url, headers=headers, data=payload)
  json_object = json.loads(response.text)
  json_formatted = json.dumps(json_object, indent=5)

  print(json_formatted)
  #return json_formatted

  y = json.loads(json_formatted)
  for i in y:
    print("Coordinates (lat/lon):", i['activityLatitude'], i['activityLongitude'])
    
get()
