# Generated by Django 2.2 on 2019-04-18 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bokstaever", "0029_auto_20190418_0855"),
    ]

    operations = [
        migrations.AlterField(
            model_name="databasepage",
            name="image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="images.Image",
            ),
        ),
        migrations.AlterField(
            model_name="gallery",
            name="images",
            field=models.ManyToManyField(to="images.Image"),
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="images.Image",
            ),
        ),
    ]
