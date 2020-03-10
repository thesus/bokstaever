# Generated by Django 2.0.4 on 2018-04-30 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bokstaever", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("headline", models.CharField(max_length=200)),
                ("text", models.TextField()),
                ("published", models.DateField()),
                ("draft", models.BooleanField(default=False)),
                ("url_slug", models.CharField(max_length=200)),
                ("editors", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                (
                    "image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bokstaever.Image",
                    ),
                ),
            ],
        ),
    ]
