from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'email', 'password1', 'password2'
        ]

class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'country']