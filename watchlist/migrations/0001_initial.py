# Generated by Django 4.2.4 on 2023-08-16 14:05

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
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
