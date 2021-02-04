#!/usr/bin/python3
"""Reddit API returns subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Reddit API returns subscribers"""
    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit), headers={'User-agent': 'Hi'})
    if not response:
        return 0

    return(response.json().get('data').get('subscribers'))
