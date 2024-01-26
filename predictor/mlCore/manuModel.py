import DataLoader
import Model
from joblib import dump

def run_model():
    user_id = "65b30e99201ae95a40c5bb80"
    
    data = DataLoader.retrieve_data(user_id)
    # print("After calling retrieve_data")

    is_success = Model.model_train(user_id, data)
    if is_success:
        print("Model training successful.")
    else:
        print("Model training failed.")
    
run_model()  
    