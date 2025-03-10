import requests

def get_ipinfo(ip):
    url = f"https://ip-api.com/json/{ip}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
