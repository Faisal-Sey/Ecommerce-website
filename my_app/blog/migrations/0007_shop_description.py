# Generated by Django 3.1 on 2020-09-12 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_shop_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='description',
            field=models.TextField(default='', max_length=3000),
            preserve_default=False,
        ),
    ]
