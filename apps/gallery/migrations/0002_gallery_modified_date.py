# Generated by Django 3.2.23 on 2024-01-31 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]