"""Programme parses news at BBC ukrainian."""

import requests
from bs4 import BeautifulSoup


def get_article():
    """Parse for last article and returns it."""
    bbc_request = requests.get('https://www.bbc.com/ukrainian')
    soup = BeautifulSoup(bbc_request.text, "html.parser")
    raw_article = soup.find_all('div', {'class': "bbc-1vo75s2-TextGridItem e19k1v2h0"})[0].find_all(text=True, recursive=True)

    title = raw_article[0]
    description = raw_article[1]
    publish_time = raw_article[2]
    href = soup.find_all('div', {'class': 'bbc-1vo75s2-TextGridItem e19k1v2h0'})[0].find('a', {'class': 'bbc-11m194t-Link evnt13t0'})['href']
    link = f' https://www.bbc.com/{href}'
    article = f"""⚠️ <b>Тема</b>:  {title}
                  \n📌 <b>Короткий опис</b>:  {description}
                  \n🕒 <b>Опубліковано</b>:  {publish_time}
                  \n➡️ <b>Повний текст</b>: {link}"""
    return article
