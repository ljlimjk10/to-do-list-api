from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from . import UserManager

# Need a UserManager so Django knows how to create users
class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=300, unique=True)
    email = models.CharField(max_length=300, unique=True)
    is_verified = models.BooleanField(default=False)
    is_activated = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # Overwrite the default usernmae field - username to -email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_username(self):
        return self.name

    def __str__(self):
        return self.email