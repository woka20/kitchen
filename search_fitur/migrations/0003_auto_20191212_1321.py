# Generated by Django 2.2.8 on 2019-12-12 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_fitur', '0002_auto_20191212_1210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='nama_lengkap',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]