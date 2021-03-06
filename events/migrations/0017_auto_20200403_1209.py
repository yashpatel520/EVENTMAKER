# Generated by Django 3.0.4 on 2020-04-03 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_auto_20200403_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregistration',
            name='Catering',
            field=models.CharField(choices=[('not_enroll', 'Not Enroll'), ('need_to_work', 'NEED TO WORK'), ('in_process', ' IN PROCESS'), ('done', 'DONE')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='Decoration',
            field=models.CharField(choices=[('not_enroll', 'Not Enroll'), ('need_to_work', 'NEED TO WORK'), ('in_process', ' IN PROCESS'), ('done', 'DONE')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='Photographer',
            field=models.CharField(choices=[('not_enroll', 'Not Enroll'), ('need_to_work', 'NEED TO WORK'), ('in_process', ' IN PROCESS'), ('done', 'DONE')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='Projector',
            field=models.CharField(choices=[('not_enroll', 'Not Enroll'), ('need_to_work', 'NEED TO WORK'), ('in_process', ' IN PROCESS'), ('done', 'DONE')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='Sound_system',
            field=models.CharField(choices=[('not_enroll', 'Not Enroll'), ('need_to_work', 'NEED TO WORK'), ('in_process', ' IN PROCESS'), ('done', 'DONE')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='confirmation',
            field=models.CharField(choices=[('accepted', 'accepted'), ('pending', 'pending'), ('reject', 'reject'), ('completed', 'completed')], max_length=30, null=True),
        ),
    ]
