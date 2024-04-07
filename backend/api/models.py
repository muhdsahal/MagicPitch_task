from django.contrib.auth.models import AbstractUser, Group, Permission
import random
import string
from django.db import models

# Generate a 10-character random string
def generate_referral_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

class User(AbstractUser):
    username = models.CharField(max_length=100,null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    referral_code = models.CharField(max_length=10, unique=True,
                    blank=True, null=True, default=generate_referral_code)
    registred_at=models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']