from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb+srv://arnav:9VUZ78czRcevJm7m@cluster0.cdpuq5t.mongodb.net/?appName=Cluster0"

client = AsyncIOMotorClient(MONGO_URL)

db = client.expense_db

expense_collection = db.expenses

log_collection = db.logs

#PASSSWORD
#9VUZ78czRcevJm7m