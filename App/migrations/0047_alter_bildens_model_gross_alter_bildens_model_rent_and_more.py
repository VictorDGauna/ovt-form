# Generated by Django 5.0 on 2023-12-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0046_alter_bildens_model_employer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bildens_model',
            name='gross',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bildens_model',
            name='rent',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bildens_model',
            name='work',
            field=models.TextField(default=''),
        ),
    ]
