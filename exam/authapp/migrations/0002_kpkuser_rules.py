# Generated by Django 3.2 on 2022-03-04 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kpkuser',
            name='rules',
            field=models.BooleanField(default=True, verbose_name='rules'),
        ),
    ]
