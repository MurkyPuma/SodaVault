# Generated by Django 5.0 on 2024-02-10 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0008_alter_drink_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='drink_images/'),
        ),
    ]
