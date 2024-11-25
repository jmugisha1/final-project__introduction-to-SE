from django.contrib import admin
from django.urls import path, include
from userauth.views import RegisterUserView, userDetails
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import ( 
    TokenObtainPairView, TokenRefreshView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterUserView.as_view(), name="register_user"),
    path('api/login/', TokenObtainPairView.as_view(), name="get_token"),
    path('api/userdetails/', userDetails.as_view(), name="account_details"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="refresh_token"),
    path('api-auth/', include('rest_framework.urls')),  

    # urls for userproducts app
    path('api/', include('userproducts.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

