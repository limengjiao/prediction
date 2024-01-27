from django.core.management.base import BaseCommand
import DataLoader
import Model
import Accuracy
import RetrieveUser

class Command(BaseCommand):
    help = 'Retrain the model for all users'  

    # Model auto traing task
    def handle(self, *args, **options):
        
        userid_list = RetrieveUser.get_user_list()
        user_ids = userid_list['_id'].tolist()
        # user_id = "65991057ada9394da4f73eb3"
    
        for user_id in user_ids:
        # Logging last model score
            is_success_score = Accuracy.logging_model_score(user_id)
            if is_success_score:
                print("Model scoring successful.")
            else:
                print("Model scoring failed.")
                
            # Retraining model
            data = DataLoader.retrieve_data(user_id)
            if(data):
                is_success = Model.model_train(user_id, data)
                if is_success:
                    print("Model training successful.")
                    self.stdout.write(self.style.SUCCESS("Model training successful."))
                else:
                    print("Model training failed.")
                    self.stdout.write(self.style.ERROR("Model training failed."))
            else: 
                print("User doesn't have intake data to train the model.")
                self.stdout.write(self.style.SUCCESS("Model training unexecuted."))
            