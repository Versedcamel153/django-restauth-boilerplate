from allauth.core.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

User = get_user_model()

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        email = sociallogin.account.extra_data.get("email")
        if not email:
            return  # Continue the normal flow if no email

        try:
            existing_user = User.objects.get(email=email)

            if sociallogin.is_existing:
                return  # Allow normal login

            # Link the social account to the existing user
            sociallogin.connect(request, existing_user)

            # Generate JWT tokens
            refresh = RefreshToken.for_user(existing_user)
            access_token = str(refresh.access_token)

            # Return tokens instead of redirecting
            raise ImmediateHttpResponse(
                Response(
                    {
                        "refresh": str(refresh),
                        "access": access_token,
                        "user": {
                            "id": existing_user.id,
                            "email": existing_user.email,
                        },
                    },
                    status=200,
                )
            )

        except User.DoesNotExist:
            pass  # Continue the normal signup process