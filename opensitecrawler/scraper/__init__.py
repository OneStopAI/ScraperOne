from uuid import uuid4
from typing import List, Any, Optional
from pydantic import BaseModel


from .base import Scrapper
from .image_scrapper import ImageScrapper
from .table_scrapper import TableScrapper
from .text_scrapper import TextScrapper
from .url_scrapper import UrlScrapper

class Response(BaseModel):
    id: uuid4()


def scrape(url=None):
    response = Scrapper(url).__call__()
    images = ImageScrapper(response).__call__()
    tables = TableScrapper(response).__call__()
    texts = TextScrapper(response).__call__()
    urls = UrlScrapper(response).__call__()

