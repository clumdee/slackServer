import os

# search for .env file with respect to the location of execution
# i.e. os.getcwd()
if os.path.exists("../.env"):
    from dotenv import load_dotenv
    load_dotenv(override=True)


SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")