# Generated by Django 2.0.7 on 2019-07-24 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='description',
            field=models.TextField(default='None'),
            preserve_default=False,
        ),
    ]