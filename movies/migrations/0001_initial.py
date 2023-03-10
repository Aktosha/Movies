# Generated by Django 4.1.3 on 2022-11-10 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('image', models.ImageField(upload_to='movies')),
                ('banner', models.ImageField(upload_to='movies_banner')),
                ('category', models.CharField(choices=[('action', 'ACTION'), ('drama', 'DRAMA'), ('comedy', 'COMEDY'), ('romance', 'ROMANCE')], max_length=10)),
                ('language', models.CharField(choices=[('english', 'ENGLISH'), ('russian', 'RUSSIAN')], max_length=10)),
                ('status', models.CharField(choices=[('RA', 'RECENTLY ADDED'), ('MW', 'MOST WATCHED'), ('TR', 'TOP RATED')], max_length=2)),
                ('cast', models.CharField(max_length=100)),
                ('year_of_production', models.DateField()),
                ('views_count', models.IntegerField(default=0)),
            ],
        ),
    ]
