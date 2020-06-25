from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from . models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number', 'is_active', 'is_staff', 'department')
        # fields = UserCreationForm.Meta.fields + ('age',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number', 'is_active', 'is_staff', 'department')
        # fields = UserChangeForm.Meta.fields
