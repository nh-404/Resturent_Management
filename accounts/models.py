from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from accounts.managers import UserManager




class User(AbstractBaseUser, PermissionsMixin):

    full_name = models.CharField(max_length=150, null=False)
    phone = phone = models.CharField(max_length=14)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["full_name", "phone"]

    def __str__(self):
        return self.email
    
