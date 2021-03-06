from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import CustomUser, OtpAuthentificate


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


class OtpCreationForm(ModelForm): #ModelForm
    class Meta:
        model = OtpAuthentificate
        fields = ['otp_password']
