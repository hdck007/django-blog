# Generated by Django 3.0.8 on 2020-07-23 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default='write your description here', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]