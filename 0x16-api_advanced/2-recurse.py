#!/usr/bin/python3
""" Recursive to returns a list titles of all hot articles """


import requests

def recurse(subreddit, hot_list=[], after=None):
    """ Recursive to returns a list titles of all hot articles """

    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={'User-agent': 'your bot 0.1'}, params={'after': after})

    if not response:
        return (None)
    else:
        response_request = response.json().get('data').get('children')

        for json_dict in response_request:
            hot_list.append(json_dict.get('data').get('title'))

        if response.json().get('data').get('after') is not None:
            after = response.json().get('data').get('after')
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
