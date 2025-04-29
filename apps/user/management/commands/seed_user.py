from django.core.management.base import BaseCommand
from apps.user.models.user import User

class Command(BaseCommand):
    help = "Seed default user data"

    def handle(self, *args, **kwargs):
        User.objects.get_or_create(username="admin")
        self.stdout.write(self.style.SUCCESS("Default user created"))
