# Generated by Django 2.0.4 on 2018-05-01 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bokstaever', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bokstaever.Image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateField(auto_now_add=True),
        ),
    ]