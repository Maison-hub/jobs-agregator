import requests

def get_coordinates_from_api_adresse(city_name):
    url = f"https://api-adresse.data.gouv.fr/search/"
    params = {"q": city_name, "limit": 1}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data["features"]:
            coordinates = data["features"][0]["geometry"]["coordinates"]
            longitude, latitude = coordinates
            return latitude, longitude
        else:
            print("Aucune correspondance trouvée pour cette ville.")
            return None, None
    else:
        print(f"Erreur lors de la requête : {response.status_code}")
        return None, None

