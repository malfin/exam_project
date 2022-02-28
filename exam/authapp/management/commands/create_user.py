import random

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

    def handle(self, *args, **options):
        print('Введите 1/2 (1 - создать 10 пользователей, 2 - создать 1 суперпользователя)')
        number = input()
        if number == '1':
            i = 0
            while i <= 9:
                KpkUser.objects.create_user(
                    login=f'user{i + 1}',
                    password='pass',
                    surname=random.choice(surname),
                    name=random.choice(name),
                    email=f'user{i + 1}@mail.ru'
                )
                print(f'Пользователь (login: user{i + 1}; password: pass) успешно создан!')
                i += 1
            print('Пользователи успешно созданы!')
        elif number == '2':
            KpkUser.objects.create_superuser(login='kpk', password='pass', email='kpk@mail.ru')
            print('Супер-пользователь успешно создан: login: kpk; password: pass')
        else:
            print('Вы ничего не выбрали!')
