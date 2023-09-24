from rest_framework.views import APIView
from rest_framework.response import Response
from keycloak import KeycloakError
from oauth.utils.keycloak import get_keycloak
import json

class LoginView(APIView):
    authentication_classes = []
    
    def post(self, request):
        keycloak_openid = get_keycloak()
        
        if not "username" in request.data:
            return Response(status=400, data={"username": "Это поле обязательно"})
        
        if not "password" in request.data:
            return Response(status=400, data={"password": "Это поле обязательно"})
        
        try:
            token = keycloak_openid.token(request.data['username'], request.data['password'])
        except KeycloakError as e:
            return Response(json.loads(e.response_body.decode('utf8').replace("'", '"')))
        return Response(token)
    
    def put(self, request):
        keycloak_openid = get_keycloak()
        
        if not "refresh_token" in request.data:
            return Response(status=400, data={"refresh_token": "Это поле обязательно"})

        return Response(keycloak_openid.refresh_token(request.data['refresh_token']))
