from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from accounts.managers import UserManager




class User(AbstractBaseUser, PermissionsMixin):

    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=14)
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["full_name", "phone"]

    def __str__(self):
        return self.email



class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    image = models.ImageField( upload_to='user_profile', blank=True, null=True)
    address = models.CharField( max_length=100)

    def __str__(self):
        return self.user.email
    