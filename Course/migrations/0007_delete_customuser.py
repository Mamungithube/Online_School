# Generated by Django 5.0.6 on 2024-11-08 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0006_alter_course_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
