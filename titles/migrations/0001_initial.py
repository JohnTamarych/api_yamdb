# Generated by Django 3.0.5 on 2020-10-31 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название категории')),
                ('slug', models.SlugField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название жанра')),
                ('slug', models.SlugField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название тайтла')),
                ('year', models.PositiveSmallIntegerField(verbose_name='год выпуска')),
                ('description', models.TextField(max_length=400, verbose_name='описание')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='titles.Category', verbose_name='категория')),
                ('genre', models.ManyToManyField(blank=True, related_name='titles', to='titles.Genre', verbose_name='жанр')),
            ],
            options={
                'ordering': ['-year'],
            },
        ),
    ]