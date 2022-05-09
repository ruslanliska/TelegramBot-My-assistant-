import logging
from pathlib import Path

import pdfplumber
from gtts import gTTS


def pdf_converter(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        logging.info("File for converting exists")
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        audio_result = gTTS(text=text, lang=language)
        logging.info("MP3 file converted")
        return audio_result
    else:
        logging.error("File for convertion not found")
