# Generated by Django 4.2 on 2023-04-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(unique=True)),
                ('info_1', models.CharField(blank=True, max_length=255, null=True)),
                ('info_2', models.CharField(blank=True, max_length=255, null=True)),
                ('info_3', models.CharField(blank=True, max_length=255, null=True)),
                ('info_4', models.CharField(blank=True, max_length=255, null=True)),
                ('info_5', models.CharField(blank=True, max_length=255, null=True)),
                ('info_6', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=17, unique=True, verbose_name='Tell')),
                ('email', models.CharField(max_length=50, unique=True, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=520, unique=True)),
                ('cover', models.ImageField(unique=True, upload_to='images/')),
            ],
        ),
    ]
