from django.urls import path
from .views import PlantsView

urlpatterns =   [
    path('', PlantsView.as_view()),
    path('<int:id>/', PlantsView.as_view()),
]