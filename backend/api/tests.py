from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
User = get_user_model()

USER = {
    'username':'amir',
    'password':'testetst2738920',
    'email':'aaa@b.de',
}

ADMIN = {
    'username':'admin',
    'password':'testetst2738920',
    'email':'admin@b.de',
}

def create_jwt_token(self,user=USER):
    create_url = reverse('jwt-create')
    create_response = self.client.post(create_url,user)
    return create_response.data['access']

class UserSetUp(APITestCase):

    def setUp(self):
        user = User.objects.create_user(
            **USER
        )
        client = APIClient()
        client.login(
            **USER
        )

class AdminSetUp(APITestCase):

    def setUp(self):
        user = User.objects.create_superuser(
            **ADMIN
        )
        client = APIClient()
        client.login(
            **ADMIN
        )

class JWTBasicTests(UserSetUp):

    def test_get_urls(self):
        response = self.client.get(reverse('api'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_jwt(self):
        create_url = reverse('jwt-create')
        refresh_url = reverse('jwt-refresh')
        verify_url = reverse('jwt-verify')

        create_response = self.client.post(create_url,USER)
        self.assertEqual(create_response.status_code, status.HTTP_200_OK)

        refresh_response = self.client.post(refresh_url, create_response.data)
        self.assertEqual(refresh_response.status_code, status.HTTP_200_OK)
        
        verify_response = self.client.post(
            verify_url,
            {'token':create_response.data['access']}
        )
        self.assertEqual(verify_response.status_code, status.HTTP_200_OK)

class DjoserTests(UserSetUp):

    def test_add_user(self):
        me_url = f'{reverse("api")}auth/users/'
        me_response = self.client.post(
            me_url,
            {
                **USER,
                'username':'bubu',
                'email':'aaa@bbb.de'
            }
        )
        self.assertEqual(me_response.status_code, status.HTTP_201_CREATED)
        

    def test_list_users(self):
        me_url = f'{reverse("api")}auth/users/'
        me_response = self.client.get( me_url )
        self.assertEqual(me_response.status_code, status.HTTP_401_UNAUTHORIZED)
        

class DjoserAdminTests(AdminSetUp):

    def test_list_users(self):
        # TODO
        me_url = f'{reverse("api")}auth/users/ "Authorization:JWT {create_jwt_token(self,ADMIN)}" '
        me_response = self.client.get( me_url )
        print(
            '###########',
            me_response.data
        )
        self.assertEqual(me_response.status_code, status.HTTP_200_OK)
        