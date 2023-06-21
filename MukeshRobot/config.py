# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/MukeshRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "26405281" # integer value, dont use ""
    API_HASH = "77b54622ef8e0fd15555d939fc74005d"
    TOKEN = "6164258122:AAHKqHRAi-p118EOrA9g9e6HF_v7e1U0Y30"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = "6058139652" # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "jashan_bal69x"
    SUPPORT_CHAT = "Xd_Bots_Support"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001655270746
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001655270746
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://sano07:sano07@cluster0.jxywgnn.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://ldgvebhopozkzy:6f707efe3a3f37f50c23bd64dde30d0037792810f04c742b0e3c1b9e523d681c@ec2-54-227-169-170.compute-1.amazonaws.com:5432/degk50kfgf6dn0"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "p08bVWlSmVyT~X_g11gqlbLnaJul4qh52OcVaJ8RAwAD4C~I91caPwL1hRH6Id_c"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "5875450498")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "6204994197")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "2145093972")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "5649200762")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = "https://t.me/itz_legend_coder" # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "D0ZCZ67KL8OTL0PY"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "5LB4TAKPEKZ0"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        ""  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
