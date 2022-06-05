# Generated by Django 4.0.4 on 2022-06-05 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directors', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='reviews',
        ),
        migrations.AddField(
            model_name='movie',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='review',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='email',
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
        ),
        migrations.AddField(
            model_name='review',
            name='username',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='movie',
            name='film_director',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='directors.director'),
        ),
        migrations.AlterField(
            model_name='review',
            name='source',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
