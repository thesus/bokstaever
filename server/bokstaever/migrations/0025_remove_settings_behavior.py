# Generated by Django 2.2 on 2019-04-06 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bokstaever', '0024_auto_20181117_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='behavior',
        ),
    ]
