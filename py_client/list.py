import requests
from getpass import getpass

username = input('username: ')
password = getpass('password: ')

auth_endpoint = "http://127.0.0.1:8000/api/auth/"
auth_response = requests.post(auth_endpoint, json={
    'username': username, 
    'password': password
})

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization': f'Bearer {token}'
    }

    endpoint = "http://127.0.0.1:8000/api/products/"
    response = requests.get(endpoint, headers=headers)
    print(response.json())