# Generated by Django 3.1 on 2020-09-13 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_shop_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
