# Generated by Django 2.0.4 on 2018-07-26 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bokstaever', '0008_settings_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AddField(
            model_name='image',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='thumnails'),
        ),
    ]
