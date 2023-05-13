from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from env import SLACK_BOT_TOKEN, SLACK_APP_TOKEN

# Initializes your app with your bot token and signing secret
app = App(token=SLACK_BOT_TOKEN)

@app.command("/my_command")
def hello_command(ack, body, respond):
    user_id = body["user_id"]
    print(body)
    print(respond)
    ack(f"Hi, <@{user_id}>!")
    respond(f"{body['text']}")


if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()