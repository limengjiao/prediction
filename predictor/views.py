from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PredictorSerializer
from .mlCore.Predictor import Predictor 
import logging


class PredictorView(APIView):
    def get(self, request, userid):
        try:
            prediction_result = Predictor.predict_top5_foods(userid)
            prediction_result_str = [str(id) for id in prediction_result]
            print(prediction_result_str)
            serializer = PredictorSerializer(data={"user_id": userid, "predictions": prediction_result_str}) 
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
