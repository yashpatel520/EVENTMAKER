# Generated by Django 3.0.4 on 2020-04-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20200401_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistration',
            name='Catering',
            field=models.CharField(default=False, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='Decoration',
            field=models.CharField(default=False, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='Photographer',
            field=models.CharField(default=False, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='Projector',
            field=models.CharField(default=False, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='Sound_system',
            field=models.CharField(default=False, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='confirmation',
            field=models.CharField(default=False, max_length=30, null=True),
        ),
    ]
