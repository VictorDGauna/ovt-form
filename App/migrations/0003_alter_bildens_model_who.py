# Generated by Django 5.0 on 2024-01-04 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_remove_bildens_model_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bildens_model',
            name='who',
            field=models.TextField(null=True, verbose_name='Who Reffered'),
        ),
    ]