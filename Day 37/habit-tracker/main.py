import requests
from datetime import datetime

USERNAME = "YOUR USERNAME"
TOKEN = "YOUR TOKEN"

pixela_endpoint = 'https://pixe.la/v1/users'
pixela_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameters = {
    "id": "graph1",
    "name": "Coding Frequency",
    "unit": "hours",
    "type": "int",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)


post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

# today = datetime.now()

today = datetime(year=2025, month=4, day=28)

post_pixel_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "7"
}

response = requests.put(url=post_pixel_endpoint, json=post_pixel_parameters, headers=headers)
print(response.text)

