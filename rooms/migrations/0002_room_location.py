# Generated by Django 3.2.7 on 2022-12-03 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
    ]