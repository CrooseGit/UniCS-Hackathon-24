# Generated by Django 5.0.4 on 2024-04-13 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simplearticle',
            name='target_age',
        ),
        migrations.AddField(
            model_name='simplearticle',
            name='simple_type',
            field=models.TextField(default='primary'),
            preserve_default=False,
        ),
    ]