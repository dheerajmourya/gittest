# Generated by Django 5.1.6 on 2025-03-14 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_tripplacepricing_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tripplacepricing',
            name='date',
        ),
        migrations.AddField(
            model_name='tripplacepricing',
            name='end_date',
            field=models.DateField(default='2025-01-01', verbose_name='Price Valid To'),
        ),
        migrations.AddField(
            model_name='tripplacepricing',
            name='start_date',
            field=models.DateField(default='2025-01-01', verbose_name='Price Valid From'),
        ),
    ]
