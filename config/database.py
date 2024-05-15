import os
from pymongo import MongoClient
from settings import settings

# initiate database connection
client = MongoClient(settings.DB_CONNECTION_STR)


db = client.niyo_group_task_db

# collections
users_db =  db['users']
tasks_db =  db['tasks']