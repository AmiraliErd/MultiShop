# Generated by Django 5.0 on 2024-03-31 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_order_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discountcode',
            options={'verbose_name': 'کد تخفیف', 'verbose_name_plural': 'کد های تخفیف'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'سفارش', 'verbose_name_plural': 'سفارش ها'},
        ),
    ]
