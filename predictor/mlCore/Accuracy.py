from sklearn.metrics import accuracy_score
from . import DataLoader;
import pandas as pd
from joblib import load
import os
import logging


def logging_model_score(user_id):
    log_folder = './predictor/mlCore/log/'
    log_filename = 'model_accuracy.log'
    log_path = os.path.join(log_folder, log_filename)
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
        
    logging.basicConfig(filename=log_path, level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    
    folder = './predictor/mlCore/mlModels/'
    filename = os.path.join(folder, user_id + '_intake_predictor.pkl')
    label_encoder_filename = os.path.join(folder, user_id + '_label_encoder.joblib')
    
    data = DataLoader.retrieve_data_week(user_id)
    if data.empty:
        print(f"User does not have intake data this week.")
        return False   
    # print(data)
    
    try:
        model = load(filename)
        label_encoder = load(label_encoder_filename)
    except Exception as e:
        print(f"An error occurred while loading model or label encoder: {e}")
        return False
    
    X_test = data[['weekday', 'hour']]
    data['encode'] = label_encoder.fit_transform(data['food'])
    y_test = data['encode'] 
    
    try:
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)   
        logging.info(f"User ID: {user_id} - Model Accuracy: {accuracy}")
        print(f"Model Accuracy: {accuracy}")
        return True
    except Exception as e:
        print("An error occurred during model scoring", e)
        return False 
    
logging_model_score("65b30e99201ae95a40c5bb80")   