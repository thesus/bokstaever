# Generated by Django 2.0.4 on 2018-08-17 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bokstaever", "0020_auto_20180816_1809"),
    ]

    operations = [
        migrations.RemoveField(model_name="page", name="gallery",),
        migrations.RemoveField(model_name="post", name="gallery",),
    ]