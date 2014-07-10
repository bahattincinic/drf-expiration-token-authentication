from datetime import datetime, timedelta
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from .settings import api_settings


class TokenAuthenticationView(ObtainAuthToken):
    """
    Simple token based authentication.
    """
    def post(self, request):
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            token, created = self.model.objects.get_or_create(
                user=serializer.object['user'])

            utc_now = datetime.now()
            key = token.key
            if token.created < (utc_now - timedelta(
                    days=api_settings.expiration_time)):
                key = token.generate_key()
            if not created:
                self.model.objects.filter(key=token.key)\
                                  .update(key=key, created=utc_now)
            expiration_date = utc_now + timedelta(
                days=api_settings.expiration_time)
            return Response({'token': key, 'expiration_date': expiration_date})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
