# Generated by Django 4.0.5 on 2022-07-12 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'verbose_name': 'movie', 'verbose_name_plural': 'movies'},
        ),
    ]