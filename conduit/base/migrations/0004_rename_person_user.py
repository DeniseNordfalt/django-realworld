# Generated by Django 4.1.3 on 2022-11-20 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_person_age'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='User',
        ),
    ]
