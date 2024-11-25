from django.urls import path
from . import views

urlpatterns = [
    # creating products
    path('createproduct/', views.userProductCreate.as_view(), name='product-create'),

    # deleting products
    path('deleteproduct/<int:pk>/', views.userProductDelete.as_view(), name='product-delete'),
    
    # showing products
    path('productList/', views.userProductList.as_view(), name='product-list'),

    # showing a single product
    path('productList/<int:pk>/', views.userProductDetail.as_view(), name='product-list-detail'),

]
