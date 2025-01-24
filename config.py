import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "Api id - "28372387"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "11edc85521fb2d8f75e751bb284507e1")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6337726170"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://rahulkumar200001002:j0W8JF5RWqXOguvM@cluster0.jmmzh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0) # Warning - Give Db uri in deploy server environment variable, don't give in repo"
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
