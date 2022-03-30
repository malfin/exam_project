import django.db.utils
from django.core.management.base import BaseCommand

from authapp.models import KpkUser


class Command(BaseCommand):
    help = 'Create SuperUser'

    def handle(self, *args, **kwargs):
        try:
            KpkUser.objects.create_superuser(login='kpk', password='pass', email='kpk@mail.ru')
            self.stdout.write(self.style.NOTICE('Суперпользователь успешно созданы!'))
        except django.db.utils.IntegrityError:
            self.stdout.write(self.style.ERROR('Суперпользователь уже создан (kpk:pass)'))
