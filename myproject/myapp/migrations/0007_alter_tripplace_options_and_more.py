# Generated by Django 5.1.6 on 2025-03-14 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_tripplacepricing_deluxe_extra_bed_price_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tripplace',
            options={'verbose_name': 'Destination', 'verbose_name_plural': 'Destinations'},
        ),
        migrations.AlterModelOptions(
            name='tripplacepricing',
            options={'verbose_name': 'Destination Price', 'verbose_name_plural': 'Destination Price'},
        ),
    ]
