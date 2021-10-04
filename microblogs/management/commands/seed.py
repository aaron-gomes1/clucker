from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from microblogs.models import User

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        for i in range(0, 100):
            user = User.objects.create_user(
                username = '@' + self.faker.unique.user_name(),
                first_name=self.faker.first_name(),
                last_name=self.faker.last_name(),
                email=self.faker.email(),
                password='Password123',
                bio='The quick brown fox jumped over the lazy dog'
            )
            user.save()
