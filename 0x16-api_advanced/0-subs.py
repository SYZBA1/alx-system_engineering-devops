#!/usr/bin/python3
"""
Script that queries the number of subscribers for a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": (
            "python:subreddit.subscriber.counter:v1.0 "
            "(by u/<your-username>)"
        )
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except Exception:
        return 0


if __name__ == "__main__":
    # Ensure the function prints the result for correct output capture
    print(number_of_subscribers("python"))  # Test with an existing subreddit
    print(number_of_subscribers(
        "nonexistingsubreddit"))  # Test with a non-existing subreddit

