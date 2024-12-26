"""
This file is used to define the views for the user app.
"""

from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializer import UserSerializer, AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status


class CreateUserView(generics.CreateAPIView):
    """
    Create a new user in the system
    """

    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """
    Create a new auth token for user
    """

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class LoginUserView(generics.CreateAPIView):
    """
    Login user view
    """

    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        """
        Handle creating user authentication tokens
        """

        serializer = self.serializer_class(
            data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]

        # Generate or retrieve the token for the user
        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {"token": token.key, "user_id": user.id, "email": user.email},
            status=status.HTTP_200_OK,
        )


class ManageUserView(generics.RetrieveUpdateAPIView):
    """
    Manage the authenticated user
    """

    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """
        Retrieve and return authenticated user
        """

        return self.request.user
