# Generated by Django 4.0.4 on 2022-07-28 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sap', '0004_movie_score'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'permissions': [('create_movie', 'Can create movie'), ('update_movie', 'Can update movie'), ('remove_movie', 'Can delete movie'), ('approve_movie', 'Can approve movie')]},
        ),
        migrations.AddField(
            model_name='review',
            name='disapproved',
            field=models.BooleanField(default=True),
        ),
    ]
