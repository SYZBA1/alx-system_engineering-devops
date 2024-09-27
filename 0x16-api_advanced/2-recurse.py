#!/usr/bin/python3
"""
Contains recurse function that fetches hot post titles
from a given subreddit using recursion.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": (
            "0x16-api_advanced:project:v1.0.0 "
            "(by /u/firdaus_cartoon_jr)"
        )
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    # Make the API request
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Return None if subreddit is invalid
    if response.status_code == 404:
        return None

    # Parse the response JSON
    results = response.json().get("data")

    # Update 'after' and count values
    after = results.get("after")
    count += results.get("dist")

    # Append post titles to the hot_list
    for child in results.get("children"):
        hot_list.append(child.get("data").get("title"))

    # Recursively call the function if there are more posts
    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list

