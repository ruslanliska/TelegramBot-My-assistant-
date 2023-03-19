import logging
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv()

OWM_TOKEN = os.getenv('OWM_TOKEN')
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
OPEN_AI_KEY = os.getenv('OPEN_AI_KEY')


class Logger:
    def __init__(self):
        self.filename = f'MyAssistantBot.log'
        logging.basicConfig(filename=self.filename,
                            level=logging.ERROR,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            force=True,
                            filemode='w')
