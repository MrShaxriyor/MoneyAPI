from django.urls import path
from .views import TransactionListCreateAPIView, TransactionDetailAPIView, CategoryListCreateAPIView, CategoryDetailAPIView, BalanceAPIView

urlpatterns = [
    path("transactions/", TransactionListCreateAPIView.as_view(), name="transaction-list-create"),
    path("transactions/<int:pk>/", TransactionDetailAPIView.as_view(), name="transaction-detail"),
    path("categories/", CategoryListCreateAPIView.as_view(), name="category-list-create"),
    path("categories/<int:pk>/", CategoryDetailAPIView.as_view(), name="category-detail"),
    path("balance/", BalanceAPIView.as_view(), name="balance"),
]
