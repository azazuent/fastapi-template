from keycloak import KeycloakOpenID
from fastapi.security import OAuth2AuthorizationCodeBearer

import os

keycloak_url = os.getenv("KC_URL", "http://localhost:8080")
keycloak_client_id = os.getenv("KC_CLIENT_ID")
keycloak_client_secret_key = os.getenv("KC_CLIENT_KEY")
keycloak_realm_name = os.getenv("KC_REALM_NAME")


keycloak_openid = KeycloakOpenID(
    server_url=keycloak_url,
    client_id=keycloak_client_id,
    client_secret_key=keycloak_client_secret_key,
    realm_name=keycloak_realm_name
)

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"{keycloak_url}/realms/{keycloak_realm_name}/protocol/openid-connect/auth",
    tokenUrl=f"{keycloak_url}realms/{keycloak_realm_name}/protocol/openid-connect/token"
)
