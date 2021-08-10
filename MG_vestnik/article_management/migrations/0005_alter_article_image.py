# Generated by Django 3.2.3 on 2021-08-09 16:51

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_management', '0004_alter_article_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
