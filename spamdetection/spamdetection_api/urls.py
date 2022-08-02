from django.urls import path
from . import views
from spamdetection_api.views import PredictFileView, PredictView,TrainView,FileUploadView
urlpatterns = [
    path('train/', TrainView.as_view()),
    path('bulkpredict/', PredictFileView.as_view()),
    path('predict/', PredictView.as_view()),
    path('test/', FileUploadView.as_view())
    
 #   path('dashboard/', CartItemViews.as_view())
] 