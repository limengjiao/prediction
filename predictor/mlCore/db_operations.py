import pandas as pd
import pymongo
from django.utils import timezone
from predictor.models import User
from predictor.models import ModelInfo

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
def add_model_record(model_name, tc):
    user_object_id = model_name[:24]
    try:
        user = User.objects.get(userObjectId=user_object_id)
    except User.DoesNotExist:
        print("User with the given userObjectId does not exist.")
        return
    model_info = ModelInfo(
        user=user,
        modelName = model_name,
        modelingDate=timezone.now(),
        modelScore = 0,
        trainingCount = tc,
        scoringCount = 0
    )
    model_info.save()

# Add model score to model table
def add_model_score(model_name, model_score, sc):
    try:
        model_info = ModelInfo.objects.filter(modelName=model_name).latest('modelingDate')
        model_info.modelScore = model_score
        model_info.scoringCount = sc
        model_info.save()
        print("Model score and scoring count updated successfully.")
    except ModelInfo.DoesNotExist:
        print("Model does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
    

user_ids_df = get_user_list()
update_user(user_ids_df)
