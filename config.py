import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27512723"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c082258db291ce736ade4d40d6681385")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://mohammedabdarzakeissa:PP1JphKhE5sJJa7x@cluster0.n7zkkwa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
