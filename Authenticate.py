#! /usr/bin/env python3

import praw
import os

def authenticate():
    print('Authenticating...')
    reddit = praw.Reddit('tytbot')
    print('Authenticated as {}'.format(reddit.user.me()))

    return reddit
