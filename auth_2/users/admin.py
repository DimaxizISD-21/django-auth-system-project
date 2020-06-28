from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . forms import CustomUserCreationForm, CustomUserChangeForm
from . models import CustomUser, Department, OtpAuthentificate

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['first_name', 'last_name', 'phone_number', 'is_active', 'is_staff', 'department']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Department)
admin.site.register(OtpAuthentificate)