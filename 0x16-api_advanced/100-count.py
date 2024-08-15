#!/usr/bin/python3
""" Recursively qurying Reddit API for count occurences"""


from collections import Counter
import re
import requests


def count_words(subreddit, word_list, word_count=None, after=None):
    """
    Recursively queries the Reddit API, counts occurrences
    of given keywords in the titles of all hot articles for
    a given subreddit, and prints a sorted count of keywords.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): List of keywords to count.
        word_count (dict): Dictionary to accumulate keyword counts.
        after (str): The "after" parameter for pagination.
    """
    if word_count is None:
        word_count = Counter()

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

        # Parse and count occurrences of keywords in titles
        for post in posts:
            title = post.get('data', {}).get('title', '')
            title_lower = title.lower()

            # Count occurrences of each keyword in the title
            for keyword in word_list:
                keyword_lower = keyword.lower()
                # Create a regex pattern to match whole words only
                pattern = re.compile(r'\b' + re.escape(keyword_lower) + r'\b')
                word_count[keyword_lower] += len(pattern.findall(title_lower))

        # Recursively call the function if there are more pages
        if after:
            return count_words(subreddit, word_list, word_count, after)
        else:
            # Print results sorted by count (descending) and alphabetically
            sorted_word_count = sorted(
                    word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_count:
                if count > 0:
                    print(f"{word} {count}")
    else:
        # If the subreddit is invalid or not found, print nothing
        pass
