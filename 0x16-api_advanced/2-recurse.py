#!/usr/bin/python3
"""Defines a recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles for a given subreddit
"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """a recursive function that queries the Reddit API"""
    import requests

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "myUserAgent"}

    response = requests.get(url, params={"count": count, "after": after},
                            headers=headers, allow_redirects=False)

    if response.status_code >= 400:
        return None

    hot = hot_list + [child.get("data").get("title")
                      for child in response.json().get("data")
                      .get("children")]

    information = response.json()
    if not information.get("data").get("after"):
        return hot

    return recurse(subreddit, hot, information.get("data").get("count"),
                   information.get("data").get("after"))
