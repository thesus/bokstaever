# Generated by Django 2.0.4 on 2018-07-26 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bokstaever", "0010_auto_20180726_0850"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="image",
            field=models.ImageField(upload_to="upload"),
        ),
        migrations.AlterField(
            model_name="image",
            name="thumbnail",
            field=models.ImageField(upload_to="thumnails"),
        ),
    ]