# Generated by Django 4.2 on 2023-05-06 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(unique=True, upload_to='images/')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
