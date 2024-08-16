#!/usr/bin/python3
"""A function that querries a Reddit API prints the titles
of the first 10 hot posts listed for a given subreddit"""


def top_ten(subreddit):
    """querries a Reddit API prints the titles
    of the first 10 hot posts listed for a given subreddit"""
    import requests

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "myUserAgent"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code >= 300:
        print("None")

    else:
        [print(child.get("data").get("title"))
         for child in response.json().get("data").get("children")]
