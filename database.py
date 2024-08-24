from pymongo import MongoClient, errors
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client.get_database()
url_collection = db.urls

def check_mongodb_connection():
    try:
        # Perform a simple operation to check if the database is accessible
        client.admin.command('ping')
        return True
    except errors.PyMongoError as e:
        print(f"MongoDB Connection Error: {e}")
        return False