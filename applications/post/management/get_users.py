from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Displays all users'

    def get_user(self, *args, **kwargs):
        users = get_user_model().objects.all()
        for user in users:
            self.stdout.write(f'Username {user.email}')