import random

import django.db.utils
from django.core.management.base import BaseCommand

from authapp.models import KpkUser

surname = (
    'Попова', 'Васильев', 'Горбачева', 'Громова', 'Устинова', 'Рыбаков', 'Иванов', 'Кочетков', 'Романова', 'Кошелев'
)

name = (
    'Алексей', 'Валерия', 'Лука', 'Амина', 'Вероника', 'Даниил', 'Мария', 'Дамир', 'Вероника', 'Михаил'
)


class Command(BaseCommand):
    help = 'Create UserProfile'

    def add_arguments(self, parser):
        parser.add_argument('users', type=int, help='Количество создаваемых пользователей')

    def handle(self, *args, **kwargs):
        users = kwargs['users']

        for i in range(users):
            KpkUser.objects.create_user(
                login=f'user{i + 1}',
                password='pass',
                surname=random.choice(surname),
                name=random.choice(name),
                email=f'user{i + 1}@mail.ru'
            )
            self.stdout.write(self.style.SUCCESS(f'Пользователь (login: user{i + 1}; password: pass) успешно создан!'))
            self.stdout.write(self.style.NOTICE('Пользователи успешно созданы!'))
