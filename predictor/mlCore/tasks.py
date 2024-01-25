from django.core.management.base import BaseCommand
import DataLoader
import Model
from joblib import dump

class Command(BaseCommand):
    help = 'Retrain the model'  

    # Model auto traing task
    def handle(self, *args, **options):
        user_id = "65991057ada9394da4f73eb3"
        filename = user_id + '_intake_predictor.pkl' 
        label_encoder_filename = user_id + '_label_encoder.joblib'
        
        data = DataLoader.retrieve_data(user_id)
        model, label_encoder = Model.model_train(data)
        dump(model, filename)
        dump(label_encoder, label_encoder_filename)
        self.stdout.write(self.style.SUCCESS('Model retrained successfully.'))