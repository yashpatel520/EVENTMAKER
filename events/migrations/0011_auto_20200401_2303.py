# Generated by Django 3.0.4 on 2020-04-01 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20200401_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventregistration',
            old_name='user',
            new_name='user_id',
        ),
    ]
