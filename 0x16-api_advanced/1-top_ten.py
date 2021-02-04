#!/usr/bin/python3
""" My """

import requests


def top_ten(subreddit):
    """ My """
    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit), headers={'User-agent': 'Hi'})
    if not response:
        print("None")
    else:
        Iter = 0
        while Iter < 10:
            print(response.json().get('data').get('children')[Iter].get('data')
                  .get('title'))
            Iter += 1
