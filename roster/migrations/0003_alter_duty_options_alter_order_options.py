# Generated by Django 5.0.1 on 2024-01-30 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0002_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='duty',
            options={'verbose_name_plural': 'Duty'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Order'},
        ),
    ]
