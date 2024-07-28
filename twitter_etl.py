import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs
import tweepy.errors

# Your credentials

bearer_token = "AAAAAAAAAAAAAAAAAAAAAGhMvAEAAAAA9uS9Y0fWC%2BQz5phg4WS4l%2F8gNGw%3Dne38BdiHxKywuQfhPTUwER6WO8ZA3zMaQBzglXLQv8R2fvmR30"

access_key = "595770135-wxMxrWnBe5jxPycHX9XZZRRmgTl6xFbSgrGCvR80"
access_secret = "tY088xSPX3NxlhDubMwvpZ48G5n1aEhPdjTLf10uFrq9Q"
consumer_key = "DE89clj4EIBckulDd6mDK7gDc"
consumer_secret = "aSXnAA8A7mkly2N9XZinpOfoNhRN2GHFioh4JJ0yAL0Dv1XtlW"


auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_key, access_secret)

# # # Creating an API object 
api = tweepy.API(auth)
try:
    # Verify authentication
    api.verify_credentials()
    print("Authentication OK")
except tweepy.errors.TweepyException as e:
    print(f"Error during authentication: {e}")


# Fetch tweets from the user @elonmusk
try:
    username = 'elonmusk'
    tweets = api.user_timeline(screen_name=username, count=10)  # Adjust count as needed

    # Print the tweets
    for tweet in tweets:
        print(tweet.text)
except tweepy.errors.TweepyException as e:
    print(f"Error fetching tweets: {e}")