# Generated by Django 2.1.3 on 2018-11-25 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0009_remove_contact_info_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_info',
            old_name='agent',
            new_name='contactagent',
        ),
    ]
