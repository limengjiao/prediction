import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from joblib import load
import datetime
from django.utils import timezone

class Predictor():
    @staticmethod
    def predict_top5_foods(user_id):
        cur_datetime = timezone.now()
        weekday = cur_datetime.weekday()
        hour = cur_datetime.hour
        
        filename = user_id + '_intake_predictor.pkl' 
        label_encoder_filename = user_id + '_label_encoder.joblib'
        
        model = load(filename)
        label_encoder = load(label_encoder_filename)
        
        X_pred = pd.DataFrame([[weekday, hour]], columns=['weekday', 'hour'])
        proba = model.predict_proba(X_pred)
        top5_idx = np.argsort(proba, axis=1)[0][-5:]
        top5_foods = label_encoder.inverse_transform(top5_idx)
        return top5_foods[::-1]
