from rest_framework_simplejwt import serializers
from rest_framework import reverse

class JwtTokenObtainPairSerializer (serializers.TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        return data

