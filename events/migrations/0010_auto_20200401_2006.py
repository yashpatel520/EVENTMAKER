# Generated by Django 3.0.4 on 2020-04-01 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0009_auto_20200401_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistration',
            name='profile_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL),
        ),
    ]
