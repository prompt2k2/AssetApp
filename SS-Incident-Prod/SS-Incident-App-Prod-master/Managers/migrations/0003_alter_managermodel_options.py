# Generated by Django 3.2.3 on 2021-08-17 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Managers', '0002_auto_20210812_1357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='managermodel',
            options={'ordering': ['name']},
        ),
    ]