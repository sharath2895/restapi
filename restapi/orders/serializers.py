from .models import Orders
from rest_framework import serializers


class OrderCreationSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    status = serializers.HiddenField(default='PENDING')
    quantity = serializers.IntegerField()
    # created_at = serializers.DateTimeField(auto_now_add=True)
    # updated_at = serializers.DateTimeField(auto_now=True)

    class Meta:
        model = Orders
        fields =['size','status','quantity']
