from rest_framework import serializers
from .models import User, ModelInfo

class PredictorSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=100)
    predictions = serializers.ListField(child=serializers.CharField(max_length=255))
    
class UserSerializer(serializers.ModelSerializer):
    model_count = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'userObjectId', 'model_count']
             
    def get_model_count(self, obj):
        return ModelInfo.objects.filter(user=obj).count()

class UserModelInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelInfo
        fields = ['id','modelName', 'modelingDate']
    
class ModelInfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelInfo
        fields = ['modelScore', 'trainingCount', 'scoringCount']