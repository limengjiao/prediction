from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PredictorSerializer, UserSerializer, UserModelInfoSerializer, ModelInfoDetailSerializer
from .mlCore.intake_predictor import IntakePredictor 
import logging
from .models import User, ModelInfo


class PredictorView(APIView):
    def get(self, request, userid):
        try:
            prediction_result = IntakePredictor.predict_top5_foods(userid)
            prediction_result_str = [str(id) for id in prediction_result]
            # print(prediction_result_str)
            serializer = PredictorSerializer(data={"user_id": userid, "predictions": prediction_result_str}) 
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AllUsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
class UserModelsView(APIView):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username) 
            user_models = ModelInfo.objects.filter(user=user) 
            serializer = UserModelInfoSerializer(user_models, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
        
class ModelDetailsView(APIView):
    def get(self, request, modelid):
        try:
            model_info = ModelInfo.objects.get(id=modelid)
            serializer = ModelInfoDetailSerializer(model_info)
            return Response(serializer.data)
        except ModelInfo.DoesNotExist:
            return Response({"error": "Model not found"}, status=404)