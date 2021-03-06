# Generated by Django 2.0.4 on 2018-04-30 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="File",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("height", models.PositiveIntegerField()),
                ("width", models.PositiveIntegerField()),
                (
                    "path",
                    models.ImageField(
                        height_field="height", upload_to="upload", width_field="width"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="file",
            name="image",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="bokstaever.Image"
            ),
        ),
    ]
