import pandas as pd
import pymongo
from .models import User

# MongoDB
def get_user_list():
    atlas_uri = "mongodb+srv://Sparkling:MitSummer2023@cluster0.rnnxivg.mongodb.net/"
    client = pymongo.MongoClient(atlas_uri)
    db = client["test"]
    collection_name = "users"
    collection = db[collection_name]
    projection = {
        "_id",
        "username"
    }
    query = {}
    user_list = collection.find(query, projection)
    data = pd.DataFrame(list(user_list))
    if not data.empty and '_id' in data.columns:
        data['_id'] = data['_id'].apply(str)
        print(data)
    else:
        print("DataFrame is empty")
    return data

# sqlite3
# Add new user to User table
def update_user(data):
    for index, row in data.iterrows():
        userObjectId = row['_id']
        username = row['username']
        
        user, created = User.objects.get_or_create(
        userObjectId=userObjectId,
        username=username
        )
        if created: 
            print(f"Added new user: {username}")
        else: 
            print(f"User already exists: {username}")

# Add model record to model table

# Add model score to model table

user_ids_df = get_user_list()
update_user(user_ids_df)
