from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import secrets

# Create your models here.

class Department(models.Model):
    depart_name = models.CharField(max_length=100, verbose_name="Название")
    depart_code = models.CharField(max_length=100, verbose_name="Код отдела")

    def __str__(self):
        return self.depart_name

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, first_name, last_name, password=None):
        user = self.model(
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, phone_number, first_name, last_name, password=None):
        user = self.create_user(
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

        # secrets_generate = secrets.SystemRandom()
        # otp = secrets_generate.randrange(1000, 9999)
        # print(f"OTP-password: {str(otp)}")


class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60)
    username = models.CharField(max_length=30)
    data_joined = models.DateTimeField(verbose_name="data joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last_login", auto_now_add=True)
    phone_number = models.CharField(max_length=12, verbose_name="Номер", null=True, blank=True, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Отдел", null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, verbose_name="Статус активности")
    is_staff = models.BooleanField(default=False, verbose_name="Является сотрудником")
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, verbose_name="Имя", unique=True)
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")

    USERNAME_FIELD = 'first_name'
    REQUIRED_FIELDS = ['last_name', 'phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"