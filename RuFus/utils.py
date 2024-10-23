import json
from bs4 import BeautifulSoup
import requests

def save_to_json(data, json_file='scraped_content.json'):
    '''
    This function appends the given data to the JSON file.
    '''
    try:
        # Read existing data from the JSON file (if it exists)
        with open(json_file, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty list
        existing_data = []
    
    # Append the new data to the existing list
    existing_data.append(data)
    
    # Write the updated data back to the JSON file
    with open(json_file, 'w') as file:
        json.dump(existing_data, file, indent=4)

def web_scrape(url):
  '''
  This fucntion is used to scrap the given url page and return all the contents present on the webpage.
  '''

  soup = BeautifulSoup(requests.get(url).content, 'html.parser')
  text = soup.get_text(separator='\n', strip=True).split('\n')
  content = " ".join([i for i in text if len(i.split()) > 3])
  return content