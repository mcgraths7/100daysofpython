
import feedparser
import sqlite3



FEED_FILE = "syntaxepisodes.xml"


def init():
    conn = sqlite3.connect('feed.db')
    c = conn.cursor()
    t = c.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name="{episodes}"''')
    print(t)
    if not t:
        c.execute('''CREATE TABLE episodes(published text, title text, link text)''')


if __name__ == '__main__':
    init()

#
# feed = feedparser.parse(FEED_FILE)
#
# for entry in feed.entries:
#     print(f"{entry.published} -- {entry.title}")
#     print(f"{entry.link}")
#     print(f"'{entry.description}'")

# TODO: Revisit this after SQLite lesson