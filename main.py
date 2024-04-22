import requests

POST_CODE = "CF118AZ"
URL = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{POST_CODE}"

GREEN = '\033[92m'
ORANGE = '\033[38;5;208m'
RED = '\033[91m'
RESET = '\033[0m'

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
        # Print name
        name = restaurants[i]["name"]
        print(f"{'Name':<10} : {name}")

        # Print address
        first_line = restaurants[i]["address"]['firstLine'].replace("\n", ", ")
        postcode = restaurants[i]["address"]['postalCode']
        city = restaurants[i]["address"]['city']
        address = f"{first_line}, {postcode}, {city}"
        print(f"{'Address':<10} : {address}")

        # Print rating
        rating = restaurants[i]["rating"]['starRating']
        count = restaurants[i]["rating"]['count']
        if rating >= 4:
            color = GREEN
        elif 3.5 <= rating < 4:
            color = ORANGE
        else:
            color = RED
        print(f"{'Rating':<10} : {color}{rating}{RESET} ({count} reviews)")

        # Print cuisines
        cuisine_names = ", ".join([cuisine['name'] for cuisine in restaurants[i]["cuisines"]])
        print(f"{'Cuisines':<10} : {cuisine_names}")

        print()

if __name__ == "__main__":
    all_data = get_data()
    display_resturants(all_data["restaurants"])
