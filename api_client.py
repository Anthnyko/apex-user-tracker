import requests

def fetch_player_data(username: str):
    url = "https://api.mozambiquehe.re/bridge"
    params = {
        "auth": "4973253872bd045148ec24efb57927e3",
        "player": username,
        "platform": "PC"
    }

    response = requests.get(url, params=params)

    # Checking for errors
    if response.status_code != 200:
        print("Error fetching data:", response.status_code)
        return None
    
    data = response.json()

    # Defensive Check
    if "Error" in data:
        print("API returned an error:", data["Error"])
        return None
    
    return data