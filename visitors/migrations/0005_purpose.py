# Generated by Django 4.2 on 2023-05-14 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0004_excelfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]
