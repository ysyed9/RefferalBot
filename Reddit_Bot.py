import praw
import time
import random
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Your Reddit credentials (from .env file)
client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')
user_agent = os.getenv('REDDIT_USER_AGENT')
username = os.getenv('REDDIT_USERNAME')
password = os.getenv('REDDIT_PASSWORD')

# Initialize the Reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username=username,
                     password=password)

# Referral code and link
referral_code = '10593047414a78f6'
referral_link = 'https://www.backmarket.com/en-us/refer-friend-welcome'

# Title and body of the post
post_title = f"25$ off code - {referral_code}"
post_body = f"Say thanks! You now have $25.00 to spend on Back Market with this code: {referral_code} Choose from thousands of professionally refurbished electronics and appliances at up to 70% off! {referral_link}"

# Specify the subreddit where you want to post
subreddit_name = 'Backmarket'
subreddit = reddit.subreddit(subreddit_name)

# Function to create the post
def create_post():
    subreddit.submit(post_title, selftext=post_body)
    print(f"Posted to r/{subreddit_name}: {post_title}")

# Run the bot every 6 hours
while True:
    create_post()
    time.sleep(21600)  # Sleep for 6 hours (21600 seconds)
