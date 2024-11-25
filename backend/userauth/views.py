from .models import customUser
from .serializers import customUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


class RegisterUserView(generics.CreateAPIView):
    queryset = customUser.objects.all()
    serializer_class = customUserSerializer
    permission_classes = [AllowAny]


class userDetails(generics.RetrieveAPIView):
    queryset = customUser.objects.all()
    serializer_class = customUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user