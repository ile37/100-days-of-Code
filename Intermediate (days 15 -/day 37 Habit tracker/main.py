import requests
import datetime as dt
import os


USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_endpoint = f"{graph_endpoint}/graph1"

date = dt.datetime.now().strftime("%Y%m%d")
post_body = {
    "date": date,
    "quantity": "0.5",
}

# response = requests.post(url=post_endpoint, json=post_body, headers=headers)
# print(response.text)

put_endpoint = f"{post_endpoint}/{date}"

put_body = {
    "quantity": "0.6",
}

# response = requests.post(url=put_endpoint, json=put_body, headers=headers)
# print(response.text)

delete_endpoint = f"{post_endpoint}/{date}"

# response = requests.delete(url=delete_endpoint, headers=headers)
