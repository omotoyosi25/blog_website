# Generated by Django 4.2.9 on 2024-01-24 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='example.jpg', upload_to='thumbnail'),
        ),
    ]
