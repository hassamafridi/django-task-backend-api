# from django.db import models
# from .models import *
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _
# # Create your models here.


# class User(AbstractUser):
#     username = models.CharField(_('username'), max_length=255, blank=True, unique=False)
#     email = models.EmailField(_('email address'), unique=True)
#     USERNAME_FIELD = 'email'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     def get_username(self):
#         return self.email
