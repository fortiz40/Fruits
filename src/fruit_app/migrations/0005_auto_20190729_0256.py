# Generated by Django 2.0.7 on 2019-07-29 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit_app', '0004_auto_20190727_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
