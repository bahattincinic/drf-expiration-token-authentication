# -*- coding: utf-8 -*-
import datetime
from django.test import TestCase
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework.compat import patterns
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from .authentication import ExpiringTokenAuthentication
from .views import TokenAuthenticationView


class TestView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (ExpiringTokenAuthentication,)

    def post(self, request):
        return HttpResponse({'a': 1, 'b': 2, 'c': 3})


urlpatterns = patterns(
    '',
    (r'^auth-token/$', TokenAuthenticationView.as_view()),
    (r'^token/$', TestView.as_view()),
)


class ExpiringTokenAuthenticationTests(TestCase):
    """
    Token authentication Tests
    """
    urls = 'rest_expiration_token.tests'

    def setUp(self):
        self.csrf_client = APIClient(enforce_csrf_checks=True)
        self.username = 'bahattin'
        self.email = 'bahattin@test.com'
        self.password = 'password'
        self.user = User.objects.create_user(self.username, self.email,
                                             self.password)
        self.key = 'abcd1234'
        self.token = Token.objects.create(key=self.key, user=self.user)

    def test_token_expired(self):
        """ Ensure token login view using expired token """
        self.token.created = self.token.created - datetime.timedelta(days=40)
        self.token.save()
        response = self.csrf_client.post(
            '/token/', {'example': 'example'},
            HTTP_AUTHORIZATION='Token %s' % self.token.key, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_token_not_expired(self):
        """ Ensure token login view using not expired token """
        response = self.csrf_client.post(
            '/token/', {'example': 'example'},
            HTTP_AUTHORIZATION='Token %s' % self.token.key, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_token_expire_after_renewal(self):
        """ Ensure token renewes on next login after expiration """
        self.token.created = self.token.created - datetime.timedelta(days=40)
        self.token.save()
        response = self.csrf_client.post(
            '/auth-token/', {'username': self.username,
                             'password': self.password}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(response.data['token'], self.key)
