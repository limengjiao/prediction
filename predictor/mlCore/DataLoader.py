import pandas as pd
import pymongo
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from bson import ObjectId

def retrieve_data(user_type_id):
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

    data['datetime'] = pd.to_datetime(data['date'])
    data['weekday'] = data['datetime'].dt.weekday
    data['hour'] = data['datetime'].dt.hour
    # print("Data: " + data.to_string())
    # print("Data types:\n", data.dtypes)
    return data

# retrieve_data("65991057ada9394da4f73eb3")
