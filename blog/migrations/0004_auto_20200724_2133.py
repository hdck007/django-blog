# Generated by Django 3.0.8 on 2020-07-24 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200724_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(default='write your description here', max_length=255),
        ),
    ]
