import random
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

CHAT_STORAGE = [
    "mongodb+srv://Musicbot:AdvMusicBot2@cluster0.qsj1x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "mongodb+srv://Musicbot:AdvMusicBot2@cluster0.qsj1x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
]

BADMUNDA = MongoCli(random.choice(CHAT_STORAGE))
chatdb = BADMUNDA.Anonymous
chatai = chatdb.Word.WordDb
storeai = BADMUNDA.Anonymous.Word.NewWordDb  
