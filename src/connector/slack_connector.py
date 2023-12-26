from config import Secrets
from slack_sdk import WebClient

class SlackConnector:
    @staticmethod
    def get_slack_connection():
        client = WebClient(token=Secrets.slack_bot_token)
        return client
