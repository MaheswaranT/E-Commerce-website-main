# Generated by Django 5.0.6 on 2024-06-21 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_category_description_alter_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Catagory',
            new_name='category',
        ),
    ]