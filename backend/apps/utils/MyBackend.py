from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

UserModel = get_user_model()


class AuthBackend(ModelBackend):
    """
    login auth
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(code=username) | Q(email=username))
            return user
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        except Exception as e:
            return None
