#!/usr/bin/python3

"""Query RedditAPI and print title of first 10 hot post of a subreddit"""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "custom"}
    param = {"limit": 10}

    r = requests.get(url, headers=headers, params=param)
    if (r.status_code == 200):
        data = r.json()["data"]["children"]
        for post in data:
            title = post["data"]["title"]
            print(title)
    else:
        print("None")
