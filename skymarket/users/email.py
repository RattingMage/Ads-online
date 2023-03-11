from django.contrib.auth.tokens import default_token_generator
from templated_mail.mail import BaseEmailMessage

from djoser import utils
from djoser.conf import settings


# TODO Здесь необходимо переместиться в исходный код Djoser
# TODO и правильно переопределит адрес сервера (в нашем случае это localhost:3000)
class PasswordResetEmail(BaseEmailMessage):
    template_name = "email/password_reset.html"

    def get_context_data(self):
        # PasswordResetEmail can be deleted
        pass
