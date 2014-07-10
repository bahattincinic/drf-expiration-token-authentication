import datetime

from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
from .settings import api_settings


class ExpiringTokenAuthentication(TokenAuthentication):
    """
    Token Authentication Backend
    """

    def authenticate_credentials(self, key):
        try:
            token = self.model.objects.get(key=key)
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted')

        now = datetime.datetime.now()
        difference = datetime.timedelta(days=api_settings.expiration_time)
        if api_settings.is_expired and token.created < (now - difference):
            raise exceptions.AuthenticationFailed('Token has expired')

        return token.user, token
