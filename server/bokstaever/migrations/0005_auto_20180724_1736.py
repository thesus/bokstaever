# Generated by Django 2.0.4 on 2018-07-24 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bokstaever', '0004_auto_20180724_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]