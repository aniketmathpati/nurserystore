from .views import OrderByNurseryView, OrderByUserView
from django.urls import path

urlpatterns = [
    path('user/<int:userId>/', OrderByUserView.as_view()),
    path('user/', OrderByUserView.as_view()),
    path('nursery/<int:nurseryId>/', OrderByNurseryView.as_view()),
]