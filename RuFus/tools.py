
import xmltodict
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from langchain_core.tools import tool
from .utils import save_to_json

# This method checks for the content in all possible sitemap extensions and tries to fetch the content from it.
# If sitemap not found it will fetch content from the website homepage
# Once the content is obtained it will push the content to pinecone (push_to_pinecone function)
@tool
def get_sitemap(url):
  '''
  This method checks for the content in all possible sitemap extensions and tries to fetch the content from it.
  If sitemap not found it will fetch content from the website homepage
  Once the content is obtained it will push the content to pinecone (push_to_pinecone function)
  '''

  result = urlparse(url)
  if not all([result.scheme, result.netloc]):
    raise ValueError("Not a valid url")

  # Utility function (don't change)
  def get_content(url):
    try:
      response = requests.get(url)
      response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
      print(f"Sitemap found at {url}")
      return response.text
    except requests.RequestException as e:
      print(f"Failed to fetch data from {url}: {e}")
      return None

  # Utility function (don't change)
  def get_text_from_url(urls):
    for url in urls: #[xyz/sitemap_index.xml", "xyz/sitemap.html" and "xyz/sitemap.xml"
      response = get_content(url)
      if response:
        return response
    print("All provided URLs failed.")
    return None

  # Utility function (don't change)
  def find_list_in_nested_dict(input_dict):
    for key, value in input_dict.items():
        if isinstance(value, list):
            return value
        elif isinstance(value, dict):
            # Recursively search in nested dictionaries
            result = find_list_in_nested_dict(value)
            if result is not None:
                return result
    return None

  urls = [url+"/sitemap_index.xml", url+"/sitemap.html", url+"/sitemap.xml"]
  url_list = [url]
  content =  get_text_from_url(urls)
  if content is not None:
    sitemap = xmltodict.parse(content)
    found_list = find_list_in_nested_dict(sitemap)
    if found_list:
        url_list.extend([url['loc'] for url in found_list])
  return url_list