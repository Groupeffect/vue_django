from django.contrib import admin
from django.conf.urls import url, include, path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    url(r"^jwt/create/?", views.JwtTokenObtainPairView.as_view(), name="jwt-create"),
    url(r"^jwt/refresh/?", jwt_views.TokenRefreshView.as_view(), name="jwt-refresh"),
    url(r"^jwt/verify/?", jwt_views.TokenVerifyView.as_view(), name="jwt-verify"),
    
    path('admin/', admin.site.urls),
    url(r'user/', include('userapp.urls')),
]


