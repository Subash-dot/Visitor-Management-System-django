# Generated by Django 4.2 on 2023-05-03 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0003_alter_visitor_check_in'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='excel')),
            ],
        ),
    ]