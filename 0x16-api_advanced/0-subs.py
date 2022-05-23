#!/usr/bin/python3
"""
function that queries the Reddit API and returns
the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """ subreddit
    Args:
        subreddit (str): subreddit
    Returns:
        int: _description_
    """
    url = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "platform"},
        allow_redirects=False,
    )
    if url.status_code == 200:
        return int(url.json().get("data").get("subscribers"))
    else:
        return 0
