Django Rest Framework Expiration Token Authentication
====================
Expiration Token Authentication For Django Rest Framework

[![Build Status](https://travis-ci.org/bahattincinic/django-rest-expiration-token-authentication.svg?branch=master)](https://travis-ci.org/bahattincinic/django-rest-expiration-token-authentication)


Requirements
------

* Python (2.6, 2.7, 3.2, 3.3, 3.4)
* Django (1.4, 1.3, 1.5, 1.6,)

Installation
------

Install using `pip`...

    pip install -e git@github.com:bahattincinic/django-rest-expiration-token-authentication.git
    

Usage
------
Add `TOKEN_AUTHENTICATION` to your settings.

    TOKEN_AUTHENTICATION = {
        # default: False
        'is_expired': True,
        # in days
        'expiration_time': 30
    }
    
    INSTALLED_APPS = (
        ...
        'rest_framework',
        'rest_framework.authtoken',        
    )
    
Add `Authentication Backend` to your settings.
    
    REST_FRAMEWORK = {
        ...
        DEFAULT_AUTHENTICATION_CLASSES: (
            'rest_expiration_token.authentication.ExpiringTokenAuthentication'
            ...
        )
    }

`ExpiringTokenAuthentication` To manually add
    
    from rest_framework.views import APIView
    from rest_expiration_token.authentication import ExpiringTokenAuthentication
    
    class TestView(APIView):
        authentication_classes = (ExpiringTokenAuthentication,)
        ...

Add `Authentication View` to your urls
    
    from rest_expiration_token.views import TokenAuthenticationView
    urlpatterns = patterns('',
        ...
        url(r'^auth-token/$', TokenAuthenticationView.as_view()),
    )

Sample Response
------------------
    curl -X POST  -H "Content-Type: application/json" -d '{"username":"bahattincinic","password":"123456"}' http://localhost:8000/auth-token/
    
    {"expiration_date": "2014-07-25T20:57:01.413Z", "token": "acf45a335d83074a5d7e8d4a09a4d2ba5d52de41"}
