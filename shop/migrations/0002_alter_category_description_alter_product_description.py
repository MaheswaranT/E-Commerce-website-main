# Generated by Django 5.0.6 on 2024-06-20 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=1500),
        ),
    ]
