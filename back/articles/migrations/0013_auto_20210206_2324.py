# Generated by Django 3.1.3 on 2021-02-06 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_merge_20210206_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='emotion',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='recomment',
            name='emotion',
            field=models.CharField(max_length=10),
        ),
    ]
