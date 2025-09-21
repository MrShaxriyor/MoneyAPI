from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Transaction, Category
from .serializers import TransactionSerializer, CategorySerializer
from rest_framework import status, permissions
from django.db.models import Sum

class TransactionListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = Transaction.objects.filter(user=request.user)
        serializer = TransactionSerializer(transactions, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Transaction.objects.get(pk=pk, user=user)
        except Transaction.DoesNotExist:
            return None

    def get(self, request, pk):
        transaction = self.get_object(pk, request.user)
        if not transaction:
            return Response({"error": "Topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, pk):
        transaction = self.get_object(pk, request.user)
        if not transaction:
            return Response({"error": "Topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TransactionSerializer(transaction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        transaction = self.get_object(pk, request.user)
        if not transaction:
            return Response({"error": "Topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        transaction.delete()
        return Response({"message": "O‘chirildi"}, status=status.HTTP_204_NO_CONTENT)
    



class CategoryListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        categories = Category.objects.filter(user=request.user)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Category.objects.get(pk=pk, user=user)
        except Category.DoesNotExist:
            return None

    def get(self, request, pk):
        category = self.get_object(pk, request.user)
        if not category:
            return Response({"error": "Kategoriya topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk, request.user)
        if not category:
            return Response({"error": "Kategoriya topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        category = self.get_object(pk, request.user)
        if not category:
            return Response({"error": "Kategoriya topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk, request.user)
        if not category:
            return Response({"error": "Kategoriya topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response({"message": "Kategoriya o‘chirildi"}, status=status.HTTP_204_NO_CONTENT)
    



class BalanceAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        transactions = Transaction.objects.filter(user=user)

        total_income = transactions.filter(type="income").aggregate(total=Sum("amount"))["total"] or 0
        total_expense = transactions.filter(type="expense").aggregate(total=Sum("amount"))["total"] or 0
        balance = total_income - total_expense

        return Response({
            "balance": balance,
            "total_income": total_income,
            "total_expense": total_expense
        })