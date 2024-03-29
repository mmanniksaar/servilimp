# Generated by Django 3.2.23 on 2024-01-29 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_txt', models.CharField(max_length=200)),
                ('second_txt', models.CharField(max_length=200)),
                ('third_txt', models.CharField(max_length=200)),
                ('fourth_txt', models.CharField(max_length=200)),
                ('fifth_txt', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddConstraint(
            model_name='about',
            constraint=models.UniqueConstraint(fields=('first_txt', 'second_txt', 'third_txt', 'fourth_txt', 'fifth_txt'), name='unique_fields'),
        ),
    ]
