from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

def get_db_connection():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]  # מסד נתונים
    return db[COLLECTION_NAME]  # אוסף של פוסטים חברתיים