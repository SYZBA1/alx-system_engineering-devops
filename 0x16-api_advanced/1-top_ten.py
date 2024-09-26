#!/usr/bin/python3
'''
    This module contains the function top_ten
'''
import requests
from sys import argv

def top_ten(subreddit):
    '''
        Returns the top ten posts for a given subreddit
    '''
    # Adding a User-Agent header for Reddit API
    headers = {'User-Agent': 'Lizzie'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    
    # Make the request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            # Get the data
            data = response.json()
            # Retrieve the top ten posts
            for post in data.get('data').get('children'):
                print(post.get('data').get('title'))
        except ValueError:
            print("Error decoding JSON")
    else:
        print("OK")  # Output when subreddit is non-existent or error occurs

if __name__ == "__main__":
    if len(argv) > 1:
        top_ten(argv[1])
    else:
        print("Please provide a subreddit name.")

