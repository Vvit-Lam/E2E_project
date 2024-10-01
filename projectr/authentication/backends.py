# authentication/backends.py
from django.contrib.auth.backends import ModelBackend
from .models import Userr

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Userr.objects.get(email=email)
        except Userr.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
