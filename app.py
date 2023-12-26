from flask import Flask
from config import Secrets
from slack_sdk import WebClient
from slackeventsapi import SlackEventAdapter
from src.connector.slack_connector import SlackConnector
from src.service.game import play_game

app = Flask(__name__)

client = SlackConnector.get_slack_connection()
slack_events_adapter = SlackEventAdapter(Secrets.signing_secret,"/slack/events", app)

@app.route('/')
def home():
    return "Welcome to this Numbers Game application!"

@app.route('/game')
def game():
    moves_taken=play_game()
    send_slack_message(moves_taken)
    return "Thanks for playing the game. Please check Slack for more details."

def send_slack_message(moves_taken):
    client.chat_postMessage(text=f"You have guessed the correct number. The number of guesses taken: {moves_taken} :smile:", channel="general")

@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
  emoji = event_data["event"]["reaction"]
  client.chat_postMessage(text=f"You have reacted with this emoji: :{emoji}: ", channel="general")

if __name__ == "__main__":
    app.run(port="5500", debug=True)
