# Generated by Django 4.2.4 on 2023-08-04 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_app', '0006_storeitem_added_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='zipcode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='storeitem',
            name='store_zipcode',
            field=models.CharField(max_length=10),
        ),
    ]
