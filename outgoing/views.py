from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from income.models import Transaction, Category

class StatisticsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        stats = (
            Transaction.objects
            .filter(user=user)
            .values("category__name", "type")
            .annotate(total=Sum("amount"))
            .order_by("category__name")
        )

        result = {}
        for item in stats:
            category = item["category__name"] or "No Category"
            tr_type = item["type"]
            total = item["total"]

            if category not in result:
                result[category] = {"income": 0, "expense": 0}

            result[category][tr_type] = total

        return Response(result)
