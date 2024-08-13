#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit. If the subreddit
    is invalid, prints None.

    Args:
        subreddit (str): The subreddit to query.
    """
    # Base URL for the Reddit API subreddit's hot posts endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set up the headers to mimic a browser request
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the status code indicates success
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        # Print the titles of the first 10 hot posts
        for post in posts:
            print(post.get('data', {}).get('title'))

    else:
        # Print None if the subreddit is invalid or not found
        print(None)
