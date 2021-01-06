from .views import LoginView, SignUpView
from django.urls import path

urlpatterns = [
    path('nursery-login/', LoginView.as_view()),
    path('nursery-signup/', SignUpView.as_view()),
]