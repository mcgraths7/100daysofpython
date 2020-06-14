
import requests

URL = "https://feed.syntax.fm/rss"

if __name__ == '__main__':
    r = requests.get(URL)
    r.raise_for_status()
    with open('syntaxepisodes.xml', 'wb') as f:
        f.write(r.content)
