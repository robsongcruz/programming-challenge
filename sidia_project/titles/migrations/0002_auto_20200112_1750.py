# Generated by Django 3.0.2 on 2020-01-12 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='original_title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='title',
            name='primary_title',
            field=models.CharField(max_length=200),
        ),
    ]