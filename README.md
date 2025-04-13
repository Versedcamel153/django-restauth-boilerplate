# Django REST Auth Boilerplate
This is a reusable Django app for REST API endpoints for user authentication and account management. It uses `dj-rest-auth` and `django-allauth` under the hood, with built in support for Google Login. 

What makes it different? This boilerplate comes pre-configured and simplified:
- It uses **email & password** for login instead of the default **username & password**
- Local account created with email & password are **automatically linked** when logged in with a google account with the same email
- Optional **JWT authentication** is the used instead of the default **token authentication**
    You can switch back to token authentication by setting [`USE_JWT`](#setup) to `False`

## Features

- User Registration
- Email/password login
- Google social login
- Logout
- Password reset and password change
- Built on top of `dj-rest-auth` and `django-allauth`

## Installation
```bash
pip install [git](https://github.com/Versedcamel153/django-restauth-boilerplate)
```

## Setup
In your Django settings.py:
```Python
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]

INSTALLED_APPS = [
        ...
        'django.contrib.sites',
        'rest_framework',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.google',
        'dj_rest_auth',
        'dj_rest_auth.registration',
        'backendAuth', #this app
]

MIDDLEWARE = [
    ...
    'allauth.account.middleware.AccountMiddleware',
]

AUTH_USER_MODEL = 'backendAuth.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    )
}

REST_AUTH = {
    ## Optional: JWT Authentication
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'access_token',
    'JWT_AUTH_REFRESH_COOKIE': 'refresh_token',
    'USER_DETAILS_SERIALIZER': 'dj_rest_auth.serializers.UserDetailsSerializer',
    'REGISTER_SERIALIZER': 'backendAuth.serializers.CustomRegisterSerializer',
}

SITE_ID = 1
# Email and Account Settings
SOCIALACCOUNT_AUTO_SIGNUP= True
SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT=True
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username', 'password1*', 'password2*']
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_LOGIN_METHODS = {"email"}  # Use email for authentication

```
And in your ``urls.py`` :
```Python
from django.urls import path, include

urlpatterns = [
    ...
    path('api/v1/auth/', include('backendAuth.urls')),
]
```

## Google Login Setup
To enable Google Login, add this to `settings.py`:
```Python
CALLBACK_URL = 'http://127.0.0.1:8000/api/v1/auth/google/' #Should match the 'Authorized redirect URIs' set on your Google Cloud Console
```
Then go to the Django admin panel and:
1. Navigate to **Social Applications** (provided by `django-allauth`)
2. Add a new application with:
    - **Provider**: Google
    - **Client ID** and **Secret** from your Google Developer Console
    - **Sites**: Select your site (eg., `example.com` or `localhost`)

    This would enable Google OAuth2 login for your API.