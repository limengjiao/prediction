from django.urls import path
from .views import PredictorView, AllUsersView, ModelDetailsView, UserModelsView

urlpatterns = [
    #  path('users/test', PredictorView.as_view(), name='intake_prediction'),
    path('users/<str:userid>/intake-model-prediction/', PredictorView.as_view(), name='intake_prediction'),
    path('users/', AllUsersView.as_view(), name='all-users'),
    path('users/<str:username>/models/', UserModelsView.as_view(), name='user-models'),
    path('models/<int:modelid>/details/', ModelDetailsView.as_view(), name='model-details'),
]