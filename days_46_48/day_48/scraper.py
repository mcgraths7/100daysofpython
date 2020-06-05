
import webbrowser
import requests
from bs4 import BeautifulSoup
from collections import namedtuple

BASE_URL = 'https://news.ycombinator.com'
URL = f'{BASE_URL}/submitted?id=whoishiring'
Post = namedtuple('Post', 'title, link')


def base_scrape(url):
    site = requests.get(url)
    site.raise_for_status()

    soup = BeautifulSoup(site.text, 'html.parser')
    stories = soup.select('.storylink')
    hiring_this_year = [story for story in stories if "Who is hiring" in story.string and "2020" in story.string]
    posts = []
    for post in hiring_this_year:
        posts.append(Post(title=post.string, link=f"{BASE_URL}/{post['href']}"))
    return posts


def month_scrape(url):
    site = requests.get(url)
    site.raise_for_status()

    soup = BeautifulSoup(site.text, 'html.parser')
    posts = [post.getText() for post in soup.select('.commtext') if "|" in post.getText()]
    return posts


def filter_posts_by_keywords(keywords, posts):
    matches = [post for post in posts for keyword in keywords if keyword.lower() in post.lower()]
    return matches


def main():
    posts = base_scrape(URL)
    for idx, post in enumerate(posts, 1):
        print(f"{idx}: {post.title} -- {post.link}")
    inp = input("Which thread would you like to open? ")
    monthly_posts = month_scrape(f"{posts[int(inp) - 1].link}")
    keywords = ['python', 'django', 'flask']
    # TODO: Make this user input, just using default values for now
    matches = filter_posts_by_keywords(keywords, monthly_posts)
    junior_matches = filter_posts_by_keywords(['junior'], matches)
    # for idx, jm in enumerate(junior_matches, 1):
    #     print(f"{idx}. \n {jm}")
    for idx, m in enumerate(matches, 1):
        print(f"{idx}. \n {m}")


if __name__ == '__main__':
    main()
