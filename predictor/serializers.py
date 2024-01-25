from rest_framework import serializers

class PredictorSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=100)
    predictions = serializers.ListField(child=serializers.CharField(max_length=255))