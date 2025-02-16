from os import getenv

from pyrogram import filters
from dotenv import load_dotenv

load_dotenv()

API_ID = "9972455"
# -------------------------------------------------------------
API_HASH = "5b1fd83b698e4e6670f3dcb053eecc06"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "7699442900:AAG-G6K1J_ExrCnAYAw6MHsSjb224jMJo28")
STRING1 = getenv("STRING_SESSION", None)
DB_NAME = "ronakDB"
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Aigf:AiGFChatbot@cluster0.sqwys.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = int(getenv("OWNER_ID", "6170050819"))
BOT_ID = int(getenv("BOT_ID", "7699442900"))
SUPPORT_GRP = "Spark_Developer_Bots"
UPDATE_CHNL = "Spark_Developer_Bots"
OWNER_USERNAME = "Spark_Developer"
TIME_ZONE = "Asia/Kolkata"
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002333236341"))
# --------------------------------------------------------------
SUDOERS = list(map(int, getenv("SUDOERS", "7707866111").split()))
# --------------------------------------------------------------

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()

# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Badhacker98/ShizuChat_Bot",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
