# Generated by Django 5.0.2 on 2024-02-28 11:34

import bookstore.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='author_images/')),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cover_image', models.ImageField(upload_to='')),
                ('rating', models.FloatField(default=0)),
                ('genres', models.CharField(blank=True, max_length=200, null=True)),
                ('isbn', models.CharField(blank=True, max_length=13, null=True, validators=[bookstore.models.validate_isbn])),
                ('added_date', models.DateField(auto_now_add=True)),
                ('publisher', models.TextField(max_length=100)),
                ('published_date', models.DateField()),
                ('languages', models.CharField(blank=True, max_length=200, null=True)),
                ('plot', models.TextField(blank=True, null=True)),
                ('authors', models.ManyToManyField(to='bookstore.author')),
            ],
        ),
    ]