# Generated by Django 2.2 on 2019-04-09 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bokstaever", "0026_auto_20190409_1308"),
    ]

    operations = [
        migrations.AlterModelOptions(name="pagemodel", options={"ordering": ["-pk"]},),
        migrations.DeleteModel(name="Page",),
    ]
