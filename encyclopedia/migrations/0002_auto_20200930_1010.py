# Generated by Django 3.1.1 on 2020-09-30 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myentries',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]