# Generated by Django 3.2 on 2021-06-01 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakerystore', '0004_rename_status_invoice_invoice_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='created',
            field=models.DateField(default='2021-04-01'),
        ),
    ]