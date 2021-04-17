from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.contrib.auth.password_validation import validate_password

from core.models import make_upload_path, CreatedUpdatedModel


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a users with the given email and password.
        """
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(email=email, last_login=now, **extra_fields)
        validate_password(password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser should have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser should have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, default="", blank=True, db_index=True)
    last_name = models.CharField(max_length=50, default="", blank=True, db_index=True)
    avatar = models.ImageField(upload_to=make_upload_path, blank=True, default='')

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    last_request = models.DateTimeField(
        null=True, blank=True, help_text='When user make last request'
    )

    USERNAME_FIELD = 'email'

    objects = UserManager()


class UserLastActivity(CreatedUpdatedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    url = models.TextField(default="", blank=True)
