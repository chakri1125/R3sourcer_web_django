from django.urls import path
from .views import ResetPasswordRequestToken
from django_rest_passwordreset.views import ResetPasswordConfirm, ResetPasswordValidateToken
app_name = 'password_reset'

urlpatterns = [
    path("", ResetPasswordRequestToken.as_view(), name='reset-password-request'),
    path("confirm/", ResetPasswordConfirm.as_view(), name='reset-password-confirm'),
    path("validate_token/", ResetPasswordValidateToken.as_view(), name='reset-password-validate')
]