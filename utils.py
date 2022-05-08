import logging


class Logger:
    def __init__(self):
        self.filename = f'MyAssistantBot.log'
        logging.basicConfig(filename=self.filename,
                            level=logging.ERROR,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            force=True,
                            filemode='w')
