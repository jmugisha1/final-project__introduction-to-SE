# from django.shortcuts import render
from .serializers import userProductSerializer
from .models import userProduct
from rest_framework import generics 
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny


#creating new product
class userProductCreate(generics.CreateAPIView):
    serializer_class = userProductSerializer
    permission_classes = [IsAuthenticated]
    queryset = userProduct.objects.all()

    def get_queryset(self):
        user = self.request.user
        return userProduct.objects.filter(productAuthor=user)
    

    #checking if the note is valid
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(productAuthor=self.request.user)
        else:
            print(serializer.errors)

#deleting product 
class userProductDelete(generics.DestroyAPIView):
    serializer_class = userProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return userProduct.objects.filter(productAuthor=user)


#showing products to the user
class userProductList(generics.ListAPIView):
    serializer_class = userProductSerializer
    permission_classes = [AllowAny]
    queryset = userProduct.objects.all()

# Showing a single product
class userProductDetail(generics.RetrieveAPIView):
    serializer_class = userProductSerializer
    permission_classes = [AllowAny]
    queryset = userProduct.objects.all()

