# Generated by Django 5.0 on 2023-12-28 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='email',
            field=models.EmailField(max_length=70, unique=True),
        ),
    ]