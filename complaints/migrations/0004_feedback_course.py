# Generated by Django 4.0.5 on 2022-06-23 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0003_complaint_created_feedback_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='course',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
    ]