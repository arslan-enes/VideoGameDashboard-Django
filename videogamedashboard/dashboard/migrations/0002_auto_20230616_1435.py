# Generated by Django 3.2.7 on 2023-06-16 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogame',
            name='metascore',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='videogame',
            name='metascore_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='videogame',
            name='user_rating_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='videogame',
            name='user_score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
