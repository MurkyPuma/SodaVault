# Generated by Django 5.0 on 2024-02-06 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drink',
            name='author',
        ),
    ]
