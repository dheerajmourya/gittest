# Generated by Django 5.1.6 on 2025-03-13 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_hotelprice_transportprice_volvoprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('HOTEL_STANDARD', 'Hotel - Standard'), ('HOTEL_DELUXE', 'Hotel - Deluxe'), ('HOTEL_SUPER_DELUXE', 'Hotel - Super Deluxe'), ('TRANSPORT_SEDAN', 'Transport - Sedan'), ('TRANSPORT_SUV', 'Transport - SUV'), ('TRANSPORT_TEMPO_14', 'Transport - Tempo 14'), ('TRANSPORT_TEMPO_17', 'Transport - Tempo 17'), ('VOLVO_1_SIDE', 'Volvo - One Side'), ('VOLVO_BOTH_SIDE', 'Volvo - Both Side')], max_length=50, unique=True)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
