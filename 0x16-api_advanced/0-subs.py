#!/usr/bin/python3
    """_summary_ 
        ask for subscribers of a certain subreddit
    """
import praw
import requests

def number_of_subscribers(subreddit):
    s = praw.Reddit(Mozilla/5.0 (Windows NT 10.0; Win64; x64)
                AppleWebKit/537.36 (KHTML, like Gecko)
                Chrome/101.0.4951.67 Safari/537.36)
    r = requests.get('reddit.com/r/' + subreddit)
    if ((r.status_code % 100) == 3 or r.status_code == 404):
        return 0
    return s.get_subreddit(subreddit).subscribers
