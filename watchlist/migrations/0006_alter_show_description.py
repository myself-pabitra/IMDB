# Generated by Django 4.2.4 on 2023-08-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0005_show_delete_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
