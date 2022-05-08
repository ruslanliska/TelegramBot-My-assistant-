"""Programme parses news at BBC ukrainian."""

import requests
from bs4 import BeautifulSoup


def get_article():
    """Parse for last article and returns it."""
    page = requests.get('https://www.pravda.com.ua/')
    soup = BeautifulSoup(page.content, "html.parser")

    articles = soup.find_all('div', {'class': 'article_header'})[0].find_all(text=True, recursive=True)

    href = soup.find_all('div', {'class': 'article_header'})[0].find('a')['href']
    link = f'https://www.pravda.com.ua{href}'
    print(link)
    article = f"""⚠️ <b>Тема</b>:  {articles[0]}
                  \n➡️ <b>Повний текст</b>: {link}"""
    return article
