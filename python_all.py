import json
import requests
import folium
from folium.plugins import MarkerCluster
import pandas as pd

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
      

def folium_map():
  
  url = "https://peer-review.hacettepe.edu.tr/v1/api/studentactivity?UserId=36f8374a-de3b-43f1-8f8d-d990e2fc1f18"

  payload = {}
  headers = {}

  response = requests.request("GET", url, headers=headers, data=payload)
  json_object = json.loads(response.text)
  json_formatted = json.dumps(json_object, indent=5)

  y = json.loads(json_formatted)

  #Define coordinates of where we want to center our map
  boulder_coords = [39.945883127819485, 32.686883879941405]

  #Create the map
  my_map = folium.Map(location = boulder_coords, zoom_start = 12)

  for i in y:
    print("Coordinates (lat/lon):", i['activityLatitude'], i['activityLongitude'])
    new_point = [i['activityLatitude'], i['activityLongitude']]
    folium.Marker(new_point, popup = i['activityType']).add_to(my_map)

  return my_map

post()
get()
folium_map()
