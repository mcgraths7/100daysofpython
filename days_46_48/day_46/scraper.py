
import requests
from bs4 import BeautifulSoup

URL = 'https://pybit.es/pages/projects.html'


def _pull_site():
    raw_site_page = requests.get(URL)
    raw_site_page.raise_for_status()
    return raw_site_page


def scrape(site):
    header_list = []
    soup = BeautifulSoup(site.text, 'html.parser')
    html_header_list = soup.select('.projectHeader')
    for header in html_header_list:
        header_list.append(header.getText())
    return header_list


def main():
    site = _pull_site()
    headers = scrape(site)
    for header in headers:
        print(header)


if __name__ == '__main__':
    main()