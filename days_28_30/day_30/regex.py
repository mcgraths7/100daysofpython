import re

COURSE = ('Introduction 1 Lecture 01:47'
          'The Basics 4 Lectures 32:03'
          'Getting Technical!  4 Lectures 41:51'
          'Challenge 2 Lectures 27:48'
          'Afterword 1 Lecture 05:02')
TWEET = ('New PyBites article: Module of the Week - Requests-cache '
         'for Repeated API Calls - http://pybit.es/requests-cache.html '
         '#python #APIs')
HTML = ('<p>pybites != greedy</p>'
        '<p>not the same can be said REgarding ...</p>')


def extract_course_times(course=COURSE):
    """Return the course timings from the passed in
       course string. Timings are in mm:ss (minutes:seconds)
       format, so taking COURSE above you would extract:
       ['01:47', '32:03', '41:51', '27:48', '05:02']
       Return this list.
    """
    times = re.findall(r'\d{2}:\d{2}', course)
    return times
    pass


def get_all_hashtags_and_links(tweet=TWEET):
    """Get all hashtags and links from the tweet text
       that is passed into this function. So for TWEET
       above you need to extract the following list:
       ['http://pybit.es/requests-cache.html',
        '#python',
        '#APIs']
       Return this list.
    """
    # Need to capture #anything as well as http://anything.domain
    hash_pattern = re.compile(r'#\w+')
    url_pattern = re.compile(r'\bhttps?://(www\.)?[A-Za-z0-9-]+(\.[a-z]+)+(/[A-Za-z0-9-]+)*(\.[a-z]+)?\b')
    words = tweet.split(" ")
    matches = []
    for word in words:
        if url_pattern.search(word) or hash_pattern.search(word):
            matches.append(word)
    return matches
    pass


def match_first_paragraph(html=HTML):
    """Extract the first paragraph of the passed in
       html, so for HTML above this would be:
       'pybites != greedy' (= content of first paragraph).
       Return this string.
    """
    paragraph_pattern = re.compile(r'(?<=<p>)[\w\W]+?(?=</p>)')
    return paragraph_pattern.search(html).group(0)
    pass
