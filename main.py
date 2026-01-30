import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler

load_dotenv()

slack_app = App(
  token=os.getenv("SLACK_BOT_TOKEN"),
  signing_secret=os.getenv("SLACK_SIGNING_SECRET")
)

app = Flask(__name__)
handler = SlackRequestHandler(slack_app)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port="5000")