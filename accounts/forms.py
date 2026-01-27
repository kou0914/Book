from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class SignupForm(UserChangeForm):
    class Meta:
        fields = ("username",)