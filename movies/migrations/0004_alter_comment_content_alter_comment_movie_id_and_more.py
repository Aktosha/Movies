# Generated by Django 4.1.3 on 2022-12-02 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0003_movie_movie_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(default='1', max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='movie_id',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='movie_comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='movies.movie', verbose_name='фильм'),
        ),
    ]
