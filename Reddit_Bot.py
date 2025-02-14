import praw
import time
import os

# Load environment variables from GitHub Actions (dotenv is not needed here)
client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')
user_agent = os.getenv('REDDIT_USER_AGENT')
username = os.getenv('REDDIT_USERNAME')
password = os.getenv('REDDIT_PASSWORD')

# Ensure all environment variables are loaded
if not all([client_id, client_secret, user_agent, username, password]):
    raise ValueError("❌ Missing Reddit credentials! Make sure all environment variables are set.")

# Initialize the Reddit instance
try:
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
        username=username,
        password=password
    )
    print("✅ Successfully connected to Reddit!")
except Exception as e:
    print(f"❌ Error connecting to Reddit: {e}")
    exit(1)

# Referral code and link
referral_code = '10593047414a78f6'
referral_link = 'https://www.backmarket.com/en-us/refer-friend-welcome'

# Title and body of the post
post_title = f"💰 Get $25 Off on Back Market - {referral_code}"
post_body = (
    f"Say thanks! You now have $25.00 to spend on Back Market with this code: **{referral_code}**\n\n"
    f"Choose from thousands of professionally refurbished electronics and appliances at up to 70% off!\n\n"
    f"[Click here to claim your discount]({referral_link})"
)

# Specify the subreddit where you want to post
subreddit_name = 'Backmarket'

# Function to create the post with error handling
def create_post():
    try:
        subreddit = reddit.subreddit(subreddit_name)
        submission = subreddit.submit(post_title, selftext=post_body)
        print(f"✅ Successfully posted to r/{subreddit_name}: {submission.shortlink}")
    except Exception as e:
        print(f"❌ Error posting to r/{subreddit_name}: {e}")

# Run the bot every 6 hours
while True:
    create_post()
    time.sleep(21600)  # Sleep for 6 hours (21600 seconds)
