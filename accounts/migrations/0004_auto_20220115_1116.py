# Generated by Django 3.2.9 on 2022-01-15 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220114_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='email_user',
        ),
        migrations.RemoveField(
            model_name='accounts',
            name='full_name',
        ),
    ]
