import requests

BASE = "http://127.0.0.1:5000/"

data =  [
    {"name": "HOT STUFF SEE NOW", "views": 123, "likes": 590},
    {"name": "Breaking news", "views": 5678, "likes": 33330},
    {"name": "How to do something", "views": 512453453, "likes": 1200}
]

for i in range(0, len(data)):
    response = requests.put(BASE + "video/"  + str(i), data[i])
    print(response.json())

response = requests.delete(BASE + "video/0")
print(response)
response = requests.get(BASE + "video/6")
print(response.json())
