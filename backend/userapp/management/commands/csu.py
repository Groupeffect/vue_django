from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from backend.settings import ADMIN
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = 'Set up model data'

    # def add_arguments(self, parser):
    #     parser.add_argument('user_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        User = get_user_model()
        try:
            User.objects.create_superuser(
                **ADMIN
            )
            self.stdout.write(self.style.SUCCESS(f'Super user {ADMIN} Successfully'))
        except:

            self.stdout.write(self.style.ERROR(f'Super user fail : {ADMIN}'))

        else:
            pass
        return