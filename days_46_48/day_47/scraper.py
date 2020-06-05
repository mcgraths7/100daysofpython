
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://pybit.es/pages/articles.html'




def scrape(url):
    site = requests.get(url)
    site.raise_for_status()

    soup = BeautifulSoup(site.text, 'html.parser')
    articles = soup.select('#articleList>li')
    for idx, article in enumerate(articles, 1):
        print(f"{idx}: {article.getText()}")


def main():
    scrape(BASE_URL)


if __name__ == '__main__':
    main()