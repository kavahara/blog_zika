# Generated by Django 3.2.9 on 2021-11-29 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]