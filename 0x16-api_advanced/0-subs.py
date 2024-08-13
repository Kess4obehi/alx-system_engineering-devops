#!/usr/bin/python3
"""
number of subscription for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    function that queries the reddit API and returns the number of subscribers
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    header = {'User-agent': 'MyRedditApi/0.1'}
    url = 'https://www.reddit.com/r/{}/about.json'. format(subreddit)
    response = get(url, headers=header, allow_redirects=False)
    result = response.json()

    try:
        return result.get('data').get('subscribers')

    except Exception:
        return 0
