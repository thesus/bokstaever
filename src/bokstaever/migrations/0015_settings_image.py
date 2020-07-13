# Generated by Django 2.0.4 on 2018-08-03 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bokstaever", "0014_auto_20180801_1054"),
    ]

    operations = [
        migrations.AddField(
            model_name="settings",
            name="image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="bokstaever.Image",
            ),
        ),
    ]