import requests

class RufusClient:
    def __init__(self, api_key) -> None:
        self.api_key = api_key

    def scrape(self, url, instructions):
        # Define the endpoint URL (localhost)
        endpoint = "http://127.0.0.1:8000/scrape"  # Modify port number if needed

        # Define the data to send in the POST request
        data = {
            "instructions": instructions,
            "url": url,  
            "openai_api_key": self.api_key
        }

        # Make the POST request to the API
        response = requests.post(endpoint, json=data)

        # Check if the request was successful and print the response
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed with status code {response.status_code}")