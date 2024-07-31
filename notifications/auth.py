from rest_framework import authentication
from rest_framework import exceptions
import requests


class CustomJwtAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            return None

        try:
            token = auth_header.split()[1]
            return self.validate_token(token)
        except IndexError:
            raise exceptions.AuthenticationFailed('Invalid token header')

    def validate_token(self, token):
        auth_service_url = 'http://authentication:8000/api/authenticate/'
        try:
            response = requests.post(auth_service_url, json={'token': token})
            if response.status_code == 200:
                user_data = response.json()
                user = type('User', (object,), user_data)
                return (user, token)
            else:
                raise exceptions.AuthenticationFailed('Invalid token')
        except requests.RequestException:
            raise exceptions.AuthenticationFailed('Token validation failed')
