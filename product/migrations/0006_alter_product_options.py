# Generated by Django 5.0 on 2024-03-31 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_color_alter_product_size'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
    ]
