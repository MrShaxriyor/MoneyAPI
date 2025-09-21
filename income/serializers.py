from .models import Transaction, Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class TransactionSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        source="category",
        queryset=Category.objects.none(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Transaction
        fields = ["id", "type", "amount", "description", "category", "category_id", "created_at"]
        read_only_fields = ["id", "created_at"]

    def __init__(self, *args, **kwargs):
        context = kwargs.get("context", {})
        request = context.get("request")
        user = getattr(request, "user", None)

        super().__init__(*args, **kwargs)

        if user and user.is_authenticated:
            self.fields["category_id"].queryset = Category.objects.filter(user=user)

