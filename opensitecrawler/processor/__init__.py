from .base import Processor
from .image_processor import ImageProcessor
from .table_processor import TableProcessor
from .text_processor import TextProcessor
from .url_processor import UrlProcessor

def process(text=None):
    repsone = Processor().__call__()