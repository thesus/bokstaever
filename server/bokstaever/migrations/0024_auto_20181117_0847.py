# Generated by Django 2.1.2 on 2018-11-17 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bokstaever', '0023_auto_20180929_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='theme',
            field=models.CharField(choices=[('brevlada', 'brevlåda'), ('frimarke', 'frimärke')], default='brevlada', max_length=50),
        ),
    ]
