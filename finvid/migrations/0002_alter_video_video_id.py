# Generated by Django 4.1.5 on 2023-01-03 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finvid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
