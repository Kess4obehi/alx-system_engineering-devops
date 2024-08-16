#!/usr/bin/python3
"""
Defines a function that querries the Reddit API and returns
the number of subscribers for a given subreddit.
"""


def number_of_subscribers(subreddit):
    """Querries the Reddit API and returns
    the number of subscribers for a given subreddit
    """
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "myUserAgent"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code >= 300:
        return 0

    subscribers = response.json().get("data").get("subscribers")
    return subscribers
