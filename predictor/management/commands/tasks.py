from django.core.management.base import BaseCommand
from predictor.mlCore import DataLoader, Accuracy, db_operations, intake_model

class Command(BaseCommand):
    help = 'Retrain the model for all users'  

    # Model auto traing task
    def handle(self, *args, **options):
        
        userid_list = db_operations.get_user_list()
        db_operations.update_user(userid_list)
        user_ids = userid_list['_id'].tolist()
    
        for user_id in user_ids:
        # Logging last model score and update db table
            is_success_score = Accuracy.logging_model_score(user_id)
            if is_success_score:
                print("Model scoring successful.")
            else:
                print("Model scoring failed.")
                
            # Retraining model and update db table
            data = DataLoader.retrieve_data(user_id)
            if not data.empty:
                is_success = intake_model.model_train(user_id, data)
                if is_success:
                    print("Model training successful.")
                    self.stdout.write(self.style.SUCCESS("Model training successful."))
                else:
                    print("Model training failed.")
                    self.stdout.write(self.style.ERROR("Model training failed."))
            else: 
                print("User doesn't have intake data to train the model.")
                self.stdout.write(self.style.SUCCESS("Model training unexecuted."))
            