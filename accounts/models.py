from django.db import models

# Create your models here.
from django.contrib.auth.models import  AbstractUser
from django.db import models


class User(AbstractUser):

    email = models.EmailField(unique=True)
    ROLE_CHOICES = (
        ('USER', 'User'),
        ('ADMIN', 'Admin'),
    )
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='USER')
    
    def save(self, *args, **kwargs):
        if self.role == 'ADMIN':
            self.is_superuser = True
        else:
            self.is_superuser = False
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
