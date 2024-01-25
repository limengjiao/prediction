import DataLoader
import Model
from joblib import dump

def run_model():
    user_id = "65991057ada9394da4f73eb3"
    filename = user_id + '_intake_predictor.pkl'
    label_encoder_filename = user_id + '_label_encoder.joblib'
    
    data = DataLoader.retrieve_data(user_id)
    print("After calling retrieve_data")
    data = DataLoader.retrieve_data(user_id)
    model, label_encoder = Model.model_train(data)
    dump(model, filename)
    dump(label_encoder, label_encoder_filename)
    print("Model Training Finished")
    
run_model()  
    