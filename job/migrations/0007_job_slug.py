# Generated by Django 5.1.4 on 2025-01-09 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_alter_job_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
