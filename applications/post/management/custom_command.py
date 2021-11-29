from django.core.management.base import BaseCommand
from datetime import datetime
class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        current_time = datetime.today().strftime(f'Date:%Y-%m-%d Time: %H:%M:%S')
        self.stdout.write(f'current {current_time}')