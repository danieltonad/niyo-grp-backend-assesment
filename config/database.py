import os
from pymongo import MongoClient
from settings import settings

# initiate database connection
client = MongoClient(settings.DB_CONNECTION_STR)


db = client.niyo_group_task_db

# users collection
users_db =  db['users']
users_db.create_index("username", unique=True)

# tasks collection
tasks_db =  db['tasks']
# Create a compound unique index on user_id and title
tasks_db.create_index([("user_id", 1), ("title", 1)], unique=True)