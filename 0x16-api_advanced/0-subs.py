#!/usr/bin/python3

"""Querrying RedditAPI to get subscribers of a subreddit"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {"User-Agent": "custom"}

    r = requests.get(url, headers=headers)
    if (r.status_code == 200):
        return r.json()["data"]["subscribers"]
    return 0
