# Generated by Django 5.0.6 on 2024-10-28 21:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0002_course_enrolled_users'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='enrolled_users',
        ),
        migrations.AddField(
            model_name='course',
            name='enrolled_users',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
