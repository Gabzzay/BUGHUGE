from pymongo import MongoClient

from app.core.config import settings


client = MongoClient(
    settings.mongodb_uri,
    serverSelectionTimeoutMS=5000,
)


database = client[settings.mongodb_database]


vulnerabilities_collection = database["vulnerabilities"]