from django.dispatch import receiver
from django.urls import reverse
from r3sourcer.apps.email_interface import tasks
from r3sourcer.apps.email_interface.utils import get_email_service

from django_rest_passwordreset.signals import reset_password_token_created

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_service = get_email_service()
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(
            'https://piiprent.piipaitest.com/reset_password',
            reset_password_token.key)
    }

    print(context['reset_password_url'], flush=True)
    tasks.send_email_default.delay(context['email'], "Reset your password", context['reset_password_url'], None)
    # email_service.send(context['email'], "Reset your password", context['reset_password_url'], *args, **kwargs)

    