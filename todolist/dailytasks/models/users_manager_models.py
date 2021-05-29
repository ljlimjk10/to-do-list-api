from django.db import models
from django.contrib.auth.models import BaseUserManager
class UserManager(BaseUserManager):

    def create_user(self,username,email,password=None):
        
        if not username:
            raise ValueError('User should have an username')
        if not email:
            raise ValueError('User should have an email')
        email = self.normalize_email(email)
        # model attribute from BaseUserManager
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,username,password):

        if password is None:
            raise TypeError('Password should not be none')
        
        user = self.create_user(username,email,password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


