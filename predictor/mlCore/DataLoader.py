import pandas as pd
import pymongo
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from bson import ObjectId
import datetime
from dateutil import parser

def get_collection_data(user_type_id):
    atlas_uri = "mongodb+srv://Sparkling:MitSummer2023@cluster0.rnnxivg.mongodb.net/"
    client = pymongo.MongoClient(atlas_uri)
    db = client["test"]
    collection_name = "sugarintakes"
    collection = db[collection_name]
    projection = {
        "user": 1,
        "food": 1,
        "date": 1,
    }
    query = {"user": ObjectId(user_type_id)}
    intake_data = collection.find(query, projection)
    data = pd.DataFrame(list(intake_data))
    
    if data.empty or 'date' not in data.columns:
        print(f"No data available for user {user_type_id}.")
        return pd.DataFrame()
    return data

def retrieve_data(user_type_id):
    data = get_collection_data(user_type_id)
    if data.empty:
        print(f"No data available for user {user_type_id}.")
        return pd.DataFrame()

    data['datetime'] = pd.to_datetime(data['date'])
    data['weekday'] = data['datetime'].dt.weekday
    data['hour'] = data['datetime'].dt.hour
    # print("Data: " + data.to_string())
    # print("Data types:\n", data.dtypes)
    return data

def retrieve_data_week(user_type_id):
    data = get_collection_data(user_type_id)
    if data.empty:
        print(f"No data available for user {user_type_id}.")
        return pd.DataFrame()
    
    data['datetime'] = data['date'].apply(lambda x: parser.isoparse(x).replace(tzinfo=None))
    now = datetime.datetime.now().replace(hour=3, minute=0, second=0, microsecond=0)
    
    start_cur_week = now - datetime.timedelta(days=now.weekday())
    end_cur_week = start_cur_week + datetime.timedelta(days=6)
    
    cw_data = data[(data['datetime'] >= start_cur_week) & (data['datetime'] <= end_cur_week)]
    # print(cw_data)
    cw_data['weekday'] = cw_data['datetime'].dt.weekday
    cw_data['hour'] = cw_data['datetime'].dt.hour
    # print(cw_data)
    return cw_data

retrieve_data_week("65b30e99201ae95a40c5bb80")