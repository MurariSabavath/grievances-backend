# Generated by Django 4.0.5 on 2022-06-23 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_profile_is_admin_remove_profile_is_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffprofile',
            name='is_lab',
        ),
        migrations.RemoveField(
            model_name='staffprofile',
            name='is_lab_staff',
        ),
        migrations.RemoveField(
            model_name='staffprofile',
            name='is_theory',
        ),
        migrations.AddField(
            model_name='staffprofile',
            name='user_role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Theory'), (2, 'Lab Subject'), (3, 'Lab Staff')], default=1),
            preserve_default=False,
        ),
    ]
