from rest_framework_simplejwt.views import TokenObtainPairView
from . import serializer

class JwtTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializer.JwtTokenObtainPairSerializer
 