# Generated by Django 3.1 on 2020-09-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_auto_20200917_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField()),
                ('description', models.TextField(max_length=3000)),
                ('image1', models.ImageField(blank=True, upload_to='')),
                ('image2', models.ImageField(blank=True, upload_to='')),
                ('image3', models.ImageField(blank=True, upload_to='')),
                ('image4', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Shirts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField()),
                ('description', models.TextField(max_length=3000)),
                ('image1', models.ImageField(blank=True, upload_to='')),
                ('image2', models.ImageField(blank=True, upload_to='')),
                ('image3', models.ImageField(blank=True, upload_to='')),
                ('image4', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Shorts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField()),
                ('description', models.TextField(max_length=3000)),
                ('image1', models.ImageField(blank=True, upload_to='')),
                ('image2', models.ImageField(blank=True, upload_to='')),
                ('image3', models.ImageField(blank=True, upload_to='')),
                ('image4', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Slippers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField()),
                ('description', models.TextField(max_length=3000)),
                ('image1', models.ImageField(blank=True, upload_to='')),
                ('image2', models.ImageField(blank=True, upload_to='')),
                ('image3', models.ImageField(blank=True, upload_to='')),
                ('image4', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Watches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField()),
                ('description', models.TextField(max_length=3000)),
                ('image1', models.ImageField(blank=True, upload_to='')),
                ('image2', models.ImageField(blank=True, upload_to='')),
                ('image3', models.ImageField(blank=True, upload_to='')),
                ('image4', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
