# Generated by Django 4.1.7 on 2023-03-27 13:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=256)),
                ('birth_year', models.IntegerField(db_column='birth_year')),
            ],
            options={
                'db_table': 'actors',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=256)),
                ('description', models.TextField(db_column='description')),
                ('duration_in_min', models.FloatField(db_column='duration')),
                ('release_year', models.IntegerField(db_column='year')),
                ('pic_url', models.URLField(db_column='pic_url', max_length=512, null=True)),
            ],
            options={
                'db_table': 'movies',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField(db_column='rating', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('rating_date', models.DateField(auto_now_add=True, db_column='rating_date')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_app.movie')),
            ],
            options={
                'db_table': 'ratings',
            },
        ),
        migrations.CreateModel(
            name='MovieActor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('main_role', models.BooleanField()),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_app.actor')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_app.movie')),
            ],
            options={
                'db_table': 'movie_actors',
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(through='imdb_app.MovieActor', to='imdb_app.actor'),
        ),
    ]
