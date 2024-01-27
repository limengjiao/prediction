import pandas as pd
import pymongo

def get_user_list():
    atlas_uri = "mongodb+srv://Sparkling:MitSummer2023@cluster0.rnnxivg.mongodb.net/"
    client = pymongo.MongoClient(atlas_uri)
    db = client["test"]
    collection_name = "users"
    collection = db[collection_name]
    projection = {
        "_id"
    }
    query = {}
    user_list = collection.find(query, projection)
    data = pd.DataFrame(list(user_list))
    if not data.empty and '_id' in data.columns:
        data['_id'] = data['_id'].apply(str)
        print(data)
    else:
        print("DataFrame is empty or doesn't contain '_id' column")
    return data

# user_ids_df = get_user_list()
# print(type(user_ids_df['_id'].iloc[0]))