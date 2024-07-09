from django.contrib.auth.forms import UserCreationForm
from .models import User, Certif
from django.forms import ModelForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

class BookForms (ModelForm):
    class Meta:
        model = Certif
        fields = '__all__'
