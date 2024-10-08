# Generated by Django 5.0.6 on 2024-08-14 16:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0002_alter_course_image'),
        ('Teacher', '0003_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='Course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Course.course'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='Course',
            field=models.ManyToManyField(to='Course.course'),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
