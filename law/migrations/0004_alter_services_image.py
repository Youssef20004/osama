# Generated by Django 5.1.5 on 2025-03-17 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law', '0003_services_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
