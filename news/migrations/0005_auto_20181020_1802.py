# Generated by Django 2.1.2 on 2018-10-20 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20181020_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='uuid',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]
