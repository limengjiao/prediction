from django.core.management.base import BaseCommand
import DataLoader
import Model
from joblib import dump

class Command(BaseCommand):
    help = 'Retrain the model'  

    # Model auto traing task
    def handle(self, *args, **options):
        user_id = "65991057ada9394da4f73eb3"

        is_success = Model.model_train(user_id, data)
        if is_success:
            print("Model training successful.")
            self.stdout.write(self.style.SUCCESS("Model training successful."))
        else:
            print("Model training failed.")
            self.stdout.write(self.style.SUCCESS("Model training failed."))
        
        