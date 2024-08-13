#!/usr/bin/python3
""" Queyries the Reddit API and returns the number of subscribers"""


import requests


def number_of_subscribers(subreddit):
    """
    Queyries the Reddit API and returns the number of subscribers
    for a given subreddit. If an invalid subreddit is provided,
    the function returns 0.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        int: Number of subscribers, or 0 if invalid subreddit.
    """
    # Base URL for the Reddit API subreddit endpoint
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set up the headers to mimic a browser request
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the status code indicates success
    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        # Return 0 if the subreddit is invalid or not found
        return 0
