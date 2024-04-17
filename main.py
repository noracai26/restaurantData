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
    # print(response.json())

if __name__ == "__main__":
    get_restaurants()