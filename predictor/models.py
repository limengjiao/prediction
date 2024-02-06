from django.db import models

class User(models.Model):
    userObjectId = models.CharField(max_length=24, unique=True)
    username = models.CharField(max_length=100)
    
class ModelInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='models')
    modelName = models.CharField(max_length=100)
    modelingDate = models.DateField()
    modelScore = models.FloatField()
    trainingCount = models.IntegerField()
    scoringCount = models.IntegerField()

    