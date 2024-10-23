from typing import Union
from .model import gpt_agent
from .utils import web_scrape
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for the input data
class ScrapeRequest(BaseModel):
    instructions: str
    url: str
    openai_api_key: str

@app.post("/scrape")
def scrape(request: ScrapeRequest):
    responses = gpt_agent(instructions=request.instructions, url=request.url, openai_api_key=request.openai_api_key)
    data = {}
    for url in responses:
        content = web_scrape(url=url)
        data[url] = content
    return data
