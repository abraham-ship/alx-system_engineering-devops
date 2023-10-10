#!/usr/bin/python3

"""
recursive function to query RedditAPI and return a list of titles
of all hot articles for a subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?"
    headers = {"User-Agent": "custom"}
    params = {"after": after}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        posts = response.json()["data"]
        for post in posts["children"]:
            title = post["data"]["title"]
            hot_list.append(title)

        after = posts["after"]
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    else:
        return None
