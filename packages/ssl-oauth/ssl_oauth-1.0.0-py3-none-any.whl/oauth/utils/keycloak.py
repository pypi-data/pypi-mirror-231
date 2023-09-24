from keycloak import KeycloakOpenID, KeycloakOpenIDConnection, KeycloakAdmin
from django.conf import settings

def get_keycloak():
    return KeycloakOpenID(server_url=settings.KEYCLOAK_URL,
                                 client_id=settings.KEYCLOAK_CLIENT_ID,
                                 realm_name=settings.KEYCLOAK_REALM_NAME,
                                 client_secret_key=settings.KEYCLOAK_CLIENT_SECRET)
    
def get_keycloak_admin():
    keycloak_connection = KeycloakOpenIDConnection(
                        server_url=settings.KEYCLOAK_URL,
                        realm_name=settings.KEYCLOAK_REALM_NAME,
                        client_id=settings.KEYCLOAK_CLIENT_ID,
                        client_secret_key=settings.KEYCLOAK_CLIENT_SECRET,
                        verify=True)
    return KeycloakAdmin(connection=keycloak_connection)