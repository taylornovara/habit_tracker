"""Habit Tracking using Pixela tracking the number of pages I read daily"""
import requests
import datetime

# Constants
USERNAME = "taylornovara"
TOKEN = "kj235n24n3k2ln423lk4n"
ID = "reading-graph1"
DATE = datetime.datetime.now()

user_endpoint = "https://pixe.la/v1/users"

# The required parameters to create an account on Pixela
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Creates our profile on Pixela
# response = requests.post(url=user_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{user_endpoint}/{USERNAME}/graphs'

graph_config = {
    "id": ID,
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Creates a graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

value_endpoint = f"{user_endpoint}/{USERNAME}/graphs/{ID}"

value_params = {
    "date": f"{DATE.strftime('%Y%m%d')}",
    "quantity": "1",
}

# Adds a value to the graph
# response = requests.post(url=value_endpoint, json=value_params, headers=headers)
# print(response.text)

update_value_endpoint = f"{user_endpoint}/{USERNAME}/graphs/{ID}/{DATE.strftime('%Y%m%d')}"

# Updates an existing value
# response = requests.put(url=update_value_endpoint, json=value_params, headers=headers)
# print(response.text)

delete_value_endpoint = f"{user_endpoint}/{USERNAME}/graphs/{ID}/{DATE.strftime('%Y%m%d')}"

# Deletes an existing value
# response = requests.delete(url=delete_value_endpoint, headers=headers)
# print(response.text)
