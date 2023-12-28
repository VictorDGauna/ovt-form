# Generated by Django 5.0 on 2023-12-23 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0037_remove_bildens_model_agree_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bildens_model',
            name='agree',
            field=models.BooleanField(blank=True, max_length=100, null=True, verbose_name='Agree'),
        ),
        migrations.AddField(
            model_name='bildens_model',
            name='agreeTerms',
            field=models.BooleanField(blank=True, max_length=100, null=True, verbose_name='agree terms'),
        ),
        migrations.AddField(
            model_name='bildens_model',
            name='authorize',
            field=models.BooleanField(blank=True, max_length=100, null=True, verbose_name='Yes'),
        ),
        migrations.AddField(
            model_name='bildens_model',
            name='married',
            field=models.BooleanField(blank=True, max_length=100, null=True, verbose_name='married'),
        ),
        migrations.AddField(
            model_name='bildens_model',
            name='other',
            field=models.BooleanField(blank=True, max_length=100, null=True, verbose_name='other'),
        ),
        migrations.AddField(
            model_name='bildens_model',
            name='single',
            field=models.BooleanField(blank=True, max_length=100, null=True, verbose_name='single'),
        ),
    ]
