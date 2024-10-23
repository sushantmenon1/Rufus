from typing import Union
from .model import agent
from .utils import web_scrape
from fastapi import FastAPI

app = FastAPI()


@app.post("/scrape")
def scrape(instructions, url, openai_api_key):
    responses = agent(input=instructions, url=url, openai_api_key=openai_api_key)
    for url in responses:
        web_scrape(url=url)
