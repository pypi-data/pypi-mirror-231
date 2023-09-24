from rest_framework.views import APIView
from rest_framework.response import Response
from oauth.utils.keycloak import get_keycloak_admin

class UserView(APIView):
    
    def get(self, request):
        return Response(request.user.toJSON())
    

class CreateUserView(APIView):
    authentication_classes = []

    def post(self, request):
        keycloak_admin = get_keycloak_admin()
        try:
            keycloak_admin.create_user(request.data)
            return Response(status=201)
        except:
            return Response(status=400, data={"error": "Нельзя создать"})
