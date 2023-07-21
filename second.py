import requests


def create_folder(path):
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    token = ''
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
    response = requests.put(f'{URL}?path={path}', headers=headers)
    return response
