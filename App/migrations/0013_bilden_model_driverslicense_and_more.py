# Generated by Django 5.0 on 2023-12-23 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_alter_bilden_model_dateofbirth'),
    ]

    operations = [
        migrations.AddField(
            model_name='bilden_model',
            name='driversLicense',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='bilden_model',
            name='numberSecurity',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
