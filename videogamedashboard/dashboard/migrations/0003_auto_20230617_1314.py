# Generated by Django 3.2.7 on 2023-06-17 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20230616_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogame',
            name='critic_reviews',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='videogame',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]