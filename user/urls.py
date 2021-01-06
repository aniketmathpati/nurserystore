from .views import LoginView, SignUpView
from django.urls import path

urlpatterns = [
    path('user-login/', LoginView.as_view()),
    path('user-signup/', SignUpView.as_view()),
]