from gtts import gTTS
import pdfplumber
from pathlib import Path
import logging


def pdf_converter(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        logging.info("File for converting exists")
        print("AAAA")
    else:
        logging.error("File for convertion not found")
        print("aaaaa")


print(pdf_converter(file_path='/home/ruslan/PycharmProjects/MyAssistantBot/sample.pdf'))
