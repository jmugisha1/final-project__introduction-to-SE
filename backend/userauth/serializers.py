from rest_framework import serializers
from .models import customUser

class customUserSerializer(serializers.ModelSerializer):
    class Meta():
        model = customUser
        fields = (
            'id',
            'email',
            'fullNames',
            'password'  
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create (self, validated_data):
        user = customUser.objects.create_user(**validated_data)
        return user

