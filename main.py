import requests

POST_CODE = "CF118AZ"
URL = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{POST_CODE}"

def get_restaurants():
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
        print(restaurants[i]["name"])
        print(restaurants[i]["address"])
        print(restaurants[i]["rating"]['starRating'])
        print(restaurants[i]["cuisines"])
        print()

if __name__ == "__main__":
    restaurant_data = get_restaurants()
    # print(restaurant_data.keys())
    # print(restaurant_data["restaurants"][0].keys())

    display_resturants(restaurant_data["restaurants"])
