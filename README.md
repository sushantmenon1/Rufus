# Rufus Client

## Project Overview

### Problem

Retrieving useful data from websites for Retrieval-Augmented Generation (RAG) agents presents several challenges:
- Simple scraping tools can handle individual pages, but much of the valuable data resides deep within websites or across multiple linked pages.
- Collecting this data often requires building custom tools, which are prone to breaking when website structures change.

### Solution

**Rufus** is designed to address this problem by intelligently crawling websites based on user-provided input, selectively retrieving only the most relevant content. Rufus aims to:
- Synthesize structured documents from the web.
- Make it easy for engineers to plug these documents into RAG pipelines.
- Automate the process of crawling and extracting information by interpreting a user's instructions, allowing engineers to quickly retrieve data based on a brief prompt.

## Rufus Client

The Rufus Client is a Python interface that interacts with the Rufus API to scrape data from a given URL using custom instructions. The client sends requests to a locally hosted Rufus API endpoint and returns the extracted content.

### Features
- **Simple API integration**: Easy to use class-based implementation.
- **Custom scraping**: Specify your scraping instructions for each URL.
- **Automatic crawling**: The API automatically crawls and extracts data based on the input instructions.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sushantmenon1/Rufus.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Rufus
   ```
3. Install the required dependencies:
   ```bash
   pip install -e .
   ```

## Hosting the FastAPI API Locally

Before using the `RufusClient`, you need to host the FastAPI API locally. Follow these steps:

1. Ensure you have FastAPI and Uvicorn installed:
   ```bash
   pip install fastapi
   ```

2. Run the FastAPI application locally:
   ```bash
   fastapi dev RuFus/api.py
   ```

   This will start the FastAPI server at `http://127.0.0.1:8000`.

Make sure this API is running locally before you proceed with the Rufus Client.

## Usage

### Initialization

To use the Rufus Client, you need to provide your API key (which is used to interact with the Rufus backend). Initialize the client by creating an instance of the `RufusClient` class:

```python
from rufus_client import RufusClient

# Replace 'your_openai_api_key' with your actual API key
client = RufusClient(api_key='your_openai_api_key')
```

### Scraping Data

To scrape data from a URL, simply call the `scrape` method with the desired `url` and a set of `instructions`:

```python
# Define the URL and instructions for scraping
url = "https://example.com"
instructions = "Extract all paragraphs related to technology."

# Scrape the URL
scraped_data = client.scrape(url, instructions)

# Display the results
print(scraped_data)
```

### Rufus API

The Rufus Client interacts with a locally hosted Rufus API via the following endpoint:
- **POST `/scrape`**: This endpoint accepts a URL and user-provided instructions to crawl the web page and extract relevant content. The response contains the scraped content.

The data payload sent to the API includes:
- `url`: The website URL to be scraped.
- `instructions`: A brief prompt explaining what content to retrieve.
- `openai_api_key`: Your API key for authentication.

## API Example

The Rufus API expects a `POST` request to the `/scrape` endpoint in the following format:

```json
{
    "instructions": "Extract all relevant data on AI from the page.",
    "url": "https://example.com",
    "openai_api_key": "your_openai_api_key_here"
}
```

The response contains the relevant content extracted from the provided URL.

## Requirements

- Python 3.12
- A running instance of the Rufus API on `localhost`
- FastAPI and Uvicorn

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
