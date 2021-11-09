from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from libgravatar import Gravatar

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

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def gravatar(self, size=120):
        """Return a URL to the user's gravatar."""
        gravatar_object = Gravatar(self.email)
        gravatar_url = gravatar_object.get_image(size=size, default='mp')
        return gravatar_url

    def mini_gravatar(self):
        """Return a URL to a miniature version of the user's gravatar."""
        return self.gravatar(size=60)


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
