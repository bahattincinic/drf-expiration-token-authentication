#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='django-rest-expired-token',
    version='0.1',
    packages=['rest_expired_token'],
    url='https://github.com/bahattincinic/django-rest-expired-token',
    license='BSD',
    description='Expiration Token Authentication For Django Rest Framework',
    author='Bahattin Cinic',
    author_email='bahattincinic@gmail.com',
    test_suite='rest_expired_token.runtests.runtests.main',
    install_requires=['djangorestframework', 'django-nose'],
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
