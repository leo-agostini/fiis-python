from typing import Union
from fastapi import FastAPI
import asyncio

from .infra.service.PyppeteerFiiScrappingService import PyppeteerFiiScrappingService

app = FastAPI()

@app.get("/")
async def read_root():
    fiis = await PyppeteerFiiScrappingService.scrapFiis()
    print(fiis)
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}