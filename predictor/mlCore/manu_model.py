import predictor.mlCore.data_loader as data_loader
import predictor.mlCore.intake_model as intake_model
import pandas as pd
from joblib import dump
import Accuracy

def run_model():
    user_id = "65b30e99201ae95a40c5bb80"
    
    is_success_score = Accuracy.logging_model_score(user_id)
    # print(is_success_score)
    if is_success_score:
        print("Model scoring successful.")
    else:
        print("Model scoring failed.")
        
    data = data_loader.retrieve_data(user_id)
    # print("After calling retrieve_data")

    is_success = intake_model.model_train(user_id, data)
    if is_success:
        print("Model training successful.")
    else:
        print("Model training failed.")
    
run_model()  
    