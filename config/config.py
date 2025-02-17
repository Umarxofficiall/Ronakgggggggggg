from os import getenv

from pyrogram import filters
from dotenv import load_dotenv

load_dotenv()

API_ID = ""
# -------------------------------------------------------------
API_HASH = ""
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "")
STRING1 = getenv("STRING_SESSION", None)
DB_NAME = "ronakDB"
MONGO_URL = getenv("MONGO_URL", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
BOT_ID = int(getenv("BOT_ID", ""))
SUPPORT_GRP = "" #username
UPDATE_CHNL = ""#username
OWNER_USERNAME = ""#username
TIME_ZONE = "Asia/Kolkata"
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "")
# --------------------------------------------------------------
SUDOERS = list(map(int, getenv("SUDOERS", "").split()))
# --------------------------------------------------------------

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()

# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Umarxofficiall/Ronakgggggggggg",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
