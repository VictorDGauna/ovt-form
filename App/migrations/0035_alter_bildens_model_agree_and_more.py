# Generated by Django 5.0 on 2023-12-23 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0034_alter_bildens_model_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bildens_model',
            name='agree',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Agree'),
        ),
        migrations.AlterField(
            model_name='bildens_model',
            name='agreeTerms',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='agree terms'),
        ),
        migrations.AlterField(
            model_name='bildens_model',
            name='authorize',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Yes'),
        ),
        migrations.AlterField(
            model_name='bildens_model',
            name='married',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='married'),
        ),
        migrations.AlterField(
            model_name='bildens_model',
            name='other',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='other'),
        ),
        migrations.AlterField(
            model_name='bildens_model',
            name='single',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='single'),
        ),
    ]
