# Generated by Django 2.2.5 on 2019-09-23 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0002_auto_20190923_1506'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Links',
            new_name='Link',
        ),
    ]