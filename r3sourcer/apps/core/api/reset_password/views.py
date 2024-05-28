from django.conf import settings

from datetime import timedelta
from django.utils import timezone
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from r3sourcer.apps.core.models import User, Contact
from django_rest_passwordreset.signals import reset_password_token_created
from django_rest_passwordreset.models import ResetPasswordToken, clear_expired, get_password_reset_token_expiry_time
from django_rest_passwordreset.serializers import EmailSerializer

HTTP_USER_AGENT_HEADER = getattr(settings, 'DJANGO_REST_PASSWORDRESET_HTTP_USER_AGENT_HEADER', 'HTTP_USER_AGENT')
HTTP_IP_ADDRESS_HEADER = getattr(settings, 'DJANGO_REST_PASSWORDRESET_IP_ADDRESS_HEADER', 'REMOTE_ADDR')

class ResetPasswordRequestToken(GenericAPIView):
    throttle_classes = ()
    permission_classes = ()
    serializer_class = EmailSerializer
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        # before we continue, delete all existing expired tokens
        password_reset_token_validation_time = get_password_reset_token_expiry_time()

        # datetime.now minus expiry hours
        now_minus_expiry_time = timezone.now() - timedelta(hours=password_reset_token_validation_time)

        # delete all tokens where created_at < now - 24 hours
        clear_expired(now_minus_expiry_time)

        try:
            contact = Contact.objects.get(email__iexact=email)
            user = User.objects.get(contact=contact)
            if user:
                active_user_found = False

                # check if user is active
                # also check whether the password can be changed (is useable), as user is not allowed
                # to change his password (e.g., LDAP user)
                if user.eligible_for_reset():
                    active_user_found = True

                # No active user found, raise a validation error
                # but not if DJANGO_REST_PASSWORDRESET_NO_INFORMATION_LEAKAGE == True
                if not active_user_found and not getattr(settings, 'DJANGO_REST_PASSWORDRESET_NO_INFORMATION_LEAKAGE', False):
                    raise exceptions.ValidationError({
                        'email': [_(
                            "We couldn't find an account associated with that email. Please try a different e-mail address.")],
                    })

                # last but not least: change his password
                # and create a Reset Password Token and send a signal with the created token
                if user.eligible_for_reset():
                    # define the token as none for now
                    token = None

                    # check if the user already has a token
                    if user.password_reset_tokens.all().count() > 0:
                        # yes, already has a token, re-use this token
                        token = user.password_reset_tokens.all()[0]
                    else:
                        # no token exists, generate a new token
                        token = ResetPasswordToken.objects.create(
                            user=user,
                            user_agent=request.META.get(HTTP_USER_AGENT_HEADER, ''),
                            ip_address=request.META.get(HTTP_IP_ADDRESS_HEADER, ''),
                        )
                    # send a signal that the password token was created
                    # let whoever receives this signal handle sending the email for the password reset
                    reset_password_token_created.send(sender=self.__class__, instance=self, reset_password_token=token)
        
        except (Contact.DoesNotExist, User.DoesNotExist):
            return self.http_response_no_content()

        # Continue with the rest of the process
        return Response({'status': 'OK'})