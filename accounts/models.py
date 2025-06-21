from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    country = models.CharField(
        max_length=20,
        choices=(
            ('USA', 'USA'),
            ('UK', 'UK'),
            ('JP', 'JP'),
            ('MX', 'MX'),
            ('Ghana', 'Ghana'),
            ('Nigeria', 'Nigeria')
        ),
        null=True
    )
