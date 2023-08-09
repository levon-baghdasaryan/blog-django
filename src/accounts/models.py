from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


class UserManager(BaseUserManager):
    """
    Creates and saves a User with the given email, date of
    birth and password.
    """
    def create_user(self, email, first_name, last_name, password=None, **other_fields):
        if not email:
            raise ValueError('Users must have an email address')

        if not password:
            raise ValueError('Users must have a password')

        if not first_name:
            raise ValueError('Users must have a First Name')

        if not last_name:
            raise ValueError('Users must have a Last Name')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            **other_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    email_verified_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)  # can login
    is_staff = models.BooleanField(default=False)  # staff user non superuser
    is_superuser = models.BooleanField(default=False)  # superuser
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'  # instead of username
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = ['first_name', 'last_name']  # for this command 'python manage.py createsuperuser'

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
