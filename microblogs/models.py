from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(
        max_length = 30,
        unique = True,
        validators=[RegexValidator(
            regex=r'^@\w{3,}$',
            message='Username must consist of @ followed by at least three alphanumericals'
        )]
    )
    first_name = models.CharField(unique = False, blank = False, max_length = 50)
    bio = models.TextField(
        max_length = 520,
        unique = False,
        blank = True
    )
