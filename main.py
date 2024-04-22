import requests
from prettytable import PrettyTable

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

def extract_info(restaurant, table):
    # Extracting name
    name = restaurant["name"]
    # Extracting address
    first_line = restaurant["address"]['firstLine'].replace("\n", ", ")
    postcode = restaurant["address"]['postalCode']
    city = restaurant["address"]['city']
    address = f"{first_line}, {postcode}, {city}"
    # Extracting rating
    rating = float(restaurant["rating"]['starRating'])
    count = restaurant["rating"]['count']
    if rating >= 4:
        color_rating = f"{GREEN}{rating}{RESET}"
    elif 3 <= rating < 4:
        color_rating = f"{ORANGE}{rating}{RESET}"
    else:
        color_rating = f"{RED}{rating}{RESET}"
    rating_with_reviews = f"{color_rating} ({count} reviews)"
    # Extracting cuisine
    cuisine_names = ", ".join([cuisine['name'] for cuisine in restaurant["cuisines"]])

    # Add a row for each restaurant
    table.add_row([name, rating_with_reviews, cuisine_names, address])

def display_resturants(restaurants):
    table = PrettyTable()
    table.field_names = ["Name", "Ratings", "Cuisines", "Address"]
    table.align = "l"
    table._max_width = {"Name": 20, "Address": 40, "Rating": 15, "Cuisines": 30}
    table.hrules = 1

    for i in range(0, 10):
        extract_info(restaurants[i], table)

    print(table)

if __name__ == "__main__":
    all_data = get_data()
    display_resturants(all_data["restaurants"])
