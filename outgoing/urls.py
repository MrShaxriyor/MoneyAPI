from django.urls import path
from .views import StatisticsAPIView

urlpatterns = [
    path("stat/", StatisticsAPIView.as_view(), name="statistics"),
]
