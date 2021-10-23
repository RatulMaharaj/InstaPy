import os
from dotenv import load_dotenv
from instapy import InstaPy

# load environment variables
load_dotenv()

# get username and password from environment
username = os.getenv("USERNAME")
pwd = os.getenv("PASSWORD")

# Start bot
session = InstaPy(username=username, password=pwd)
session.login()
session.set_dont_like(["naked", "nsfw"])
# session.set_do_like(enabled=True, percentage=67)
session.set_user_interact(amount=2, randomize=True, percentage=60, media="Photo")
session.follow_user_followers(
    ["istoreza", "uctjustkidding"],
    amount=30,
    randomize=False,
    interact=True,
)
session.end()
