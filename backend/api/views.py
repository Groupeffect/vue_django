from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import (
    views,
    response,
    reverse,
    status
)
from . import serializer

class JwtTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializer.JwtTokenObtainPairSerializer
 
class ApiView(views.APIView):

    def get(self, request, format=None):
        users = f'{reverse.reverse("api",request=request).split("api")[0]}api/auth/users/'

        urls = [
            'jwt-create',
            'jwt-refresh',
            'jwt-verify',
            'api'
        ]
        endpoints={
            'register':'None',
            'users': {
                'me':f'{users}me/',
                'confirm':f'{users}confirm/',
                'resend_activation':f'{users}resend_activation/',
                'set_password':f'{users}set_password/',
                'reset_password':f'{users}reset_password/',
                'reset_password_confirm':f'{users}reset_password_confirm/',
                'set_username':f'{users}set_username/',
                'reset_username':f'{users}reset_username/',
                'reset_username_confirm':f'{users}reset_username_confirm/',
            }
        }

        for i in urls:
            endpoints[i] = reverse.reverse(i,request=request)

        return response.Response(
            endpoints,
            status=status.HTTP_200_OK
        )