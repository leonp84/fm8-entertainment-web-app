# Generated by Django 5.0.4 on 2024-05-05 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_movie_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.CharField(max_length=10),
        ),
    ]