import os

class Secrets:
    signing_secret=os.getenv("SIGNING_SECRET")
    slack_bot_token=os.getenv("SLACK_BOT_TOKEN")
