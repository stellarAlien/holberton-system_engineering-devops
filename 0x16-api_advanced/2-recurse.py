#!/usr/bin/python3
"""
Query Reddit API recursively for all hot articles of a given subreddit
"""
import requests


def hot_recursion_api(subreddit, hot_list=[], after="tmp"):
    """
       read api responses recursively
    """
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0'})
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after is not None:
        url = url + "?after={}".format(after)
    r = requests.get(url, headers=headers, allow_redirects=False)
    results = r.json().get('data', {}).get('children', [])
    if not results:
        return hot_list
    for t in results:
        hot_list.append(t.get('data').get('title'))
    after = r.json().get('data').get('after')
    if not after:
        return hot_list
    return (hot_recursion_api(subreddit, hot_list, after))
