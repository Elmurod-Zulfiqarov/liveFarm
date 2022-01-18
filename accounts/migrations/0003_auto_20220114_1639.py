# Generated by Django 3.2.9 on 2022-01-14 11:39

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0002_auto_20211204_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('definition', models.TextField(blank=True, max_length=4096, null=True)),
                ('salary', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('passport', models.FileField(blank=True, null=True, upload_to='')),
                ('email_user', models.CharField(blank=True, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, max_length=13, null=True)),
                ('phone_farm', models.CharField(blank=True, max_length=13, null=True)),
                ('telegram', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.DeleteModel(
            name='Farm',
        ),
        migrations.DeleteModel(
            name='StaffUser',
        ),
    ]
