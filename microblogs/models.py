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

class Post(models.Model):
    class Meta:
        ordering = ["-created_at"]
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    text = models.TextField(
        max_length = 280,
        unique = False,
        blank = True
    )
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
