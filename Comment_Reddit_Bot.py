#! /usr/bin/env python3

import praw
import time
import os
from Authenticate import authenticate

# Subreddit applied to

sub = 'Put subreddit here'

# Reply Messages

message_1 = '''*Insert message here.* You can use YAML and \n\n
            For a new line'''

# Dictionary of phrases bot itirates through

phrases = { 'test' : message_1 , 'phrase' : message_1 }

def comment_bot(r, comments_replied):
    print('Starting bot...')

    for key in phrases.keys(): # iterates thru keys in phrases dictionary

        for comment in r.subreddit(sub).comments(limit=10):
            if key.lower() in comment.body.lower() and comment.id not in comments_replied and comment.author != r.user.me():
                comment.reply(phrases[key]) # replies with value from phrases dictionary
                print('Replied to comment ' + comment.id)

                comments_replied.append(comment.id)

                with open('comments_replied.txt', 'a') as f:
                    f.write(comment.id + '\n')


    print('Will start up again in 5 seconds...')
    time.sleep(5)  # sleep for 5 seconds

def saved_comments():
    if not os.path.isfile('comments_replied.txt'):
        comments_replied = []
    else:
        with open('comments_replied.txt', 'r') as f:
            comments_replied = f.read()
            comments_replied = comments_replied.split('\n')
            comments_replied = filter(None, comments_replied)
            comments_replied = list(comments_replied)

    return comments_replied

def main():
    reddit = authenticate()
    comments_replied = saved_comments()

    while True:
        comment_bot(reddit, comments_replied)


if __name__ == '__main__':
    main()
