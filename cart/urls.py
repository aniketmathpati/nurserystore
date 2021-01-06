from django.urls import path
from .views import CartView,CartUnitView

urlpatterns =   [
    path('<int:userId>/', CartView.as_view()),
    path('', CartView.as_view()),
    path('<int:userId>/plant/<int:plantId>/', CartUnitView.as_view()),
]