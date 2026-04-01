import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")

headers = {
    "X-USER-TOKEN": TOKEN
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# TODO-1: Create User, you have to comment this out, else it will fail the next time you start the project
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# TODO-2: Create a Graph, you have to comment this out, else it will fail the next time you start the project
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# # https://pixe.la/v1/users/{USERNAME}/graphs/graph1.html
# graph_config = {
#     "id": "graph1",
#     "name": "Sleep Graph",
#     "unit": "h",
#     "type": "float",
#     "color": "kuro"
# }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# TODO-3: Add a Pixel to the Habit Tracker
# pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

# pixel_data = {
#     "date": "20260331", # YYYYMMDD
#     "quantity": "6.5"
# }

# with datetime
# today = datetime.now().strftime("%Y%m%d")

# pixel_data = {
#     "date": today,
#     "quantity": "6.5"
# }

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# TODO-4: Update a Pixel in the Habit Tracker
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20260331" # Update Pixel created on 31.03.2026

# update_data = {
#     "quantity": "7"
# }

# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

# TODO-5: Delete a Pixel in the Habid Tracker
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20260331" # Delete Pixel created on 31.03.2026

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

# TODO-6: Delete the Graph
# grap_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

# response = requests.delete(url=grap_delete_endpoint, headers=headers)
# print(response.text)