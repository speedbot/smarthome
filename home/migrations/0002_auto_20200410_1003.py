# Generated by Django 2.2 on 2020-04-10 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulb',
            name='deleted_at',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='fan',
            name='deleted_at',
            field=models.DateTimeField(default=None),
        ),
    ]