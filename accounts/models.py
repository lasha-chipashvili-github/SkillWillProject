from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.core.validators import MinLengthValidator

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=320, unique=True)


    #pn = models.CharField(max_length=11, validators=[MinLengthValidator(11)])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
