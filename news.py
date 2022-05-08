import requests
from bs4 import BeautifulSoup


class BotArticles:
    @staticmethod
    def get_article():
        """Parse for last article and returns it."""
        page = requests.get('https://www.pravda.com.ua/')
        soup = BeautifulSoup(page.content, "html.parser")

        articles = soup.find_all('div', {'class': 'article_header'})
        article_list = []
        for i in range(5):
            article = articles[i].find_all(text=True, recursive=True)
            href = soup.find_all('div', {'class': 'article_header'})[i].find('a')['href']
            link = f'https://www.pravda.com.ua{href}'
            article = f"""⚠️ <b>Тема</b>:  {article[-1]}
                      \n➡️ <b>Повний текст</b>: {link}"""
            article_list.append(article)

        return article_list
