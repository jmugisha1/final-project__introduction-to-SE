from .models import userProduct
from rest_framework import serializers

class userProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = userProduct
        fields = (
            'id',
            'productName',
            'productPrice',
            'productDate',
            'productImage',
            'productAuthor',
        )
        extra_kwargs = {'productAuthor': {'read_only': True},}