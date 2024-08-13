#!/usr/bin/python3
"""Recursively queries the Reddit API and returns a list """


import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of
    titles of all hot articles for a given subreddit. If the
    subreddit is invalid, returns None.

    Args:
        subreddit (str): The subreddit to query.
        hot_list (list): The list to accumulate the titles of hot posts.
        after (str): The "after" parameter for pagination.

    Returns:
        list: A list of titles of all hot articles,
        or None if invalid subreddit.
    """
    # Base URL for the Reddit API subreddit's hot posts endpoint
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set up the headers to mimic a browser request
    headers = {'User-Agent': 'Mozilla/5.0'}
    # Parameters to handle pagination
    params = {'after': after, 'limit': 100}

    # Make the request to the Reddit API
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

    # Check if the status code indicates success
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        after = data.get('data', {}).get('after')

        # Accumulate the titles of the hot posts
        hot_list.extend([post.get('data', {}).get('title') for post in posts])

        # If there's more data to fetch, recursively call the function
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        # Return None if the subreddit is invalid or not found
        return None
