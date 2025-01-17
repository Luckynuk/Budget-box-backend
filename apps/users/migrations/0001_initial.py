# Generated by Django 5.0.4 on 2024-07-09 02:11

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('password', models.CharField(max_length=255, verbose_name='Password')),
                ('budget', models.IntegerField(default=0, verbose_name='Budget')),
                ('token', models.CharField(blank=True, db_index=True, max_length=500, null=True, verbose_name='Token')),
                ('profile', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Profile Picture')),
                ('token_expires', models.DateTimeField(blank=True, null=True, verbose_name='Token Expiration Date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
