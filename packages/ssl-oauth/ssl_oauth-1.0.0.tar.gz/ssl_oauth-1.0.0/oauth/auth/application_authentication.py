from rest_framework import exceptions
from django.utils.translation import gettext_lazy as _
from oauth.utils.keycloak import get_keycloak
from oauth.models.user import User

class ApplicationAuthentication:

    def authenticate(self, request):
        keycloak_openid = get_keycloak()

        token = self.get_token(request)
        try:
            keycloak_user = keycloak_openid.userinfo(token)
            user = User(
                first_name=keycloak_user['given_name'], 
                second_name=keycloak_user['family_name'], 
                username=keycloak_user['preferred_username'],
                email=keycloak_user['email'],
                id=keycloak_user['sub'])
            return (user, None)
        except:
            msg = _('Неверный токен')
            raise exceptions.AuthenticationFailed(msg)
        
        
    
    def get_token(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION', b'').split(" ")

        if not len(auth) == 2:
            msg = _('Не предоставлены учетные данные')
            raise exceptions.AuthenticationFailed(msg)
        
        if auth[0] != self.authenticate_header(request):
            msg = _('Не предоставлены учетные данные')
            raise exceptions.AuthenticationFailed(msg)

        return auth[1]

    def authenticate_header(self, request):
        return "Bearer"