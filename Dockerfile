FROM python

WORKDIR /TelegramBot-My-assistant

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]