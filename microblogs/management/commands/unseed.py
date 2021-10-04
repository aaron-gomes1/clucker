from django.core.management.base import BaseCommand, CommandError
from microblogs.models import User

class Command(BaseCommand):
    def __init__(self):
        super().__init__()

    def handle(self, *args, **options):
        for user in User.objects.all():
            if type(user).__name__ == "User":
                user.delete()
