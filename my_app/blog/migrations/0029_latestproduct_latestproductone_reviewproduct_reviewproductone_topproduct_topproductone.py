# Generated by Django 3.1 on 2020-09-17 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_delete_search'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_name', models.CharField(max_length=300)),
                ('price', models.TextField(max_length=50)),
                ('Description', models.TextField(blank=True, max_length=600)),
                ('Image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='LatestProductOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_name', models.CharField(max_length=300)),
                ('price', models.TextField(max_length=50)),
                ('Description', models.TextField(blank=True, max_length=600)),
                ('Image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_name', models.CharField(max_length=300)),
                ('price', models.TextField(max_length=50)),
                ('Description', models.TextField(blank=True, max_length=600)),
                ('Image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewProductOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_name', models.CharField(max_length=300)),
                ('price', models.TextField(max_length=50)),
                ('Description', models.TextField(blank=True, max_length=600)),
                ('Image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='TopProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_name', models.CharField(max_length=300)),
                ('price', models.TextField(max_length=50)),
                ('Description', models.TextField(blank=True, max_length=600)),
                ('Image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='TopProductOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_name', models.CharField(max_length=300)),
                ('price', models.TextField(max_length=50)),
                ('Description', models.TextField(blank=True, max_length=600)),
                ('Image', models.ImageField(upload_to='')),
            ],
        ),
    ]
