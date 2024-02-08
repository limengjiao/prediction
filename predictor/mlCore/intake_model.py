from sklearn.preprocessing import LabelEncoder
from joblib import dump
import xgboost as xgb
import os
from . import db_operations

folder = './predictor/mlCore/mlModels/'
if not os.path.exists(folder):
    os.makedirs(folder)

def model_train(user_id, data):
    
    filename = user_id + '_intake_predictor.pkl' 
    label_encoder_filename = user_id + '_label_encoder.joblib'
    
    label_encoder = LabelEncoder()
    data_count = len(data)
    data['encode'] = label_encoder.fit_transform(data['food'])

    X_train = data[['weekday', 'hour']]
    y_train = data['encode']   
    # print(y_train.unique())

    model = xgb.XGBClassifier(objective='multi:softmax', num_class=len(data['encode'].unique()))
    try:
        model.fit(X_train, y_train)
        dump(model, os.path.join(folder, filename))
        dump(label_encoder, os.path.join(folder, label_encoder_filename))
        db_operations.add_model_record(filename, data_count)
        return True
    except Exception as e:
        print("An error occurred during model training:", e)
        return False 

        
        
        
