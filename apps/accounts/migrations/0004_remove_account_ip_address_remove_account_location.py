# Generated by Django 4.2.7 on 2025-03-03 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='ip_address',
        ),
        migrations.RemoveField(
            model_name='account',
            name='location',
        ),
    ]
