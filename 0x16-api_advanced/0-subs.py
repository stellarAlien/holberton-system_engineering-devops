#!/usr/bin/python3
"""_summary_
        ask for subscribers of a certain subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """_summary_
    try to fetch information about subreddit
    tried to do it with praw but extra credentials are required

    Args:
        subreddit (string): subreddit in reddit

    Returns:
        _type_: 0 or nubmer of subscribers
    """
    '''
     #praw style
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)
    AppleWebKit/537.36 (KHTML, like Gecko)
    Chrome/101.0.4951.67 Safari/537.36"
    s = praw.Reddit(user_agent)
    #r = requests.get('reddit.com/r/' + subreddit)
    #if ((r.status_code % 100) == 3 or r.status_code == 404):
        #return 0
    #return s.get_subreddit(subreddit).subscribers
    '''
    if (type(subreddit) is not str):
        return(0)
    url_api = ("https://www.reddit.com/r/{}/about.json".format(subreddit))
    headers = {'user-agent': 'safari:holberton/0.1.0'}
    response = requests.get(url_api, headers=headers)
    if response.status_code != 200:
        return(0)
    return(response.json().get("data").get("subscribers"))
