# Generated by Django 5.0 on 2023-12-29 05:39

from django.db import migrations
from django.db import models



class Migration(migrations.Migration):

    dependencies = [
        ('App', '0068_alter_bildens_model_aptadress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bildens_model',
            name='who',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Who Reffered'),
        ),
    ]