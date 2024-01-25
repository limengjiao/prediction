from django.urls import path
from .views import PredictorView

urlpatterns = [
    #  path('users/test', PredictorView.as_view(), name='intake_prediction'),
    path('users/<str:username>/intake-model-prediction/', PredictorView.as_view(), name='intake_prediction'),
]