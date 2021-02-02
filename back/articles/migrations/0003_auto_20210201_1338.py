# Generated by Django 3.1.3 on 2021-02-01 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210127_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashtag',
            name='article',
        ),
        migrations.AddField(
            model_name='hashtag',
            name='articles',
            field=models.ManyToManyField(related_name='hashtags', to='articles.Article'),
        ),
    ]