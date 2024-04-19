import requests
import json

POST_CODE = "CF118AZ"
URL = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{POST_CODE}"

def get_data():
    print(URL)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(URL, headers=headers)
    if response.status_code != 200:
        print("Error code: ", response.status_code)
        print("Error message: ", response.reason)
        raise Exception(response.reason)
    return response.json()

def display_resturants(restaurants):
    for i in range(0, 10):
        print("Name: " + restaurants[i]["name"])

        firstLine = restaurants[i]["address"]['firstLine']
        postcode = restaurants[i]["address"]['postalCode']
        city = restaurants[i]["address"]['city']
        print("Address: " + firstLine + ", " + postcode + ", " + city)

        rating = restaurants[i]["rating"]['starRating']
        count = restaurants[i]["rating"]['count']
        print(f"Rating: {rating} ({count} reviews)")

        cuisineNames = [cuisine['name'] for cuisine in restaurants[i]["cuisines"]]
        print("Cuisines: " + ", ".join(cuisineNames))

        print()

if __name__ == "__main__":
    all_data = get_data()
    # print(all_data.keys())
    # print(all_data['restaurants'][0].keys())
    display_resturants(all_data["restaurants"])
    print(all_data['restaurants'][0]['address'].keys())
