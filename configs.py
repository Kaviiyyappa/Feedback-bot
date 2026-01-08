import os

class Config(object):

    API_ID = int(os.environ.get("API_ID", 36464925))

    API_HASH = str(os.environ.get("API_HASH", "942f6440a3ab83321135d7c1927aba0a"))

    BOT_TOKEN = str(os.environ.get("BOT_TOKEN", "8518141013:AAFeviG1vD59bequrumg1L9RFPrSAlVp7Ng"))
    
    OWNER_ID = int(os.environ.get("OWNER_ID", 8422190094))

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    START = str(os.environ.get("START_TEXT", ""))

    HELP = str(os.environ.get("HELP_TEXT", ""))

    DONATE = str(os.environ.get("DONATE_TEXT", "t.me/IKBRYTBOTZ"))

    DONATE_LINK = str(os.environ.get("DONATE_LINK", "https://t.me/IKBRYTBOTZ"))

    UPDATE_CHANNEL = str(os.environ.get("UPDATE_CHANNEL", "https://t.me/HeimanSupports"))

    SUPPORT_GROUP = str(os.environ.get("SUPPORT_GROUP", "https://t.me/HeimanSupport"))

    DB_URL = str(os.environ.get("DB_URL", "mongodb+srv://Sasuke_db_user:UI9EuEPlxYFzq3FG@cluster0.ewoo4eq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))
    
    DB_NAME = str(os.environ.get("DB_NAME", "feedback_bot"))
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003386075651"))

    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))


