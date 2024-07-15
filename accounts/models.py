from django.db import models

# Create your models here.
from django.contrib.auth.models import  AbstractUser
from django.db import models


class User(AbstractUser):

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, default='USER')

    def __str__(self):
        return self.username
