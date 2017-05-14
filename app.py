from slackeventsapi import SlackEventAdapter
from slackclient import SlackClient
import os

SLACK_VERIFICATION_TOKEN = os.environ["SLACK_VERIFICATION_TOKEN"]
slack_events_adapter = SlackEventAdapter(SLACK_VERIFICATION_TOKEN, "/slack/events")

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
CLIENT = SlackClient(SLACK_BOT_TOKEN)

port = int(os.environ.get("PORT"))



# Checks for Negative emoji's coming into the welcome channel and pops a headsup
# into the admin room
@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    event = event_data["event"]
    emoji = event["reaction"]
    message = event["item"]
    input_channel = event["item"]["channel"]
    if input_channel == "C5D5QUNLT": # this is the id for the welcome channel
        print ("input_channel")
        if emoji == "-1":
            send_to_channel = "G5DT6HCF8" # this is the id for admin-private
            output_text = "<@%s> is being negative in the <#%s>." % (event["user"], input_channel)
            CLIENT.api_call("chat.postMessage", channel=send_to_channel, text=output_text)
        else:
            return
    else:
        return

# when a user joins the slack, they are auto invited to the welcome channel,
# they are welcomed automatically. This could be expanded to provide sample rooms
@slack_events_adapter.on("member_joined_channel")
def member_joined_channel(event_data):
    event = event_data["event"]
    welcome_channel = event["channel"]
    if welcome_channel == "C5D5QUNLT":
        message = "Welcome to our Slack community <@%s>!" % event["user"]
        CLIENT.api_call("chat.postMessage", channel=welcome_channel, text=message)
    else:
        return

slack_events_adapter.start(port=port)
