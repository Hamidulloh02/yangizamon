# Generated by Django 4.2 on 2023-05-22 23:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_qarashlarimiz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kassalliklar',
            name='description',
            field=ckeditor.fields.RichTextField(unique=True),
        ),
        migrations.AlterField(
            model_name='yangiliklar',
            name='description',
            field=ckeditor.fields.RichTextField(unique=True),
        ),
    ]
