# Generated by Django 2.1.2 on 2018-10-20 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20181020_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='uuid',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
