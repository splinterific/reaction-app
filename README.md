# Reaction_Bot

Reaction_Bot is a proof of concept created by Mark Preston. It is for personal use only. This bot monitors a room called #welcome on a personal slack and when someone joins, it welcomes them to the Slack community with a personalized message. It will then monitor the emoji's used in that room. If someone uses a thumbsdown ( :-1: ), It alerts a #admin-private channel with the user with added the emoji and the channel name.

- Python 3
- Uses the Slack events API and RTM api
- Uses the [Slack Events API adapter for Python](https://github.com/slackapi/python-slack-events-api)

## Requirements

  - Before you can use the [Events API](https://api.slack.com/events-api) you must [create a Slack App](https://api.slack.com/apps/new), and turn on [Event Subscriptions](https://api.slack.com/events-api#subscriptions) for both `reaction_added` and `member_joined_channel`.
  - These should be set as Environment variables on your machine using the following names:
  --`SLACK_VERIFICATION_TOKEN`
  --`SLACK_BOT_TOKEN`
  - I used ngrok for testing locally but this is up to your preference. You can read more about this on the [Slack Events API adapter for Python](https://github.com/slackapi/python-slack-events-api) github page.


## Setup

- setup a python3 virtual environment if you wish for your own cleanliness
- `pip3 install -r requirements.txt`
- Configure your Event Subscriptions and the url endpoint e.g.`http://111.ngrok.io/slack/events`
- Start your application with `python3 app.py`


## Issues

- Need to create a seperate config file that allows you use to use a local config instead of env variables
- Continue to fight with Heroku as at the moment it fails with the port binding and won't allow connection to the local events
- Allow a look up for the rooms rather than using the channel ID
